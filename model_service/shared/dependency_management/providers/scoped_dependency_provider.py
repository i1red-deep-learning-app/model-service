from typing import TypeVar, Type

from model_service.shared.dependency_management.providers.abstract_dependency_provider import (
    AbstractDependencyProvider,
)

TDependency = TypeVar("TDependency")


class ScopedDependencyProvider(AbstractDependencyProvider):
    _dependencies: dict[Type[TDependency], TDependency]

    def __init__(self) -> None:
        self._dependencies = {}

    def _set(self, type_: Type[TDependency], obj: TDependency) -> None:
        if type_ in self._dependencies:
            raise ValueError(f"Dependency for type {type_.__name__} is already set")

        self._dependencies[type_] = obj

    def _remove(self, type_: Type[TDependency]) -> None:
        if type_ not in self._dependencies:
            raise ValueError(f"Dependency for type {type_.__name__} is not set")

        del self._dependencies[type_]

    def get(self, type_: Type[TDependency]) -> TDependency:
        if type_ not in self._dependencies:
            raise ValueError(f"Dependency for type {type_.__name__} is not set")

        return self._dependencies[type_]


class ScopedDependencies:
    _scope_dependencies: list[type]

    def __init__(self, scoped_provider: ScopedDependencyProvider) -> None:
        self._provider = scoped_provider
        self._scope_dependencies = []

    def __enter__(self) -> "ScopedDependencies":
        return self

    def set(self, type_: Type[TDependency], obj: TDependency) -> None:
        self._provider._set(type_, obj)
        self._scope_dependencies.append(type_)

    def __exit__(self, exc_type: Type[Exception], exc_val: Exception, exc_tb: "traceback") -> bool:
        for dependency_type in self._scope_dependencies:
            self._provider._remove(dependency_type)

        self._scope_dependencies = []
        return False
