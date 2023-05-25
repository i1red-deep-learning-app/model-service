from pydantic import BaseModel

from model_service.application.schemas.linear_layer_schema import LinearLayerSchema


class FeedForwardNetworkSchema(BaseModel):
    layers: list[LinearLayerSchema]
