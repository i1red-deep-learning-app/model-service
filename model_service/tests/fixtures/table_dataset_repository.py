import pytest

from model_service.domain.entities.dataset.table_dataset import TableDataset
from model_service.domain.repositories.abstract_table_dataset_repository import AbstractTableDatasetRepository
from model_service.infrastructure.fake.repositories.fake_table_dataset_repository import FakeTableDatasetRepository


@pytest.fixture
def table_dataset_repository(dataset_info: TableDataset) -> AbstractTableDatasetRepository:
    repository = FakeTableDatasetRepository()
    repository.save(dataset_info)
    return repository
