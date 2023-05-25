from typing import TypeVar, Type

from model_service.shared.dependency_management.providers.abstract_dependency_provider import (
    AbstractDependencyProvider,
)

TDependency = TypeVar("TDependency")


class SingletonDependencyProvider(AbstractDependencyProvider):
    _dependencies: dict[Type[TDependency], TDependency]

    def __init__(self) -> None:
        self._dependencies = {}

    def set(self, type_: Type[TDependency], obj: TDependency) -> None:
        if type_ in self._dependencies:
            raise ValueError(f"Dependency for type {type_.__name__} is already set")

        self._dependencies[type_] = obj

    def get(self, type_: Type[TDependency]) -> TDependency:
        if type_ not in self._dependencies:
            raise ValueError(f"Dependency for type {type_.__name__} is not set")

        return self._dependencies[type_]
