from bson import ObjectId

from model_service.infrastructure.mongo.mappers.abstract_mongo_mapper import AbstractMongoMapper
from model_service.infrastructure.mongo.documents.dataset.table_dataset_document import TableDatasetDocument
from model_service.domain.repositories.abstract_table_dataset_repository import AbstractTableDatasetRepository
from model_service.domain.entities.dataset.table_dataset import TableDataset


class MongoTableDatasetRepository(AbstractTableDatasetRepository):
    def __init__(self, mapper: AbstractMongoMapper[TableDataset, TableDatasetDocument]) -> None:
        self._mapper = mapper

    def save(self, table_dataset: TableDataset) -> TableDataset:
        table_dataset_document = self._mapper.entity_to_document(table_dataset)
        table_dataset_document = table_dataset_document.save()

        return self._mapper.document_to_entity(table_dataset_document)

    def get_by_id(self, table_dataset_id: str) -> TableDataset | None:
        table_dataset_document = TableDatasetDocument.objects(id=ObjectId(table_dataset_id)).first()

        if table_dataset_document is None:
            return None

        return self._mapper.document_to_entity(table_dataset_document)

    def get_user_datasets(self, user: str) -> list[TableDataset]:
        table_dataset_document_iterable = TableDatasetDocument.objects(user=user)
        return list(map(self._mapper.document_to_entity, table_dataset_document_iterable))
