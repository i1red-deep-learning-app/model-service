from model_service.application.schemas.feed_forward_network_schema import FeedForwardNetworkSchema
from model_service.domain.entities.neural_network.feed_forward_network import FeedForwardNetwork
from model_service.domain.entities.value_objects.activation_function import ActivationFunction, ActivationFunctionType
from model_service.domain.entities.value_objects.linear_layer import LinearLayer


def map_feed_forward_network_from_schema(schema: FeedForwardNetworkSchema) -> FeedForwardNetwork:
    layers = [
        LinearLayer(
            size=layer_schema.size,
            activation=ActivationFunction(
                type=ActivationFunctionType(layer_schema.activation.type), params=layer_schema.activation.params
            ),
        )
        for layer_schema in schema.layers
    ]
    return FeedForwardNetwork.create(user=schema.user, layers=layers)
