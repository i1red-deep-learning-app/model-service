from pydantic import BaseModel


class StartFfnTraining(BaseModel):
    training_session_id: str
