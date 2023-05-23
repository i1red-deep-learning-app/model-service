from collections.abc import Callable
from typing import Final, TypeVar, Type

from model_service.application.integration_events.integration_event import IntegrationEvent

TIntegrationEvent = TypeVar("TIntegrationEvent", bound=IntegrationEvent)


_INTEGRATION_EVENT_PUBLISHERS: Final[dict[Type[TIntegrationEvent], Callable[[TIntegrationEvent], None]]] = {}


def register_integration_event_publisher(
    event_type: Type[TIntegrationEvent], publisher: Callable[[TIntegrationEvent], None]
) -> None:
    if event_type in _INTEGRATION_EVENT_PUBLISHERS:
        raise ValueError(f"Event publisher for {event_type.__name__} has already been registered")

    _INTEGRATION_EVENT_PUBLISHERS[event_type] = publisher


def unregister_integration_event_publisher(
    event_type: Type[TIntegrationEvent], publisher: Callable[[TIntegrationEvent], None]
) -> None:
    if publisher != _INTEGRATION_EVENT_PUBLISHERS.get(event_type):
        raise ValueError(f"Provided event publisher for {event_type.__name__} has not been registered")

    del _INTEGRATION_EVENT_PUBLISHERS[event_type]


def publish_integration_event(event: IntegrationEvent) -> None:
    publisher = _INTEGRATION_EVENT_PUBLISHERS[type(event)]
    publisher(event)
