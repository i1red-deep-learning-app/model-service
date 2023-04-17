from mongoengine import EmbeddedDocument, EmbeddedDocumentField, IntField

from model_service.infrastructure.mongo.models.neural_network.activation_function import ActivationFunctionModel


class LinearLayerModel(EmbeddedDocument):
    size: int = IntField()
    activation: ActivationFunctionModel = EmbeddedDocumentField(ActivationFunctionModel)
