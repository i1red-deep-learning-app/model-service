from uuid import UUID

import attrs

from model_service.domain.entities.training.training_session import TrainingSession
from model_service.domain.repositories.abstract_training_session_repository import AbstractTrainingSessionRepository


class FakeTrainingSessionRepository(AbstractTrainingSessionRepository):
    _training_sessions: dict[UUID, TrainingSession]

    def __init__(self) -> None:
        self._training_sessions = {}

    def save(self, training_session: TrainingSession) -> TrainingSession:
        persisted_training_session = attrs.evolve(training_session)
        self._training_sessions[persisted_training_session.id] = persisted_training_session

        return persisted_training_session

    def get_by_id(self, training_session_id: UUID) -> TrainingSession | None:
        return self._training_sessions.get(training_session_id)

    def get_user_sessions(self, user: str) -> list[TrainingSession]:
        return [
            training_session for training_session in self._training_sessions.values() if training_session.user == user
        ]
