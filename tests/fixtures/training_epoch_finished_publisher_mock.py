from typing import Generator
from unittest.mock import MagicMock

import pytest

from model_service.application.integration_events.core.publishers import (
    register_integration_event_publisher,
    unregister_integration_event_publisher,
)
from model_service.application.integration_events.training_epoch_finished import TrainingEpochFinished


@pytest.fixture
def training_epoch_finished_publisher_mock() -> Generator[MagicMock, None, None]:
    event_publisher_mock = MagicMock()
    register_integration_event_publisher(TrainingEpochFinished, event_publisher_mock)
    yield event_publisher_mock
    unregister_integration_event_publisher(TrainingEpochFinished, event_publisher_mock)
