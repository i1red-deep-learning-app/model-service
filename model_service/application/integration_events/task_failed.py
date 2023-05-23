import attrs


@attrs.define
class TaskFailed:
    task_name: str
    error_type: str
    error_message: str
