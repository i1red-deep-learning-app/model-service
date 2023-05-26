from mongoengine import EmbeddedDocument, EmbeddedDocumentField, IntField

from model_service.infrastructure.mongo.documents.neural_network.activation_function_document import (
    ActivationFunctionDocument,
)


class LinearLayerDocument(EmbeddedDocument):
    size: int = IntField()
    activation: ActivationFunctionDocument = EmbeddedDocumentField(ActivationFunctionDocument)
