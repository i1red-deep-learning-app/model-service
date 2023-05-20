from unittest.mock import MagicMock

import numpy as np
import pandas as pd

from model_service.domain.entities.dataset.table_dataset import TableDataset
from model_service.domain.entities.neural_network.feed_forward_network import FeedForwardNetwork
from model_service.domain.entities.training.training_session import TrainingSession
from model_service.domain.events.epoch_finished import EpochFinished
from model_service.domain.services.model_training.train_feed_forward_network import train_feed_forward_network


def test_train_feed_forward_network(
    feed_forward_network: FeedForwardNetwork,
    training_session: TrainingSession,
    dataset_info: TableDataset,
    data: pd.DataFrame,
    epoch_finished_handler_mock: MagicMock,
) -> None:
    train_feed_forward_network(feed_forward_network, training_session, dataset_info, data)

    assert epoch_finished_handler_mock.call_count == training_session.epochs

    for call_index, call in enumerate(epoch_finished_handler_mock.mock_calls):
        event: EpochFinished
        (event,) = call.args

        assert event.user == training_session.user
        assert event.training_session_id == training_session.id
        assert event.epoch == call_index
        assert isinstance(event.loss, float)
        assert isinstance(event.validation_loss, float)

        message = "Event should have training and validation metric for each metric specified in training session"
        assert len(event.metrics) == 2 * len(training_session.metrics), message

        assert isinstance(event.weights, list)
        for layer_weights in event.weights:
            assert isinstance(layer_weights, np.ndarray)
