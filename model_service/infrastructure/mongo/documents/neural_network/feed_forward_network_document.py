from bson import ObjectId
from mongoengine import Document, IntField, EmbeddedDocumentListField, StringField, ObjectIdField

from model_service.infrastructure.mongo.documents.neural_network.linear_layer_document import LinearLayerDocument


class FeedForwardNetworkDocument(Document):
    id: ObjectId = ObjectIdField(db_field="_id", primary_key=True, default=ObjectId)
    user: str = StringField()
    layers: list[LinearLayerDocument] = EmbeddedDocumentListField(LinearLayerDocument)
