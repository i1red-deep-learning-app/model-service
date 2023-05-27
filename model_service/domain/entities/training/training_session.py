from uuid import UUID, uuid4

import attrs

from model_service.domain.entities.core.entity import Entity
from model_service.domain.entities.training.loss_function_type import LossFunctionType
from model_service.domain.entities.training.metric_type import MetricType
from model_service.domain.entities.value_objects.optimizer import Optimizer


@attrs.define(kw_only=True)
class TrainingSession(Entity):
    id: UUID = attrs.field(factory=uuid4)
    user: str = attrs.field()
    network_id: UUID = attrs.field()
    dataset_id: UUID = attrs.field()
    optimizer: Optimizer = attrs.field()
    loss_function: LossFunctionType = attrs.field()
    metrics: list[MetricType] = attrs.field()
    epochs: int = attrs.field()
    batch_size: int = attrs.field()
    validation_split: float = attrs.field()
