from model_service.application.domain_event_handlers.notify_on_epoch_finished_handler import (
    notify_on_epoch_finished_handler,
)
from model_service.application.domain_event_handlers.save_result_on_epoch_finished_handler import (
    SaveResultOnEpochFinishedHandler,
)
from model_service.domain.events.core.handlers import register_domain_event_handler
from model_service.domain.events.epoch_finished import EpochFinished


def setup_domain_event_handlers() -> None:
    register_domain_event_handler(EpochFinished, SaveResultOnEpochFinishedHandler())
    register_domain_event_handler(EpochFinished, notify_on_epoch_finished_handler)
