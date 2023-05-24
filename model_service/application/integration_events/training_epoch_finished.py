import attrs

from model_service.application.integration_events.core.integration_event import IntegrationEvent


@attrs.define
class TrainingEpochFinished(IntegrationEvent):
    training_session_id: str = attrs.field()
    epoch: int = attrs.field()
