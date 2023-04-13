from tensorflow.python.keras import optimizers

from model_service.domain.entities.value_objects.optimizer import Optimizer, OptimizerType


def create_keras_optimizer(optimizer: Optimizer) -> optimizers.optimizer_v2.OptimizerV2:
    match optimizer.type:
        case OptimizerType.ADAM:
            return optimizers.adam_v2.Adam(**optimizer.params)
        case _:
            raise NotImplementedError("Optimizer is not supported")
