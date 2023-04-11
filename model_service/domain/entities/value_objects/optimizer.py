from enum import Enum

import attrs


class OptimizerType(Enum):
    ADAM = "adam"


@attrs.define
class Optimizer:
    type: OptimizerType = attrs.field()
    params: dict = attrs.field()
