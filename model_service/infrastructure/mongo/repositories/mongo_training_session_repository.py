from bson import ObjectId

from model_service.domain.entities.training.training_session import TrainingSession
from model_service.domain.repositories.abstract_training_session_repository import AbstractTrainingSessionRepository
from model_service.infrastructure.mongo.mappers.abstract_mongo_mapper import AbstractMongoMapper
from model_service.infrastructure.mongo.models.training.training_session_model import TrainingSessionModel


class MongoTrainingSessionRepository(AbstractTrainingSessionRepository):
    def __init__(self, mapper: AbstractMongoMapper[TrainingSession, TrainingSessionModel]) -> None:
        self._mapper = mapper

    def save(self, training_session: TrainingSession) -> TrainingSession:
        training_session_model = self._mapper.entity_to_model(training_session)
        training_session_model = training_session_model.save()

        return self._mapper.model_to_entity(training_session_model)

    def get_by_id(self, training_session_id: str) -> TrainingSession | None:
        training_session_model = TrainingSessionModel.objects(id=ObjectId(training_session_id)).first()

        if training_session_model is None:
            return None

        return self._mapper.model_to_entity(training_session_model)

    def get_user_sessions(self, user: str) -> list[TrainingSession]:
        training_session_model_iterable = TrainingSessionModel.objects(user=user)
        return list(map(self._mapper.model_to_entity, training_session_model_iterable))
