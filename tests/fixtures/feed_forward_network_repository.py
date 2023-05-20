import pytest

from model_service.domain.entities.neural_network.feed_forward_network import FeedForwardNetwork
from model_service.domain.repositories.abstract_feed_forward_network_repository import (
    AbstractFeedForwardNetworkRepository,
)
from model_service.infrastructure.fake.repositories.fake_feed_forward_network_repository import (
    FakeFeedForwardNetworkRepository,
)


@pytest.fixture
def feed_forward_network_repository(feed_forward_network: FeedForwardNetwork) -> AbstractFeedForwardNetworkRepository:
    repository = FakeFeedForwardNetworkRepository()
    repository.save(feed_forward_network)
    return repository
