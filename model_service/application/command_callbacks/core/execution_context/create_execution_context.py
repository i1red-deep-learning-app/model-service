from pika import BasicProperties

from model_service.application.command_callbacks.core.execution_context.exceptions import ExecutionContextCreationError
from model_service.domain.shared.execution_context import ExecutionContext


def create_execution_context(properties: BasicProperties) -> ExecutionContext:
    if properties.headers is None:
        raise ExecutionContextCreationError("No headers provided")

    if "username" not in properties.headers:
        raise ExecutionContextCreationError("'username' header was not provided")

    return ExecutionContext(user=properties.headers["username"], metadata={})
