import pytest

from model_service.domain.repositories.abstract_training_result_repository import AbstractTrainingResultRepository
from model_service.infrastructure.fake.repositories.fake_training_result_repository import FakeTrainingResultRepository


@pytest.fixture
def training_result_repository() -> AbstractTrainingResultRepository:
    return FakeTrainingResultRepository()
