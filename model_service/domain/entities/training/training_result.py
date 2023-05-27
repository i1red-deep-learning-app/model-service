from uuid import UUID, uuid4

import attrs

from model_service.domain.entities.core.entity import Entity


@attrs.define(kw_only=True)
class TrainingResult(Entity):
    id: UUID = attrs.field(factory=uuid4)
    user: str = attrs.field()
    training_session_id: UUID = attrs.field()
    loss: float = attrs.field()
    validation_loss = attrs.field()
    metrics: dict = attrs.field()
    weights_file_key: str = attrs.field()
