from bson import ObjectId

from model_service.domain.entities.training.training_session import TrainingSession
from model_service.domain.repositories.abstract_training_session_repository import AbstractTrainingSessionRepository
from model_service.infrastructure.mongo.mappers.abstract_mongo_mapper import AbstractMongoMapper
from model_service.infrastructure.mongo.documents.training.training_session_document import TrainingSessionDocument


class MongoTrainingSessionRepository(AbstractTrainingSessionRepository):
    def __init__(self, mapper: AbstractMongoMapper[TrainingSession, TrainingSessionDocument]) -> None:
        self._mapper = mapper

    def save(self, training_session: TrainingSession) -> TrainingSession:
        training_session_document = self._mapper.entity_to_document(training_session)
        training_session_document = training_session_document.save()

        return self._mapper.document_to_entity(training_session_document)

    def get_by_id(self, training_session_id: str) -> TrainingSession | None:
        training_session_document = TrainingSessionDocument.objects(id=ObjectId(training_session_id)).first()

        if training_session_document is None:
            return None

        return self._mapper.document_to_entity(training_session_document)

    def get_user_sessions(self, user: str) -> list[TrainingSession]:
        training_session_document_iterable = TrainingSessionDocument.objects(user=user)
        return list(map(self._mapper.document_to_entity, training_session_document_iterable))
