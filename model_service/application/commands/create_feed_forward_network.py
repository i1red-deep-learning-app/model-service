from pydantic import BaseModel

from model_service.application.schemas.feed_forward_network_schema import FeedForwardNetworkSchema


class CreateFeedForwardNetwork(BaseModel):
    feed_forward_network: FeedForwardNetworkSchema
