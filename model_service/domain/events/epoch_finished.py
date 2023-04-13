import attrs


@attrs.define
class EpochFinished:
    user: str = attrs.field()
    training_session_id: str = attrs.field()
    epoch: int = attrs.field()
    loss: float = attrs.field()
    validation_loss: float = attrs.field()
    metrics: dict = attrs.field()
    weights: bytes = attrs.field()
