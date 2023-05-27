from uuid import UUID

from mongoengine import Document, EmbeddedDocumentListField, StringField, UUIDField

from model_service.infrastructure.mongo.documents.neural_network.linear_layer_document import LinearLayerDocument


class FeedForwardNetworkDocument(Document):
    id: UUID = UUIDField(db_field="_id", primary_key=True)
    user: str = StringField()
    layers: list[LinearLayerDocument] = EmbeddedDocumentListField(LinearLayerDocument)
