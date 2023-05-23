import logging

from model_service.application.commands.create_feed_forward_network import CreateFeedForwardNetwork
from model_service.application.error_handling.handle_command_callback_errors import handle_command_callback_errors
from model_service.application.commands.start_ffn_training import StartFfnTraining
from model_service.application.services.start_ffn_training import start_ffn_training

from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties

logger = logging.getLogger(__name__)


@handle_command_callback_errors("Start Feed Forward Network Training")
def start_ffn_training_callback(
    channel: BlockingChannel,
    method: Basic.Deliver,
    properties: BasicProperties,
    body: bytes,
) -> None:
    logger.info(f"Handle {CreateFeedForwardNetwork.__name__}. Serialized body: {body}")
    command = StartFfnTraining.parse_raw(body)
    start_ffn_training(command)
