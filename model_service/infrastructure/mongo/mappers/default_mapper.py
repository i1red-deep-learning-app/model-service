from typing import TypeVar, Type

from bson import ObjectId
from mongoengine import Document, ObjectIdField

from model_service.domain.entities.core.entity import BaseEntity
from model_service.domain.entities.core.generated import GENERATED_VALUE
from model_service.infrastructure.mongo.mappers.abstract_mapper import AbstractMapper

TEntity = TypeVar("TEntity", bound=BaseEntity)
TModel = TypeVar("TModel", bound=Document)


class DefaultMapper(AbstractMapper[TEntity, TModel]):
    def __init__(self, entity_type: Type[TEntity], model_type: Type[TModel]) -> None:
        self._entity_type = entity_type
        self._model_type = model_type

    def entity_to_model(self, entity: TEntity) -> TModel:
        model_kwargs = {}

        for field_name, field_type in self._model_type._fields.items():
            value = getattr(entity, field_name)

            if value is GENERATED_VALUE:
                continue

            if isinstance(field_type, ObjectIdField):
                value = ObjectId(value)

            model_kwargs[field_name] = value

        return self._model_type(**model_kwargs)

    def model_to_entity(self, model: TModel) -> TEntity:
        entity_kwargs = {}

        for field_name, field_type in self._model_type._fields.items():
            if isinstance(field_type, ObjectIdField):
                value = str(getattr(model, field_name))
            else:
                value = getattr(model, field_name)

            entity_kwargs[field_name] = value

        return self._entity_type(**entity_kwargs)
