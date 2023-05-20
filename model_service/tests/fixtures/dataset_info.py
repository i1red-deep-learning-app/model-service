import pytest

from model_service.domain.entities.dataset.table_dataset import TableDataset


@pytest.fixture
def dataset_info(table_dataset_id: str, user: str, file_key: str, labels_column: str) -> TableDataset:
    return TableDataset(id=table_dataset_id, user=user, file_key=file_key, label_column=labels_column)
