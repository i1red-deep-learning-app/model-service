import logging
from collections.abc import Callable
from typing import Final, TypeVar, Type

from model_service.application.integration_events.core.integration_event import IntegrationEvent
from model_service.domain.shared.execution_context import ExecutionContext
from model_service.shared.dependency_management.dependency_kind import SCOPED
from model_service.shared.dependency_management.provide import Dependency, provide

logger = logging.getLogger(__name__)

TIntegrationEvent = TypeVar("TIntegrationEvent", bound=IntegrationEvent)


_INTEGRATION_EVENT_PUBLISHERS: Final[
    dict[Type[TIntegrationEvent], Callable[[TIntegrationEvent, ExecutionContext], None]]
] = {}


def register_integration_event_publisher(
    event_type: Type[TIntegrationEvent], publisher: Callable[[TIntegrationEvent, ExecutionContext], None]
) -> None:
    if event_type in _INTEGRATION_EVENT_PUBLISHERS:
        raise ValueError(f"Event publisher for {event_type.__name__} has already been registered")

    _INTEGRATION_EVENT_PUBLISHERS[event_type] = publisher


def unregister_integration_event_publisher(
    event_type: Type[TIntegrationEvent], publisher: Callable[[TIntegrationEvent, ExecutionContext], None]
) -> None:
    if publisher != _INTEGRATION_EVENT_PUBLISHERS.get(event_type):
        raise ValueError(f"Provided event publisher for {event_type.__name__} has not been registered")

    del _INTEGRATION_EVENT_PUBLISHERS[event_type]


@provide
def publish_integration_event(
    event: IntegrationEvent, execution_context: ExecutionContext = Dependency(SCOPED)
) -> None:
    logger.info(f"Publish {type(event).__name__} integration event")
    publisher = _INTEGRATION_EVENT_PUBLISHERS[type(event)]
    publisher(event, execution_context)
