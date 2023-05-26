from bson import ObjectId

from model_service.domain.entities.neural_network.feed_forward_network import FeedForwardNetwork
from model_service.domain.repositories.abstract_feed_forward_network_repository import (
    AbstractFeedForwardNetworkRepository,
)
from model_service.infrastructure.mongo.mappers.abstract_mongo_mapper import AbstractMongoMapper
from model_service.infrastructure.mongo.models.neural_network.feed_forward_network import FeedForwardNetworkModel


class MongoFeedForwardNetworkRepository(AbstractFeedForwardNetworkRepository):
    def __init__(self, mapper: AbstractMongoMapper[FeedForwardNetwork, FeedForwardNetworkModel]) -> None:
        self._mapper = mapper

    def save(self, feed_forward_network: FeedForwardNetwork) -> FeedForwardNetwork:
        feed_forward_network_model = self._mapper.entity_to_model(feed_forward_network)
        feed_forward_network_model = feed_forward_network_model.save()

        return self._mapper.model_to_entity(feed_forward_network_model)

    def get_by_id(self, feed_forward_network_id: str) -> FeedForwardNetwork | None:
        feed_forward_network_model = FeedForwardNetworkModel.objects(id=ObjectId(feed_forward_network_id)).first()

        if feed_forward_network_model is None:
            return None

        return self._mapper.model_to_entity(feed_forward_network_model)

    def get_user_networks(self, user: str) -> list[FeedForwardNetwork]:
        feed_forward_network_model_iterable = FeedForwardNetworkModel.objects(user=user)
        return list(map(self._mapper.model_to_entity, feed_forward_network_model_iterable))
