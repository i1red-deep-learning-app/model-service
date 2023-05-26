from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from mongoengine import Document

from model_service.domain.entities.core.entity import BaseEntity


TEntity = TypeVar("TEntity", bound=BaseEntity)
TDocument = TypeVar("TDocument", bound=Document)


class AbstractMongoMapper(Generic[TEntity, TDocument], ABC):
    @abstractmethod
    def entity_to_document(self, entity: TEntity) -> TDocument:
        """Map entity to model"""

    @abstractmethod
    def document_to_entity(self, model: TDocument) -> TEntity:
        """Map model to entity"""
