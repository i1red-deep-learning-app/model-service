import uuid

import attrs

from model_service.domain.entities.core.generated import GENERATED_VALUE
from model_service.domain.repositories.abstract_table_dataset_repository import (
    AbstractTableDatasetRepository,
)
from model_service.domain.entities.dataset.table_dataset import TableDataset


class FakeTableDatasetRepository(AbstractTableDatasetRepository):
    _table_datasets: dict[str, TableDataset]

    def __init__(self) -> None:
        self._table_datasets = {}

    def save(self, table_dataset: TableDataset) -> TableDataset:
        if table_dataset.id is GENERATED_VALUE:
            persisted_table_dataset = attrs.evolve(table_dataset, id=uuid.uuid4().hex)
        else:
            persisted_table_dataset = attrs.evolve(table_dataset)

        self._table_datasets[persisted_table_dataset.id] = persisted_table_dataset

        return persisted_table_dataset

    def get_by_id(self, table_dataset_id: str) -> TableDataset | None:
        return self._table_datasets.get(table_dataset_id)

    def get_user_datasets(self, user: str) -> list[TableDataset]:
        return [table_dataset for table_dataset in self._table_datasets.values() if table_dataset.user == user]
