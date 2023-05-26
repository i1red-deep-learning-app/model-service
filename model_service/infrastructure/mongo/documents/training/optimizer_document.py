from mongoengine import EmbeddedDocument, DictField, EnumField

from model_service.domain.entities.value_objects.optimizer import OptimizerType


class OptimizerDocument(EmbeddedDocument):
    type: OptimizerType = EnumField(OptimizerType)
    params: dict = DictField()
