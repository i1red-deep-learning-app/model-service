from uuid import UUID

from mongoengine import (
    Document,
    StringField,
    FloatField,
    IntField,
    ListField,
    EnumField,
    EmbeddedDocumentField, UUIDField,
)

from model_service.domain.entities.training.loss_function_type import LossFunctionType
from model_service.domain.entities.training.metric_type import MetricType
from model_service.infrastructure.mongo.documents.training.optimizer_document import OptimizerDocument


class TrainingSessionDocument(Document):
    id: UUID = UUIDField(db_field="_id", primary_key=True)
    user: str = StringField()
    network_id: UUID = UUIDField()
    dataset_id: UUID = UUIDField()
    optimizer: OptimizerDocument = EmbeddedDocumentField(OptimizerDocument)
    loss_function: LossFunctionType = EnumField(LossFunctionType)
    metrics: list[MetricType] = ListField(EnumField(MetricType))
    epochs: int = IntField()
    batch_size: int = IntField()
    validation_split: float = FloatField()
