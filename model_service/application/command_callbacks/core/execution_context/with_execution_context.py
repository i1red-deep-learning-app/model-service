import functools
import logging

from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties

from model_service.application.command_callbacks.core.command_callback import CommandCallback
from model_service.application.command_callbacks.core.execution_context.create_execution_context import (
    create_execution_context,
)
from model_service.application.command_callbacks.core.execution_context.exceptions import ExecutionContextCreationError
from model_service.application.shared.execution_context import ExecutionContext
from model_service.shared.dependency_management.provider_getters import get_scoped_provider
from model_service.shared.dependency_management.providers.scoped_dependency_provider import ScopedDependencies


def with_execution_context(callback: CommandCallback) -> CommandCallback:
    logger = logging.getLogger(callback.__module__)

    @functools.wraps(callback)
    def wrapper(
        channel: BlockingChannel,
        method: Basic.Deliver,
        properties: BasicProperties,
        body: bytes,
    ) -> None:
        try:
            execution_context = create_execution_context(properties)
        except ExecutionContextCreationError as e:
            logger.exception(e)
            logger.error(f"Task '{callback.task_name}' failed.\nHeaders: {properties.headers}.\nBody: {body}")
            channel.basic_nack(method.delivery_tag, requeue=False)
            return

        with ScopedDependencies(get_scoped_provider()) as dependencies:
            dependencies.set(ExecutionContext, execution_context)
            return callback(channel, method, properties, body)

    return wrapper
