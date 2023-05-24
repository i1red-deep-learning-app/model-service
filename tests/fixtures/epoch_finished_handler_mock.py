from typing import Generator
from unittest.mock import MagicMock

import pytest

from model_service.domain.events.epoch_finished import EpochFinished
from model_service.domain.events.core.handlers import register_domain_event_handler, unregister_domain_event_handler


@pytest.fixture
def epoch_finished_handler_mock() -> Generator[MagicMock, None, None]:
    event_handler_mock = MagicMock()
    register_domain_event_handler(EpochFinished, event_handler_mock)
    yield event_handler_mock
    unregister_domain_event_handler(EpochFinished, event_handler_mock)
