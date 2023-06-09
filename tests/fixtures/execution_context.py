import pytest

from model_service.application.shared.execution_context import ExecutionContext


@pytest.fixture
def execution_context(user: str) -> ExecutionContext:
    return ExecutionContext(user=user, metadata={})
