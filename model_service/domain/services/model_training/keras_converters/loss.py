from tensorflow.python.keras import losses

from model_service.domain.entities.training.loss_function_type import LossFunctionType


def create_loss(loss: LossFunctionType) -> losses.Loss:
    match loss:
        case LossFunctionType.BINARY_CROSSENTROPY:
            return losses.BinaryCrossentropy()
        case LossFunctionType.SPARSE_CATEGORICAL_CROSSENTROPY:
            return losses.SparseCategoricalCrossentropy()
        case _:
            raise NotImplementedError("Loss function is not supported")
