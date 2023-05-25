import attrs


@attrs.define
class ExecutionContext:
    user: str = attrs.field()
    metadata: dict = attrs.field()
