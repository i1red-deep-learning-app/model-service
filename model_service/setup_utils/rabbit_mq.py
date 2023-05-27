from typing import Final

from pydantic import BaseSettings

from pika import BlockingConnection, ConnectionParameters, PlainCredentials
from pika.adapters.blocking_connection import BlockingChannel


class RabbitMqSettings(BaseSettings):
    host: str
    port: int
    username: str
    password: str

    class Config:
        env_prefix = "rabbit_"


def _get_connection_parameters() -> ConnectionParameters:
    settings = RabbitMqSettings()
    return ConnectionParameters(
        host=settings.host,
        port=settings.port,
        credentials=PlainCredentials(username=settings.username, password=settings.password),
    )


_CONNECTION: Final[BlockingConnection] = BlockingConnection(_get_connection_parameters())
_CHANNEL: Final[BlockingChannel] = _CONNECTION.channel()


def get_rabbit_channel() -> BlockingChannel:
    return _CHANNEL
