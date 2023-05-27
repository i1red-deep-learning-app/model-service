from uuid import UUID

import attrs

from model_service.domain.entities.training.training_result import TrainingResult
from model_service.domain.repositories.abstract_training_result_repository import (
    AbstractTrainingResultRepository,
)


class FakeTrainingResultRepository(AbstractTrainingResultRepository):
    _training_results: dict[UUID, TrainingResult]

    def __init__(self) -> None:
        self._training_results = {}

    def save(self, training_result: TrainingResult) -> TrainingResult:
        persisted_training_result = attrs.evolve(training_result)
        self._training_results[persisted_training_result.id] = persisted_training_result

        return persisted_training_result

    def get_by_training_session_id(self, training_session_id: UUID) -> TrainingResult | None:
        for training_result in self._training_results.values():
            if training_result.training_session_id == training_session_id:
                return training_result

        return None

    def delete_by_id(self, training_result_id: UUID) -> None:
        del self._training_results[training_result_id]
