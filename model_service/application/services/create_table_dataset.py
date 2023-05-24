from model_service.application.commands.create_table_dataset import CreateTableDataset
from model_service.application.integration_events.core.publishers import publish_integration_event
from model_service.application.integration_events.table_dataset_created import TableDatasetCreated
from model_service.application.schema_mappers.map_table_dataset_from_schema import map_table_dataset_from_schema
from model_service.dependencies.dependency_management.provide import Dependency, provide
from model_service.domain.repositories.abstract_table_dataset_repository import AbstractTableDatasetRepository
from model_service.utility.logging.log_function_execution import log_function_execution


@log_function_execution()
@provide
def create_table_dataset(
    command: CreateTableDataset,
    repository: AbstractTableDatasetRepository = Dependency(),
) -> None:
    table_dataset = map_table_dataset_from_schema(command.table_dataset)
    persisted_table_dataset = repository.save(table_dataset)
    event = TableDatasetCreated(table_dataset_id=persisted_table_dataset.id)
    publish_integration_event(event)
