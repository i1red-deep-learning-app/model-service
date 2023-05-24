import io

import pandas as pd

from model_service.application.commands.start_ffn_training import StartFfnTraining
from model_service.application.integration_events.core.publishers import publish_integration_event
from model_service.application.integration_events.training_completed import TrainingCompleted
from model_service.dependencies.dependency_management.provide import Dependency, provide
from model_service.domain.data_storage.abstract_data_storage import AbstractDataStorage
from model_service.domain.repositories.abstract_feed_forward_network_repository import (
    AbstractFeedForwardNetworkRepository,
)
from model_service.domain.repositories.abstract_table_dataset_repository import AbstractTableDatasetRepository
from model_service.domain.repositories.abstract_training_session_repository import AbstractTrainingSessionRepository
from model_service.domain.services.model_training.train_feed_forward_network import train_feed_forward_network
from model_service.utility.logging.log_function_execution import log_function_execution


@log_function_execution()
@provide
def start_ffn_training(
    command: StartFfnTraining,
    feed_forward_network_repository: AbstractFeedForwardNetworkRepository = Dependency(),
    training_session_repository: AbstractTrainingSessionRepository = Dependency(),
    table_dataset_repository: AbstractTableDatasetRepository = Dependency(),
    data_storage: AbstractDataStorage = Dependency(),
) -> None:
    training_session = training_session_repository.get_by_id(command.training_session_id)
    feed_forward_network = feed_forward_network_repository.get_by_id(training_session.network_id)
    table_dataset_info = table_dataset_repository.get_by_id(training_session.dataset_id)

    table_dataset_file_bytes = data_storage.load_file(table_dataset_info.file_key)
    with io.BytesIO(table_dataset_file_bytes) as bytes_io:
        data = pd.read_feather(bytes_io)

    train_feed_forward_network(feed_forward_network, training_session, table_dataset_info, data)

    event = TrainingCompleted(training_session_id=command.training_session_id)
    publish_integration_event(event)
