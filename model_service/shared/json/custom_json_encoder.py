from json import JSONEncoder
from typing import Any
from uuid import UUID


class CustomJSONEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, UUID):
            return str(o)
        return super().default(o)
