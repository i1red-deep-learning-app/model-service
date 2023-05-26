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
from model_service.infrastructure.mongo.models.training.optimizer_model import OptimizerModel


class TrainingSessionModel(Document):
    id: ObjectId = ObjectIdField(db_field="_id", primary_key=True, default=ObjectId)
    user: str = StringField()
    network_id: ObjectId = ObjectIdField()
    dataset_id: ObjectId = ObjectIdField()
    optimizer: OptimizerModel = EmbeddedDocumentField(OptimizerModel)
    loss_function: LossFunctionType = EnumField(LossFunctionType)
    metrics: list[MetricType] = ListField(EnumField(MetricType))
    epochs: int = IntField()
    batch_size: int = IntField()
    validation_split: float = FloatField()
