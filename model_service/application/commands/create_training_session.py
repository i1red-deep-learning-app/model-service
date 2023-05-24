from model_service.application.commands.core.command import Command
from model_service.application.schemas.training_session_schema import TrainingSessionSchema


class CreateTrainingSession(Command):
    training_session: TrainingSessionSchema
