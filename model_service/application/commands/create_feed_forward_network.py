from model_service.application.commands.core.command import Command
from model_service.application.schemas.feed_forward_network_schema import FeedForwardNetworkSchema


class CreateFeedForwardNetwork(Command):
    feed_forward_network: FeedForwardNetworkSchema
