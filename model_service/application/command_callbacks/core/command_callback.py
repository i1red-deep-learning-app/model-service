import functools
import logging
from collections.abc import Callable
from typing import Protocol

from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties


PikaCallback = Callable[[BlockingChannel, Basic.Deliver, BasicProperties, bytes], None]


class CommandCallback(Protocol):
    task_name: str
    """Human readable task name"""

    def __call__(
        self,
        channel: BlockingChannel,
        method: Basic.Deliver,
        properties: BasicProperties,
        body: bytes,
    ) -> None:
        """Callback method"""


def command_callback(*, task_name: str, log_level: int = logging.INFO) -> Callable[[PikaCallback], CommandCallback]:
    def decorator(callback: PikaCallback) -> CommandCallback:
        logger = logging.getLogger(callback.__module__)

        @functools.wraps(callback)
        def wrapper(
            channel: BlockingChannel,
            method: Basic.Deliver,
            properties: BasicProperties,
            body: bytes,
        ) -> None:
            logger.log(log_level, f"Execute '{task_name}' task")
            return callback(channel, method, properties, body)

        wrapper.task_name = task_name
        return wrapper

    return decorator
