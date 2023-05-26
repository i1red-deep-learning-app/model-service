from bson import ObjectId

from model_service.domain.entities.core.generated import GENERATED_VALUE
from model_service.domain.entities.neural_network.feed_forward_network import FeedForwardNetwork
from model_service.domain.entities.value_objects.linear_layer import LinearLayer
from model_service.infrastructure.mongo.mappers.abstract_mongo_mapper import AbstractMongoMapper
from model_service.infrastructure.mongo.models.neural_network.activation_function import ActivationFunctionModel
from model_service.infrastructure.mongo.models.neural_network.feed_forward_network import FeedForwardNetworkModel
from model_service.infrastructure.mongo.models.neural_network.linear_layer import LinearLayerModel


class FeedForwardNetworkMongoMapper(AbstractMongoMapper[FeedForwardNetwork, FeedForwardNetworkModel]):
    def entity_to_model(self, entity: FeedForwardNetwork) -> FeedForwardNetworkModel:
        layers = [
            LinearLayerModel(
                size=layer.size,
                activation=ActivationFunctionModel(type=layer.activation.type, params=layer.activation.params),
            )
            for layer in entity.layers
        ]
        model = FeedForwardNetworkModel(
            user=entity.user,
            input_size=entity.input_size,
            layers=layers,
        )
        if entity.id is not GENERATED_VALUE:
            model.id = ObjectId(entity.id)

        return model

    def model_to_entity(self, model: FeedForwardNetworkModel) -> FeedForwardNetwork:
        layers = [
            LinearLayer(
                size=layer_model.size,
                activation=ActivationFunctionModel(
                    type=layer_model.activation.type, params=layer_model.activation.params
                ),
            )
            for layer_model in model.layers
        ]
        entity = FeedForwardNetwork(
            id=str(model.id),
            user=model.user,
            input_size=model.input_size,
            layers=layers,
        )
        return entity
