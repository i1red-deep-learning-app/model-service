from collections.abc import Callable
from typing import Final, TypeVar, Type

TEvent = TypeVar("TEvent")
THandler = TypeVar("THandler", bound=Callable)


_DOMAIN_EVENT_HANDLERS: Final[dict[Type[TEvent], list[Callable[[TEvent], None]]]] = {}


def domain_event_handler(event_type: Type[TEvent]) -> Callable[[Callable[[TEvent], None]], Callable[[TEvent], None]]:
    def register_handler(handler: Callable[[TEvent], None]) -> Callable[[TEvent], None]:
        event_handlers_list = _DOMAIN_EVENT_HANDLERS.setdefault(event_type, [])
        event_handlers_list.append(handler)

        return handler

    return register_handler


def publish_domain_event(event: TEvent) -> None:
    for handler in _DOMAIN_EVENT_HANDLERS[type(event)]:
        handler(event)
