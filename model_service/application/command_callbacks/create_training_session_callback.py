from pydantic import ValidationError

from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties

from model_service.application.command_callbacks.core.command_callback import command_callback
from model_service.application.command_callbacks.core.execution_context.with_execution_context import (
    with_execution_context,
)
from model_service.application.command_callbacks.core.handle_command_callback_errors import (
    handle_command_callback_errors,
)
from model_service.application.commands.create_training_session import CreateTrainingSession
from model_service.application.services.create_training_session import create_training_session
from model_service.shared.logging.log_exceptions import log_exceptions


@with_execution_context
@handle_command_callback_errors
@log_exceptions
@command_callback(task_name="Create Training Session")
def create_training_session_callback(
    channel: BlockingChannel,
    method: Basic.Deliver,
    properties: BasicProperties,
    body: bytes,
) -> None:
    try:
        command = CreateTrainingSession.parse_raw(body)
    except ValidationError:
        channel.basic_nack(method.delivery_tag, requeue=False)
        raise

    channel.basic_ack(method.delivery_tag)

    create_training_session(command)
