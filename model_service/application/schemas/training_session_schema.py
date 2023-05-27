from typing import Literal

from pydantic import BaseModel, UUID4

from model_service.application.schemas.optimizer_schema import OptimizerSchema


class TrainingSessionSchema(BaseModel):
    network_id: UUID4
    dataset_id: UUID4
    optimizer: OptimizerSchema
    loss_function: Literal["binary_cross_entropy", "categorical_cross_entropy"]
    metrics: list[Literal["accuracy", "sparse_categorical_accuracy"]]
    epochs: int
    batch_size: int
    validation_split: float
