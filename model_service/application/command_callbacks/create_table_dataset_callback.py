import logging

from model_service.application.error_handling.handle_command_callback_errors import handle_command_callback_errors
from model_service.application.commands.create_table_dataset import CreateTableDataset
from model_service.application.services.create_table_dataset import create_table_dataset

from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties

logger = logging.getLogger(__name__)


@handle_command_callback_errors("Create Table Dataset")
def create_table_dataset_callback(
    channel: BlockingChannel,
    method: Basic.Deliver,
    properties: BasicProperties,
    body: bytes,
) -> None:
    channel.basic_ack(method.delivery_tag)

    logger.info(f"Handle {CreateTableDataset.__name__}. Serialized body: {body}")
    command = CreateTableDataset.parse_raw(body)
    create_table_dataset(command)
