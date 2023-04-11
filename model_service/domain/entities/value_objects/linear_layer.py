import attrs

from model_service.domain.entities.value_objects.activation_function import ActivationFunction


@attrs.define
class LinearLayer:
    size: int = attrs.field()
    activation: ActivationFunction = attrs.field()
