from model_service.application.commands.core.command import Command
from model_service.application.schemas.table_dataset_schema import TableDatasetSchema


class CreateTableDataset(Command):
    table_dataset: TableDatasetSchema
