from mongoengine import EmbeddedDocument, DictField, EnumField

from model_service.domain.entities.value_objects.activation_function import ActivationFunctionType


class ActivationFunctionDocument(EmbeddedDocument):
    type: ActivationFunctionType = EnumField(ActivationFunctionType)
    params: dict = DictField()
