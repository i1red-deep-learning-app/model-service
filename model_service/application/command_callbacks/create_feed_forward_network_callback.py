import logging

from model_service.application.command_callbacks.core.command_callback import command_callback
from model_service.application.command_callbacks.core.handle_command_callback_errors import (
    handle_command_callback_errors,
)
from model_service.application.commands.create_feed_forward_network import CreateFeedForwardNetwork
from model_service.application.services.create_feed_forward_network import create_feed_forward_network

from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties

from model_service.utility.logging.log_exceptions import log_exceptions

logger = logging.getLogger(__name__)


@handle_command_callback_errors
@log_exceptions
@command_callback(task_name="Create Feed Forward Network")
def create_feed_forward_network_callback(
    channel: BlockingChannel,
    method: Basic.Deliver,
    properties: BasicProperties,
    body: bytes,
) -> None:
    channel.basic_ack(method.delivery_tag)

    logger.info(f"Handle {CreateFeedForwardNetwork.__name__}. Serialized body: {body}")
    command = CreateFeedForwardNetwork.parse_raw(body)
    create_feed_forward_network(command)
