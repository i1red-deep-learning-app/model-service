from mongoengine import EmbeddedDocument, DictField, EnumField

from model_service.domain.entities.value_objects.activation_function import ActivationFunctionType


class ActivationFunctionModel(EmbeddedDocument):
    type: ActivationFunctionType = EnumField(ActivationFunctionType)
    params: dict = DictField()
