import functools
import inspect
from collections.abc import Callable
from typing import TypeVar, Any, Final

from model_service.shared.dependency_management.dependency_kind import DependencyKind, SINGLETON, SCOPED
from model_service.shared.dependency_management.providers.abstract_dependency_provider import (
    AbstractDependencyProvider,
)
from model_service.shared.dependency_management.provider_getters import (
    get_singleton_provider,
    get_scoped_provider,
)

TCallable = TypeVar("TCallable", bound=Callable)


_PROVIDERS_MAP: Final[dict[DependencyKind, AbstractDependencyProvider]] = {
    SINGLETON: get_singleton_provider(),
    SCOPED: get_scoped_provider(),
}


class Dependency:
    provider: AbstractDependencyProvider

    def __init__(self, dependency_kind: DependencyKind = SINGLETON, type_: type | None = None) -> None:
        self.provider = _PROVIDERS_MAP[dependency_kind]
        self.type_ = type_


def provide(func: TCallable) -> TCallable:
    signature = inspect.signature(func)
    _init_dependency_params(signature)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        bound_arguments = signature.bind(*args, **kwargs)
        bound_arguments.apply_defaults()
        arguments_dict = bound_arguments.arguments
        updated_arguments_dict = _provide_dependencies(arguments_dict)

        return func(**updated_arguments_dict)

    return wrapper


def _init_dependency_params(signature: inspect.Signature) -> None:
    for param_name, param_info in signature.parameters.items():
        if not isinstance(param_info.default, Dependency):
            continue

        dependency_info = param_info.default
        annotation = param_info.annotation

        if dependency_info.type_ is None:
            if annotation is inspect.Parameter.empty:
                raise ValueError(
                    "Can not resolve dependency type. "
                    "Neither parameter annotation nor Dependency.type_ parameter not specified"
                )
            dependency_info.type_ = annotation


def _provide_dependencies(arguments_dict: dict[str, Any]) -> dict[str, Any]:
    updated_arguments_dict = {}

    for arg_name, arg_value in arguments_dict.items():
        if isinstance(arg_value, Dependency):
            dependency_provider = arg_value.provider
            dependency_type = arg_value.type_
            updated_arguments_dict[arg_name] = dependency_provider.get(dependency_type)
        else:
            updated_arguments_dict[arg_name] = arg_value

    return updated_arguments_dict
