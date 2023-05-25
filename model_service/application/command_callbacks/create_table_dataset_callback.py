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
from model_service.application.commands.create_table_dataset import CreateTableDataset
from model_service.application.services.create_table_dataset import create_table_dataset
from model_service.shared.logging.log_exceptions import log_exceptions


@with_execution_context
@handle_command_callback_errors
@log_exceptions
@command_callback(task_name="Create Table Dataset")
def create_table_dataset_callback(
    channel: BlockingChannel,
    method: Basic.Deliver,
    properties: BasicProperties,
    body: bytes,
) -> None:
    try:
        command = CreateTableDataset.parse_raw(body)
    except ValidationError:
        channel.basic_nack(method.delivery_tag, requeue=False)
        raise

    channel.basic_ack(method.delivery_tag)

    create_table_dataset(command)
