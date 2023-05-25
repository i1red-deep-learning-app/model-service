from typing import Final

from model_service.shared.dependency_management.providers.scoped_dependency_provider import (
    ScopedDependencyProvider,
)
from model_service.shared.dependency_management.providers.singleton_dependency_provider import (
    SingletonDependencyProvider,
)

_SINGLETON_PROVIDER: Final = SingletonDependencyProvider()
_SCOPED_PROVIDER: Final = ScopedDependencyProvider()


def get_singleton_provider() -> SingletonDependencyProvider:
    return _SINGLETON_PROVIDER


def get_scoped_provider() -> ScopedDependencyProvider:
    return _SCOPED_PROVIDER
