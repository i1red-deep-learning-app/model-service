from model_service.application.schemas.table_dataset_schema import TableDatasetSchema
from model_service.domain.entities.dataset.table_dataset import TableDataset
from model_service.application.shared.execution_context import ExecutionContext
from model_service.shared.dependency_management.dependency_kind import SCOPED
from model_service.shared.dependency_management.provide import Dependency, provide


@provide
def map_table_dataset_from_schema(
    schema: TableDatasetSchema, execution_context: ExecutionContext = Dependency(SCOPED)
) -> TableDataset:
    return TableDataset(user=execution_context.user, file_key=schema.file_key, label_column=schema.label_column)
