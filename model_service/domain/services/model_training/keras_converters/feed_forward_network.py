from tensorflow.python import keras
from tensorflow.python.keras import layers

from model_service.domain.entities.neural_network.feed_forward_network import FeedForwardNetwork
from model_service.domain.services.model_training.keras_converters.activation_function import (
    create_keras_activation_function,
)


def create_keras_feed_forward_network(
    feed_forward_network: FeedForwardNetwork, input_size: int, number_of_classes: int
) -> keras.Model:
    model = keras.Sequential()

    model.add(layers.InputLayer(input_shape=(input_size,)))

    for layer in feed_forward_network.layers:
        model.add(layers.Dense(layer.size))
        model.add(create_keras_activation_function(layer.activation))

    if number_of_classes == 2:
        model.add(layers.Dense(1))
        model.add(layers.Activation("sigmoid"))
    else:
        model.add(layers.Dense(number_of_classes))
        model.add(layers.Activation("softmax"))

    return model
