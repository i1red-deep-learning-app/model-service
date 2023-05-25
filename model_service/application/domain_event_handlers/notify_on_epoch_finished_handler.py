from model_service.application.integration_events.core.publishers import publish_integration_event
from model_service.application.integration_events.training_epoch_finished import TrainingEpochFinished
from model_service.domain.events.epoch_finished import EpochFinished
from model_service.shared.logging.log_function_execution import log_function_execution


@log_function_execution()
def notify_on_epoch_finished_handler(event: EpochFinished) -> None:
    integration_event = TrainingEpochFinished(training_session_id=event.training_session_id, epoch=event.epoch)
    publish_integration_event(integration_event)
