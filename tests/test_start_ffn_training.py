from model_service.application.domain_event_handlers.save_result_on_epoch_finished_handler import (
    SaveResultOnEpochFinishedHandler,
)
from model_service.application.commands.start_ffn_training import StartFfnTraining
from model_service.application.services.start_ffn_training import start_ffn_training
from model_service.domain.data_storage.abstract_data_storage import AbstractDataStorage
from model_service.domain.events.epoch_finished import EpochFinished
from model_service.domain.events.handlers import register_domain_event_handler
from model_service.domain.repositories.abstract_feed_forward_network_repository import (
    AbstractFeedForwardNetworkRepository,
)
from model_service.domain.repositories.abstract_table_dataset_repository import AbstractTableDatasetRepository
from model_service.domain.repositories.abstract_training_result_repository import AbstractTrainingResultRepository
from model_service.domain.repositories.abstract_training_session_repository import AbstractTrainingSessionRepository


def test_start_ffn_training(
    command: StartFfnTraining,
    feed_forward_network_repository: AbstractFeedForwardNetworkRepository,
    training_session_repository: AbstractTrainingSessionRepository,
    table_dataset_repository: AbstractTableDatasetRepository,
    training_result_repository: AbstractTrainingResultRepository,
    data_storage: AbstractDataStorage,
) -> None:
    register_domain_event_handler(
        EpochFinished, SaveResultOnEpochFinishedHandler(training_result_repository, data_storage)
    )

    start_ffn_training(
        command, feed_forward_network_repository, training_session_repository, table_dataset_repository, data_storage
    )

    training_result = training_result_repository.get_by_training_session_id(command.training_session_id)

    assert training_result is not None

    # check that loading weights does not raise error
    data_storage.load_file(training_result.weights_file_key)