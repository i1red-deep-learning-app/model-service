from typing import TypeVar, Type

from mongoengine import Document

from model_service.domain.entities.core.entity import Entity
from model_service.infrastructure.mongo.mappers.abstract_mongo_mapper import AbstractMongoMapper

TEntity = TypeVar("TEntity", bound=Entity)
TDocument = TypeVar("TDocument", bound=Document)


class DefaultMongoMapper(AbstractMongoMapper[TEntity, TDocument]):
    def __init__(self, entity_type: Type[TEntity], model_type: Type[TDocument]) -> None:
        self._entity_type = entity_type
        self._document_type = model_type

    def entity_to_document(self, entity: TEntity) -> TDocument:
        model_kwargs = {}

        for field_name, field_type in self._document_type._fields.items():
            model_kwargs[field_name] = getattr(entity, field_name)

        return self._document_type(**model_kwargs)

    def document_to_entity(self, model: TDocument) -> TEntity:
        entity_kwargs = {}

        for field_name, field_type in self._document_type._fields.items():
            entity_kwargs[field_name] = getattr(model, field_name)

        return self._entity_type(**entity_kwargs)
