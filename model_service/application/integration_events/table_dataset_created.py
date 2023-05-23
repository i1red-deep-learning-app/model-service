import attrs

from model_service.application.integration_events.integration_event import IntegrationEvent


@attrs.define
class TableDatasetCreated(IntegrationEvent):
    table_dataset_id: str
