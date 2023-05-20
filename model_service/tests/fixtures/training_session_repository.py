import pytest

from model_service.domain.entities.training.training_session import TrainingSession
from model_service.domain.repositories.abstract_training_session_repository import AbstractTrainingSessionRepository
from model_service.infrastructure.fake.repositories.fake_training_session_repository import (
    FakeTrainingSessionRepository,
)


@pytest.fixture
def training_session_repository(training_session: TrainingSession) -> AbstractTrainingSessionRepository:
    repository = FakeTrainingSessionRepository()
    repository.save(training_session)
    return repository
