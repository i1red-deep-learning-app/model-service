from uuid import UUID

import attrs

from model_service.domain.entities.neural_network.feed_forward_network import FeedForwardNetwork
from model_service.domain.repositories.abstract_feed_forward_network_repository import (
    AbstractFeedForwardNetworkRepository,
)


class FakeFeedForwardNetworkRepository(AbstractFeedForwardNetworkRepository):
    _feed_forward_networks: dict[UUID, FeedForwardNetwork]

    def __init__(self) -> None:
        self._feed_forward_networks = {}

    def save(self, feed_forward_network: FeedForwardNetwork) -> FeedForwardNetwork:
        persisted_feed_forward_network = attrs.evolve(feed_forward_network)
        self._feed_forward_networks[persisted_feed_forward_network.id] = persisted_feed_forward_network

        return persisted_feed_forward_network

    def get_by_id(self, feed_forward_network_id: UUID) -> FeedForwardNetwork | None:
        return self._feed_forward_networks.get(feed_forward_network_id)

    def get_user_networks(self, user: str) -> list[FeedForwardNetwork]:
        return [
            feed_forward_network
            for feed_forward_network in self._feed_forward_networks.values()
            if feed_forward_network.user == user
        ]
