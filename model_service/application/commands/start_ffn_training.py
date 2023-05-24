from model_service.application.commands.core.command import Command


class StartFfnTraining(Command):
    training_session_id: str
