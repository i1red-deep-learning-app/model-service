from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from mongoengine import Document

from model_service.domain.entities.core.entity import BaseEntity


TEntity = TypeVar("TEntity", bound=BaseEntity)
TModel = TypeVar("TModel", bound=Document)


class AbstractMapper(Generic[TEntity, TModel], ABC):
    @abstractmethod
    def entity_to_model(self, entity: TEntity) -> TModel:
        """Map entity to model"""

    @abstractmethod
    def model_to_entity(self, model: TModel) -> TEntity:
        """Map model to entity"""
