from bson import ObjectId
from mongoengine import Document, IntField, EmbeddedDocumentListField, StringField, ObjectIdField

from model_service.infrastructure.mongo.models.neural_network.linear_layer import LinearLayerModel


class FeedForwardNetworkModel(Document):
    id: ObjectId = ObjectIdField(db_field="_id", primary_key=True, default=ObjectId)
    user: str = StringField()
    input_size: int = IntField()
    layers: list[LinearLayerModel] = EmbeddedDocumentListField(LinearLayerModel)
