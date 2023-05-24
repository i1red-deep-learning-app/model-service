import attrs
import numpy as np

from model_service.domain.events.core.domain_event import DomainEvent


@attrs.define
class EpochFinished(DomainEvent):
    user: str = attrs.field()
    training_session_id: str = attrs.field()
    epoch: int = attrs.field()
    loss: float = attrs.field()
    validation_loss: float = attrs.field()
    metrics: dict = attrs.field()
    weights: list[np.ndarray] = attrs.field()
