from bson import ObjectId

from model_service.infrastructure.mongo.mappers.abstract_mongo_mapper import AbstractMongoMapper
from model_service.infrastructure.mongo.models.dataset.table_dataset import TableDatasetModel
from model_service.domain.repositories.abstract_table_dataset_repository import AbstractTableDatasetRepository
from model_service.domain.entities.dataset.table_dataset import TableDataset


class MongoTableDatasetRepository(AbstractTableDatasetRepository):
    def __init__(self, mapper: AbstractMongoMapper[TableDataset, TableDatasetModel]) -> None:
        self._mapper = mapper

    def save(self, table_dataset: TableDataset) -> TableDataset:
        table_dataset_model = self._mapper.entity_to_model(table_dataset)
        table_dataset_model = table_dataset_model.save()

        return self._mapper.model_to_entity(table_dataset_model)

    def get_by_id(self, table_dataset_id: str) -> TableDataset | None:
        table_dataset_model = TableDatasetModel.objects(id=ObjectId(table_dataset_id)).first()

        if table_dataset_model is None:
            return None

        return self._mapper.model_to_entity(table_dataset_model)

    def get_user_datasets(self, user: str) -> list[TableDataset]:
        table_dataset_model_iterable = TableDatasetModel.objects(user=user)
        return [
            self._mapper.model_to_entity(table_dataset_model) for table_dataset_model in table_dataset_model_iterable
        ]
