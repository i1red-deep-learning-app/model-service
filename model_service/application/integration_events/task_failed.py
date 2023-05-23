import attrs

from model_service.application.integration_events.integration_event import IntegrationEvent


@attrs.define
class TaskFailed(IntegrationEvent):
    task_name: str
    error_type: str
    error_message: str
