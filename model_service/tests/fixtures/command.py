import pytest

from model_service.application.external_commands.start_ffn_training import StartFfnTraining


@pytest.fixture
def command(training_session_id: str) -> StartFfnTraining:
    return StartFfnTraining(training_session_id=training_session_id)
