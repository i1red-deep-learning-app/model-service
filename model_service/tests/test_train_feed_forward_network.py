from typing import Generator
from unittest.mock import MagicMock

import numpy as np
import pandas as pd
import pytest

from model_service.domain.entities.dataset.table_dataset import TableDataset
from model_service.domain.entities.neural_network.feed_forward_network import FeedForwardNetwork
from model_service.domain.entities.training.loss_function_type import LossFunctionType
from model_service.domain.entities.training.metric_type import MetricType
from model_service.domain.entities.training.training_session import TrainingSession
from model_service.domain.entities.value_objects.activation_function import ActivationFunction, ActivationFunctionType
from model_service.domain.entities.value_objects.linear_layer import LinearLayer
from model_service.domain.entities.value_objects.optimizer import Optimizer, OptimizerType
from model_service.domain.events.epoch_finished import EpochFinished
from model_service.domain.events.handlers import domain_event_handler, register_event_handler, unregister_event_handler
from model_service.domain.services.model_training.train_feed_forward_network import train_feed_forward_network


@pytest.fixture
def user() -> str:
    return "test_user"


@pytest.fixture
def labels_column() -> str:
    return "labels"


@pytest.fixture
def feed_forward_network(user: str) -> FeedForwardNetwork:
    layers = [LinearLayer(size=128, activation=ActivationFunction(type=ActivationFunctionType.PRELU, params={}))]
    return FeedForwardNetwork(id="test_ffn", user=user, layers=layers)


@pytest.fixture
def dataset_info(user: str, labels_column: str) -> TableDataset:
    return TableDataset(id="test_dataset", user=user, file_key="test_file_key", label_column=labels_column)


@pytest.fixture
def training_session(user: str, dataset_info: TableDataset) -> TrainingSession:
    return TrainingSession(
        id="test_session",
        user=user,
        dataset_id=dataset_info.id,
        optimizer=Optimizer(type=OptimizerType.ADAM, params={}),
        loss_function=LossFunctionType.BINARY_CROSSENTROPY,
        metrics=[MetricType.ACCURACY],
        epochs=5,
        batch_size=1,
        validation_split=0.2,
    )


@pytest.fixture
def data(labels_column: str) -> pd.DataFrame:
    data_size = 1000
    column_1_data = np.random.randn(data_size)
    labels = (column_1_data > 0.5).astype("int")
    return pd.DataFrame({"column_1": column_1_data, labels_column: labels})


@pytest.fixture
def event_handler_mock() -> Generator[MagicMock, None, None]:
    event_handler_mock = MagicMock()
    register_event_handler(EpochFinished, event_handler_mock)
    yield event_handler_mock
    unregister_event_handler(EpochFinished, event_handler_mock)


def test_train_feed_forward_network(
    feed_forward_network: FeedForwardNetwork,
    training_session: TrainingSession,
    dataset_info: TableDataset,
    data: pd.DataFrame,
    event_handler_mock: MagicMock
) -> None:
    train_feed_forward_network(feed_forward_network, training_session, dataset_info, data)

    assert event_handler_mock.call_count == training_session.epochs

    for call_index, call in enumerate(event_handler_mock.mock_calls):
        event: EpochFinished
        (event,) = call.args

        assert event.user == training_session.user
        assert event.training_session_id == training_session.id
        assert event.epoch == call_index
        assert isinstance(event.loss, float)
        assert isinstance(event.validation_loss, float)

        message = "Event should have training and validation metric for each metric specified in training session"
        assert len(event.metrics) == 2 * len(training_session.metrics), message

        assert isinstance(event.weights, bytes)
