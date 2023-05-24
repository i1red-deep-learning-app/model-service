import logging
from collections.abc import Callable
from typing import Final, TypeVar, Type

from model_service.domain.events.core.domain_event import DomainEvent

logger = logging.getLogger(__name__)

TDomainEvent = TypeVar("TDomainEvent", bound=DomainEvent)


_DOMAIN_EVENT_HANDLERS: Final[dict[Type[TDomainEvent], list[Callable[[TDomainEvent], None]]]] = {}


def register_domain_event_handler(event_type: Type[TDomainEvent], handler: Callable[[TDomainEvent], None]) -> None:
    event_handlers_list = _DOMAIN_EVENT_HANDLERS.setdefault(event_type, [])
    event_handlers_list.append(handler)


def unregister_domain_event_handler(event_type: Type[TDomainEvent], handler: Callable[[TDomainEvent], None]) -> None:
    if event_type not in _DOMAIN_EVENT_HANDLERS:
        raise ValueError(f"{event_type.__name__} does not have registered handlers")

    try:
        _DOMAIN_EVENT_HANDLERS[event_type].remove(handler)
    except ValueError:
        raise ValueError("Provided handler is not registered")


def publish_domain_event(event: DomainEvent) -> None:
    logger.info(f"Publish {type(event).__name__} domain event")
    for handler in _DOMAIN_EVENT_HANDLERS[type(event)]:
        handler(event)
