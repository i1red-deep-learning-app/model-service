from enum import Enum

import attrs


class ActivationFunctionType(Enum):
    RELU = "relu"
    TANH = ("tanh",)
    LEAKY_RELU = "leaky_relu"
    PRELU = "prelu"
    SIGMOID = "sigmoid"
    SOFTMAX = "softmax"


@attrs.define
class ActivationFunction:
    type: ActivationFunctionType = attrs.field()
    params: dict = attrs.field()
