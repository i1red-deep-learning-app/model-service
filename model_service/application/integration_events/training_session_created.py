from uuid import UUID

import attrs

from model_service.application.integration_events.core.integration_event import IntegrationEvent


@attrs.define
class TrainingSessionCreated(IntegrationEvent):
    training_session_id: UUID
