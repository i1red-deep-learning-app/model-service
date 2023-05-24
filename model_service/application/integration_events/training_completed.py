import attrs

from model_service.application.integration_events.core.integration_event import IntegrationEvent


@attrs.define
class TrainingCompleted(IntegrationEvent):
    training_session_id: str = attrs.field()
