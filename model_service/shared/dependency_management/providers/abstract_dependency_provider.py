from abc import ABC, abstractmethod
from typing import TypeVar, Type

TDependency = TypeVar("TDependency")


class AbstractDependencyProvider(ABC):
    @abstractmethod
    def get(self, type_: Type[TDependency]) -> TDependency:
        """Get dependency registered for type"""
