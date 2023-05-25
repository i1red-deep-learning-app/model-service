import functools
import logging

from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties

from model_service.application.command_callbacks.core.command_callback import CommandCallback
from model_service.application.integration_events.core.publishers import publish_integration_event
from model_service.application.integration_events.task_failed import TaskFailed


def handle_command_callback_errors(callback: CommandCallback) -> CommandCallback:
    logger = logging.getLogger(callback.__module__)

    @functools.wraps(callback)
    def wrapper(
        channel: BlockingChannel,
        method: Basic.Deliver,
        properties: BasicProperties,
        body: bytes,
    ) -> None:
        try:
            return callback(channel, method, properties, body)
        except Exception as e:
            logger.error(f"Task '{callback.task_name}' failed.\nHeaders: {properties.headers}.\nBody: {body}")
            event = TaskFailed(task_name=callback.task_name, error_type=type(e).__name__, error_message=str(e))
            publish_integration_event(event)

        return None

    return wrapper
