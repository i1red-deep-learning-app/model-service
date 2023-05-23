from typing import Literal

from pydantic import BaseModel


class ActivationFunctionSchema(BaseModel):
    type: Literal["relu", "tanh", "leaky_relu", "prelu", "sigmoid", "softmax"]
    params: dict
