from pika.adapters.blocking_connection import BlockingChannel

from model_service.application.integration_event_publishers.default_exchange_publisher import DefaultExchangePublisher
from model_service.application.integration_events.core.publishers import register_integration_event_publisher
from model_service.application.integration_events.feed_forward_network_created import FeedForwardNetworkCreated
from model_service.application.integration_events.table_dataset_created import TableDatasetCreated
from model_service.application.integration_events.task_failed import TaskFailed
from model_service.application.integration_events.training_completed import TrainingCompleted
from model_service.application.integration_events.training_epoch_finished import TrainingEpochFinished
from model_service.application.integration_events.training_session_created import TrainingSessionCreated


def setup_integration_event_publishers(channel: BlockingChannel) -> None:
    register_integration_event_publisher(
        TableDatasetCreated, DefaultExchangePublisher(channel, queue="table_dataset_created")
    )
    register_integration_event_publisher(
        FeedForwardNetworkCreated, DefaultExchangePublisher(channel, queue="feed_forward_network_created")
    )
    register_integration_event_publisher(
        TrainingSessionCreated, DefaultExchangePublisher(channel, queue="training_session_created")
    )
    register_integration_event_publisher(
        TrainingEpochFinished, DefaultExchangePublisher(channel, queue="training_epoch_finished")
    )
    register_integration_event_publisher(
        TrainingCompleted, DefaultExchangePublisher(channel, queue="training_completed")
    )
    register_integration_event_publisher(TaskFailed, DefaultExchangePublisher(channel, queue="task_failed"))
