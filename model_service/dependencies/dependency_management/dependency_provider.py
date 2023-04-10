from typing import TypeVar, Type, Final

TDependency = TypeVar("TDependency")


class DependencyProvider:
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


_DEFAULT_PROVIDER: Final = DependencyProvider()


def get_default_provider() -> DependencyProvider:
    return _DEFAULT_PROVIDER
