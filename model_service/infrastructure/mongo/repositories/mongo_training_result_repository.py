from bson import ObjectId

from model_service.domain.entities.training.training_result import TrainingResult
from model_service.domain.repositories.abstract_training_result_repository import AbstractTrainingResultRepository
from model_service.infrastructure.mongo.mappers.abstract_mongo_mapper import AbstractMongoMapper
from model_service.infrastructure.mongo.documents.training.training_result_document import TrainingResultDocument


class MongoTrainingResultRepository(AbstractTrainingResultRepository):
    def __init__(self, mapper: AbstractMongoMapper[TrainingResult, TrainingResultDocument]) -> None:
        self._mapper = mapper

    def save(self, training_result: TrainingResult) -> TrainingResult:
        training_result_document = self._mapper.entity_to_document(training_result)
        training_result_document = training_result_document.save()

        return self._mapper.document_to_entity(training_result_document)

    def get_by_training_session_id(self, training_session_id: str) -> TrainingResult | None:
        training_result_document = TrainingResultDocument.objects(
            training_session_id=ObjectId(training_session_id)
        ).first()

        if training_result_document is None:
            return None

        return self._mapper.document_to_entity(training_result_document)

    def delete_by_id(self, training_result_id: str) -> None:
        TrainingResultDocument.objects(id=ObjectId(training_result_id)).delete()
