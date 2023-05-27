import logging
import sys

from model_service.shared.dependency_management.provider_getters import get_singleton_provider
from model_service.setup_utils.dependencies import setup_dependencies
from model_service.setup_utils.domain_events import setup_domain_event_handlers
from model_service.setup_utils.integration_events import setup_integration_event_publishers
from model_service.setup_utils.message_callbacks import setup_message_callbacks
from model_service.setup_utils.mongo_db import setup_mongo_connection
from model_service.setup_utils.rabbit_mq import get_rabbit_channel


def main() -> None:
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)

    provider = get_singleton_provider()

    setup_dependencies(provider)
    setup_domain_event_handlers()

    channel = get_rabbit_channel()
    setup_integration_event_publishers(channel)
    setup_message_callbacks(channel)

    setup_mongo_connection()

    channel.start_consuming()


if __name__ == "__main__":
    main()
