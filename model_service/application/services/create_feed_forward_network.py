from model_service.application.commands.create_feed_forward_network import CreateFeedForwardNetwork
from model_service.application.integration_events.feed_forward_network_created import FeedForwardNetworkCreated
from model_service.application.integration_events.publishers import publish_integration_event
from model_service.application.schema_mappers.map_feed_forward_network_from_schema import (
    map_feed_forward_network_from_schema,
)
from model_service.dependencies.dependency_management.provide import Dependency, provide
from model_service.domain.repositories.abstract_feed_forward_network_repository import (
    AbstractFeedForwardNetworkRepository,
)


@provide
def create_feed_forward_network(
    command: CreateFeedForwardNetwork,
    repository: AbstractFeedForwardNetworkRepository = Dependency(),
) -> None:
    feed_forward_network = map_feed_forward_network_from_schema(command.feed_forward_network)
    persisted_feed_forward_network = repository.save(feed_forward_network)
    event = FeedForwardNetworkCreated(feed_forward_network=persisted_feed_forward_network.id)
    publish_integration_event(event)
