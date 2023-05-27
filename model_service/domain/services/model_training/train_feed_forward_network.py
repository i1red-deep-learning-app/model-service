import pandas as pd

from model_service.domain.entities.dataset.table_dataset import TableDataset
from model_service.domain.entities.neural_network.feed_forward_network import FeedForwardNetwork
from model_service.domain.entities.training.training_session import TrainingSession
from model_service.domain.services.model_training.callbacks.epoch_finished import EpochFinishedCallback
from model_service.domain.services.model_training.keras_converters.feed_forward_network import (
    create_keras_feed_forward_network,
)
from model_service.domain.services.model_training.keras_converters.loss import create_loss
from model_service.domain.services.model_training.keras_converters.metric import create_metric
from model_service.domain.services.model_training.keras_converters.optimizer import create_keras_optimizer
from model_service.shared.logging.log_function_execution import log_function_execution


@log_function_execution()
def train_feed_forward_network(
    feed_forward_network: FeedForwardNetwork,
    training_session: TrainingSession,
    dataset_info: TableDataset,
    data: pd.DataFrame,
) -> None:
    number_of_features = len(data.columns) - 1
    number_of_classes = data[dataset_info.label_column].nunique()

    model = create_keras_feed_forward_network(feed_forward_network, number_of_features, number_of_classes)

    optimizer = create_keras_optimizer(training_session.optimizer)
    loss = create_loss(training_session.loss_function)
    metric_list = [create_metric(m) for m in training_session.metrics]
    model.compile(optimizer, loss, metric_list)

    features = data.drop(dataset_info.label_column, axis="columns").to_numpy()
    labels = data[dataset_info.label_column].to_numpy()

    epoch_finished_callback = EpochFinishedCallback(training_session.user, training_session.id)

    model.fit(
        features,
        labels,
        epochs=training_session.epochs,
        batch_size=training_session.batch_size,
        validation_split=training_session.validation_split,
        callbacks=[epoch_finished_callback],
        verbose=0,
    )
