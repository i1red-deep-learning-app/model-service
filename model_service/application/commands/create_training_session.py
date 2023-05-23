from pydantic import BaseModel

from model_service.application.schemas.training_session_schema import TrainingSessionSchema


class CreateTrainingSession(BaseModel):
    training_session: TrainingSessionSchema
