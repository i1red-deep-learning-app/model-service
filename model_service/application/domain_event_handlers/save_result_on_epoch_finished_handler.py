import pickle
import uuid

from model_service.shared.dependency_management.provide import Dependency, provide
from model_service.domain.data_storage.abstract_data_storage import AbstractDataStorage
from model_service.domain.events.epoch_finished import EpochFinished
from model_service.domain.entities.training.training_result import TrainingResult
from model_service.domain.repositories.abstract_training_result_repository import AbstractTrainingResultRepository
from model_service.shared.logging.log_function_execution import log_function_execution


class SaveResultOnEpochFinishedHandler:
    @provide
    def __init__(
        self,
        training_result_repository: AbstractTrainingResultRepository = Dependency(),
        data_storage: AbstractDataStorage = Dependency(),
    ) -> None:
        self.training_result_repository = training_result_repository
        self.data_storage = data_storage

    @log_function_execution()
    def __call__(self, event: EpochFinished) -> None:
        training_result = self.training_result_repository.get_by_training_session_id(event.training_session_id)

        if training_result is not None and training_result.validation_loss < event.validation_loss:
            return

        weights_file_key = "model-weights/" + uuid.uuid4().hex
        weights_file_content = pickle.dumps(event.weights)
        self.data_storage.save_file(weights_file_key, weights_file_content)

        new_training_result = TrainingResult.create(
            user=event.user,
            training_session_id=event.training_session_id,
            loss=event.loss,
            validation_loss=event.validation_loss,
            metrics=event.metrics,
            weights_file_key=weights_file_key,
        )

        self.training_result_repository.save(new_training_result)

        if training_result is not None:
            self.data_storage.delete_file(training_result.weights_file_key)
            self.training_result_repository.delete_by_id(training_result.id)
