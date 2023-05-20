import pytest

from model_service.domain.entities.neural_network.feed_forward_network import FeedForwardNetwork
from model_service.domain.entities.value_objects.activation_function import ActivationFunction, ActivationFunctionType
from model_service.domain.entities.value_objects.linear_layer import LinearLayer


@pytest.fixture
def feed_forward_network(feed_forward_network_id: int, user: str) -> FeedForwardNetwork:
    layers = [LinearLayer(size=128, activation=ActivationFunction(type=ActivationFunctionType.PRELU, params={}))]
    return FeedForwardNetwork(id=feed_forward_network_id, user=user, layers=layers)
