import attrs

from model_service.domain.entities.core.entity import entity, BaseEntity
from model_service.domain.entities.core.generated import Generated


@entity
@attrs.define
class TrainingResult(BaseEntity):
    id: Generated[str] = attrs.field()
    user: str = attrs.field()
    training_session_id: str = attrs.field()
    loss: float = attrs.field()
    validation_loss = attrs.field()
    metrics: dict = attrs.field()
    weights_file_key: str = attrs.field()
