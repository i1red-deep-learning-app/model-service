import attrs

from model_service.application.integration_events.integration_event import IntegrationEvent


@attrs.define
class TrainingSessionCreated(IntegrationEvent):
    training_session_id: str
