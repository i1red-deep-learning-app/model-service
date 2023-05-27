from model_service.domain.entities.neural_network.feed_forward_network import FeedForwardNetwork
from model_service.domain.entities.value_objects.linear_layer import LinearLayer
from model_service.infrastructure.mongo.mappers.abstract_mongo_mapper import AbstractMongoMapper
from model_service.infrastructure.mongo.documents.neural_network.activation_function_document import (
    ActivationFunctionDocument,
)
from model_service.infrastructure.mongo.documents.neural_network.feed_forward_network_document import (
    FeedForwardNetworkDocument,
)
from model_service.infrastructure.mongo.documents.neural_network.linear_layer_document import LinearLayerDocument


class FeedForwardNetworkMongoMapper(AbstractMongoMapper[FeedForwardNetwork, FeedForwardNetworkDocument]):
    def entity_to_document(self, entity: FeedForwardNetwork) -> FeedForwardNetworkDocument:
        layers = [
            LinearLayerDocument(
                size=layer.size,
                activation=ActivationFunctionDocument(type=layer.activation.type, params=layer.activation.params),
            )
            for layer in entity.layers
        ]
        document = FeedForwardNetworkDocument(id=entity.id, user=entity.user, layers=layers)

        return document

    def document_to_entity(self, document: FeedForwardNetworkDocument) -> FeedForwardNetwork:
        layers = [
            LinearLayer(
                size=layer_document.size,
                activation=ActivationFunctionDocument(
                    type=layer_document.activation.type, params=layer_document.activation.params
                ),
            )
            for layer_document in document.layers
        ]
        entity = FeedForwardNetwork(id=document.id, user=document.user, layers=layers)

        return entity
