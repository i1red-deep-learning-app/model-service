from abc import ABC, abstractmethod
from uuid import UUID

from model_service.domain.entities.training.training_session import TrainingSession


class AbstractTrainingSessionRepository(ABC):
    @abstractmethod
    def save(self, training_session: TrainingSession) -> TrainingSession:
        """Save training session info to database"""

    @abstractmethod
    def get_by_id(self, training_session_id: UUID) -> TrainingSession | None:
        """Get training session info by id"""

    @abstractmethod
    def get_user_sessions(self, user: str) -> list[TrainingSession]:
        """Get list of user's training sessions"""
