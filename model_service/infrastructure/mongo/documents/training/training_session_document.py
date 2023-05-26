from bson import ObjectId
from mongoengine import (
    Document,
    ObjectIdField,
    StringField,
    FloatField,
    IntField,
    ListField,
    EnumField,
    EmbeddedDocumentField,
)

from model_service.domain.entities.training.loss_function_type import LossFunctionType
from model_service.domain.entities.training.metric_type import MetricType
from model_service.infrastructure.mongo.documents.training.optimizer_document import OptimizerDocument


class TrainingSessionDocument(Document):
    id: ObjectId = ObjectIdField(db_field="_id", primary_key=True, default=ObjectId)
    user: str = StringField()
    network_id: ObjectId = ObjectIdField()
    dataset_id: ObjectId = ObjectIdField()
    optimizer: OptimizerDocument = EmbeddedDocumentField(OptimizerDocument)
    loss_function: LossFunctionType = EnumField(LossFunctionType)
    metrics: list[MetricType] = ListField(EnumField(MetricType))
    epochs: int = IntField()
    batch_size: int = IntField()
    validation_split: float = FloatField()
