from abc import ABC, abstractmethod
from uuid import UUID

from model_service.domain.entities.neural_network.feed_forward_network import FeedForwardNetwork


class AbstractFeedForwardNetworkRepository(ABC):
    @abstractmethod
    def save(self, feed_forward_network: FeedForwardNetwork) -> FeedForwardNetwork:
        """Save feed forward network info to database"""

    @abstractmethod
    def get_by_id(self, feed_forward_network_id: UUID) -> FeedForwardNetwork | None:
        """Get feed forward network info by id"""

    @abstractmethod
    def get_user_networks(self, user: str) -> list[FeedForwardNetwork]:
        """Get list of user's feed forward networks"""
