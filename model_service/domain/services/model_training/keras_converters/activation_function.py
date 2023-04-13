from tensorflow.python.keras import layers

from model_service.domain.entities.value_objects.activation_function import ActivationFunction, ActivationFunctionType


def create_keras_activation_function(activation_function: ActivationFunction) -> layers.Layer:
    match activation_function.type:
        case (
            ActivationFunctionType.RELU
            | ActivationFunctionType.TANH
            | ActivationFunctionType.SIGMOID
            | ActivationFunctionType.SOFTMAX
        ):
            return layers.Activation(activation_function.type.value)
        case ActivationFunctionType.LEAKY_RELU:
            return layers.LeakyReLU(**activation_function.params)
        case ActivationFunctionType.PRELU:
            return layers.PReLU(**activation_function.params)
        case _:
            raise NotImplementedError("Activation function is not supported")
