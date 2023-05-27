from uuid import UUID

from model_service.domain.entities.neural_network.feed_forward_network import FeedForwardNetwork
from model_service.domain.repositories.abstract_feed_forward_network_repository import (
    AbstractFeedForwardNetworkRepository,
)
from model_service.infrastructure.mongo.mappers.abstract_mongo_mapper import AbstractMongoMapper
from model_service.infrastructure.mongo.documents.neural_network.feed_forward_network_document import (
    FeedForwardNetworkDocument,
)


class MongoFeedForwardNetworkRepository(AbstractFeedForwardNetworkRepository):
    def __init__(self, mapper: AbstractMongoMapper[FeedForwardNetwork, FeedForwardNetworkDocument]) -> None:
        self._mapper = mapper

    def save(self, feed_forward_network: FeedForwardNetwork) -> FeedForwardNetwork:
        feed_forward_network_document = self._mapper.entity_to_document(feed_forward_network)
        feed_forward_network_document = feed_forward_network_document.save()

        return self._mapper.document_to_entity(feed_forward_network_document)

    def get_by_id(self, feed_forward_network_id: UUID) -> FeedForwardNetwork | None:
        feed_forward_network_document = FeedForwardNetworkDocument.objects(id=feed_forward_network_id).first()

        if feed_forward_network_document is None:
            return None

        return self._mapper.document_to_entity(feed_forward_network_document)

    def get_user_networks(self, user: str) -> list[FeedForwardNetwork]:
        feed_forward_network_document_iterable = FeedForwardNetworkDocument.objects(user=user)
        return list(map(self._mapper.document_to_entity, feed_forward_network_document_iterable))
