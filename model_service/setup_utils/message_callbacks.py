from pika.adapters.blocking_connection import BlockingChannel

from model_service.application.command_callbacks.create_feed_forward_network_callback import (
    create_feed_forward_network_callback,
)
from model_service.application.command_callbacks.create_table_dataset_callback import create_table_dataset_callback
from model_service.application.command_callbacks.create_training_session_callback import (
    create_training_session_callback,
)
from model_service.application.command_callbacks.start_ffn_training_callback import start_ffn_training_callback


def setup_message_callbacks(channel: BlockingChannel) -> None:
    channel.queue_declare(queue="start_ffn_training")
    channel.basic_consume(queue="start_ffn_training", on_message_callback=start_ffn_training_callback)

    channel.queue_declare(queue="create_table_dataset")
    channel.basic_consume(queue="create_table_dataset", on_message_callback=create_table_dataset_callback)

    channel.queue_declare(queue="create_training_session")
    channel.basic_consume(queue="create_training_session", on_message_callback=create_training_session_callback)

    channel.queue_declare(queue="create_feed_forward_network")
    channel.basic_consume(queue="create_feed_forward_network", on_message_callback=create_feed_forward_network_callback)
