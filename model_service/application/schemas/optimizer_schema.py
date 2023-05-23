from typing import Literal

from pydantic import BaseModel


class OptimizerSchema(BaseModel):
    type: Literal["adam"]
    params: dict
