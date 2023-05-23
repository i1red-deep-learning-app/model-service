import functools

from model_service.application.command_callbacks.command_callback import CommandCallback
from model_service.application.integration_events.publishers import publish_integration_event
from model_service.application.integration_events.task_failed import TaskFailed


def handle_command_callback_errors(callback: CommandCallback) -> CommandCallback:
    @functools.wraps(callback)
    def wrapper(*args, **kwargs):
        try:
            return callback(*args, **kwargs)
        except Exception as e:
            event = TaskFailed(task_name=callback.task_name, error_type=type(e).__name__, error_message=str(e))
            publish_integration_event(event)

    return wrapper
