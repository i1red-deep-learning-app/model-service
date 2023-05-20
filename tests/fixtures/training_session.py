import pytest

from model_service.domain.entities.training.loss_function_type import LossFunctionType
from model_service.domain.entities.training.metric_type import MetricType
from model_service.domain.entities.training.training_session import TrainingSession
from model_service.domain.entities.value_objects.optimizer import Optimizer, OptimizerType


@pytest.fixture
def training_session(
    training_session_id: str, user: str, feed_forward_network_id: str, table_dataset_id: str
) -> TrainingSession:
    return TrainingSession(
        id=training_session_id,
        user=user,
        network_id=feed_forward_network_id,
        dataset_id=table_dataset_id,
        optimizer=Optimizer(type=OptimizerType.ADAM, params={}),
        loss_function=LossFunctionType.BINARY_CROSSENTROPY,
        metrics=[MetricType.ACCURACY],
        epochs=5,
        batch_size=1,
        validation_split=0.2,
    )
