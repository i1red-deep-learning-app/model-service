from model_service.application.schemas.table_dataset_schema import TableDatasetSchema
from model_service.domain.entities.dataset.table_dataset import TableDataset


def map_table_dataset_from_schema(schema: TableDatasetSchema) -> TableDataset:
    return TableDataset.create(user=schema.user, file_key=schema.file_key, label_column=schema.label_column)
