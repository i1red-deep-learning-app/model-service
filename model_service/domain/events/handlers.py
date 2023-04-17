from collections.abc import Callable
from typing import Final, TypeVar, Type

TEvent = TypeVar("TEvent")
THandler = TypeVar("THandler", bound=Callable)


_DOMAIN_EVENT_HANDLERS: Final[dict[Type[TEvent], list[Callable[[TEvent], None]]]] = {}


def domain_event_handler(event_type: Type[TEvent]) -> Callable[[Callable[[TEvent], None]], Callable[[TEvent], None]]:
    def decorator(handler: Callable[[TEvent], None]) -> Callable[[TEvent], None]:
        register_event_handler(event_type, handler)
        return handler

    return decorator


def register_event_handler(event_type: Type[TEvent], handler: Callable[[TEvent], None]) -> None:
    event_handlers_list = _DOMAIN_EVENT_HANDLERS.setdefault(event_type, [])
    event_handlers_list.append(handler)


def unregister_event_handler(event_type: Type[TEvent], handler: Callable[[TEvent], None]) -> None:
    if event_type not in _DOMAIN_EVENT_HANDLERS:
        raise ValueError(f"{event_type.__name__} does not have registered handlers")

    try:
        _DOMAIN_EVENT_HANDLERS[event_type].remove(handler)
    except ValueError:
        raise ValueError("Provided handler is not registered")


def publish_domain_event(event: TEvent) -> None:
    for handler in _DOMAIN_EVENT_HANDLERS[type(event)]:
        handler(event)
