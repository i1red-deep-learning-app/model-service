from pydantic import BaseModel

from model_service.application.schemas.table_dataset_schema import TableDatasetSchema


class CreateTableDataset(BaseModel):
    table_dataset: TableDatasetSchema
