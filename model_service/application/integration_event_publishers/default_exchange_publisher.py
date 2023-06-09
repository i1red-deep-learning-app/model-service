import json
from typing import Generic, TypeVar

import attrs
from pika import BasicProperties
from pika.adapters.blocking_connection import BlockingChannel

from model_service.application.integration_events.core.integration_event import IntegrationEvent
from model_service.application.shared.execution_context import ExecutionContext
from model_service.shared.json.custom_json_encoder import CustomJSONEncoder

TIntegrationEvent = TypeVar("TIntegrationEvent", bound=IntegrationEvent)


class DefaultExchangePublisher(Generic[TIntegrationEvent]):
    def __init__(self, channel: BlockingChannel, queue: str) -> None:
        self._channel = channel
        self._queue = queue
        self._setup_publisher()

    def _setup_publisher(self) -> None:
        self._channel.queue_declare(queue=self._queue)

    def __call__(self, event: TIntegrationEvent, execution_context: ExecutionContext) -> None:
        body = json.dumps(attrs.asdict(event), cls=CustomJSONEncoder).encode()
        self._channel.basic_publish(
            exchange="",
            routing_key=self._queue,
            body=body,
            properties=BasicProperties(headers={"user": execution_context.user}),
        )
