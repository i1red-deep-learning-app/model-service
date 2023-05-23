import functools
from collections.abc import Callable
from typing import TypeVar

from model_service.application.integration_events.publishers import publish_integration_event
from model_service.application.integration_events.task_failed import TaskFailed

TCallback = TypeVar("TCallback", bound=Callable)


def handle_command_callback_errors(task_name: str) -> Callable[[TCallback], TCallback]:
    def decorator(callback: TCallback) -> TCallback:
        @functools.wraps(callback)
        def wrapper(*args, **kwargs):
            try:
                return callback(*args, **kwargs)
            except Exception as e:
                event = TaskFailed(task_name=task_name, error_type=type(e).__name__, error_message=str(e))
                publish_integration_event(event)

        return wrapper

    return decorator
