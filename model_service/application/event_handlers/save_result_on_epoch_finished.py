import uuid

from model_service.dependencies.dependency_management.provide import Dependency
from model_service.domain.data_storage.abstract_data_storage import AbstractDataStorage
from model_service.domain.events.epoch_finished import EpochFinished
from model_service.domain.events.handlers import domain_event_handler
from model_service.domain.entities.training.training_result import TrainingResult
from model_service.domain.repositories.abstract_training_result_repository import AbstractTrainingResultRepository


@domain_event_handler(EpochFinished)
def save_result_on_epoch_finished(
    event: EpochFinished,
    training_result_repository: AbstractTrainingResultRepository = Dependency(),
    data_storage: AbstractDataStorage = Dependency(),
) -> None:
    training_result = training_result_repository.get_by_training_session_id(event.training_session_id)

    if training_result is not None and training_result.validation_loss < event.validation_loss:
        return

    weights_file_key = uuid.uuid4().hex
    weights_file_content = event.weights
    data_storage.save_file(weights_file_key, weights_file_content)

    new_training_result = TrainingResult.create(
        user=event.user,
        training_session_id=event.training_session_id,
        loss=event.loss,
        validation_loss=event.validation_loss,
        metrics=event.metrics,
        weights_file_key=weights_file_key,
    )

    training_result_repository.save(new_training_result)

    if training_result is not None:
        training_result_repository.delete_by_id(training_result.id)
