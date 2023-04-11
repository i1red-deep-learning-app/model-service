import attrs

from model_service.domain.entities.core.entity import BaseEntity, entity
from model_service.domain.entities.core.generated import Generated
from model_service.domain.entities.value_objects.linear_layer import LinearLayer


@entity
@attrs.define
class FeedForwardNetwork(BaseEntity):
    id: Generated[str] = attrs.field()
    user: str = attrs.field()
    layers: list[LinearLayer] = attrs.field()
