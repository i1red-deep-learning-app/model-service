import attrs

from model_service.application.integration_events.core.integration_event import IntegrationEvent


@attrs.define
class FeedForwardNetworkCreated(IntegrationEvent):
    feed_forward_network_id: str
