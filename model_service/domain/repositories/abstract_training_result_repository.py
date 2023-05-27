from abc import ABC, abstractmethod
from uuid import UUID

from model_service.domain.entities.training.training_result import TrainingResult


class AbstractTrainingResultRepository(ABC):
    @abstractmethod
    def save(self, training_result: TrainingResult) -> TrainingResult:
        """Save training result info to database"""

    @abstractmethod
    def get_by_training_session_id(self, training_session_id: UUID) -> TrainingResult | None:
        """Get training result by id"""

    @abstractmethod
    def delete_by_id(self, training_result_id: UUID) -> None:
        """Get training result by id"""
