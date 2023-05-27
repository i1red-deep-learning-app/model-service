from abc import ABC, abstractmethod
from uuid import UUID

from model_service.domain.entities.dataset.table_dataset import TableDataset


class AbstractTableDatasetRepository(ABC):
    @abstractmethod
    def save(self, table_dataset: TableDataset) -> TableDataset:
        """Save table dataset info to database"""

    @abstractmethod
    def get_by_id(self, table_dataset_id: UUID) -> TableDataset | None:
        """Get table dataset by id"""

    @abstractmethod
    def get_user_datasets(self, user: str) -> list[TableDataset]:
        """Get list of info for user's datasets"""
