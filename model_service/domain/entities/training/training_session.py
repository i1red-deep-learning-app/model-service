import attrs

from model_service.domain.entities.core.entity import BaseEntity, entity
from model_service.domain.entities.core.generated import Generated
from model_service.domain.entities.training.loss_function_type import LossFunctionType
from model_service.domain.entities.training.metric_type import MetricType
from model_service.domain.entities.value_objects.optimizer import Optimizer


@entity
@attrs.define
class TrainingSession(BaseEntity):
    id: Generated[str] = attrs.field()
    user: str = attrs.field()
    network_id: str = attrs.field()
    dataset_id: str = attrs.field()
    optimizer: Optimizer = attrs.field()
    loss_function: LossFunctionType = attrs.field()
    metrics: list[MetricType] = attrs.field()
    epochs: int = attrs.field()
    batch_size: int = attrs.field()
    validation_split: float = attrs.field()
