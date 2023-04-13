import pickle
from tensorflow.python.keras import callbacks

from model_service.domain.events.epoch_finished import EpochFinished
from model_service.domain.events.handlers import publish_domain_event


class EpochFinishedCallback(callbacks.Callback):
    def __init__(self, user: str, training_session_id: str) -> None:
        super().__init__()

        self.user = user
        self.training_session_id = training_session_id

    def on_epoch_end(self, epoch: int, logs: dict | None = None) -> None:
        loss = logs["loss"]
        validation_loss = logs["val_loss"]
        metrics = {metric: value for metric, value in logs.items() if metric != "loss" and metric != "val_loss"}
        weights = pickle.dumps(self.model.get_weights())

        event = EpochFinished(self.user, self.training_session_id, epoch, loss, validation_loss, metrics, weights)

        publish_domain_event(event)
