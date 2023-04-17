from bson import ObjectId

from model_service.domain.entities.training.training_result import TrainingResult
from model_service.domain.repositories.abstract_training_result_repository import AbstractTrainingResultRepository
from model_service.infrastructure.mongo.mappers.abstract_mapper import AbstractMapper
from model_service.infrastructure.mongo.models.training.training_result_model import TrainingResultModel


class MongoTrainingResultRepository(AbstractTrainingResultRepository):
    def __init__(self, mapper: AbstractMapper[TrainingResult, TrainingResultModel]) -> None:
        self._mapper = mapper

    def save(self, training_result: TrainingResult) -> TrainingResult:
        training_result_model = self._mapper.entity_to_model(training_result)
        training_result_model = training_result_model.save()

        return self._mapper.model_to_entity(training_result_model)

    def get_by_training_session_id(self, training_session_id: str) -> TrainingResult | None:
        training_result_model = TrainingResultModel.objects(training_session_id=ObjectId(training_session_id)).first()

        if training_result_model is None:
            return None

        return self._mapper.model_to_entity(training_result_model)

    def delete_by_id(self, training_result_id: str) -> None:
        TrainingResultModel.objects(training_result_id=ObjectId(training_result_id)).delete()
