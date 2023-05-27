from uuid import UUID, uuid4

import attrs

from model_service.domain.entities.core.entity import Entity
from model_service.domain.entities.value_objects.linear_layer import LinearLayer


@attrs.define(kw_only=True)
class FeedForwardNetwork(Entity):
    id: UUID = attrs.field(factory=uuid4)
    user: str = attrs.field()
    layers: list[LinearLayer] = attrs.field()
