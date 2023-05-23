from pydantic import BaseModel

from model_service.application.schemas.activation_function_schema import ActivationFunctionSchema


class LinearLayerSchema(BaseModel):
    size: int
    activation: ActivationFunctionSchema
