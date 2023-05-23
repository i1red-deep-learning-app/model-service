from typing import Type, ClassVar, Dict, TypeVar

import attrs

from model_service.domain.entities.core.generated import GeneratedType, GENERATED_VALUE, is_generated


TEntity = TypeVar("TEntity", bound="BaseEntity")
TEntityCls = TypeVar("TEntityCls")


def entity(cls: TEntityCls) -> TEntityCls:
    cls._generated_attributes = {attr.name: GENERATED_VALUE for attr in attrs.fields(cls) if is_generated(attr.type)}
    return cls


@entity
@attrs.define
class BaseEntity:
    _generated_attributes: ClassVar[Dict[str, GeneratedType]]

    @classmethod
    def create(cls: Type[TEntity], **kwargs) -> TEntity:
        generated_attributes = cls._generated_attributes.copy()
        kwargs = generated_attributes | kwargs
        return cls(**kwargs)
