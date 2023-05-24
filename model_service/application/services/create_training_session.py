from model_service.application.commands.create_training_session import CreateTrainingSession
from model_service.application.integration_events.core.publishers import publish_integration_event
from model_service.application.integration_events.training_session_created import TrainingSessionCreated
from model_service.application.schema_mappers.map_training_session_from_schema import map_training_session_from_schema
from model_service.dependencies.dependency_management.provide import Dependency, provide
from model_service.domain.repositories.abstract_training_session_repository import AbstractTrainingSessionRepository
from model_service.utility.logging.log_function_execution import log_function_execution


@log_function_execution()
@provide
def create_training_session(
    command: CreateTrainingSession,
    repository: AbstractTrainingSessionRepository = Dependency(),
) -> None:
    training_session = map_training_session_from_schema(command.training_session)
    persisted_training_session = repository.save(training_session)
    event = TrainingSessionCreated(training_session_id=persisted_training_session.id)
    publish_integration_event(event)
