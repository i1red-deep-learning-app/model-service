from mongoengine import connect
from pydantic import BaseSettings


class MongoDbSettings(BaseSettings):
    host: str
    port: int
    username: str
    password: str
    database: str

    class Config:
        env_prefix = "mongo_"


def setup_mongo_connection() -> None:
    mongo_settings = MongoDbSettings()
    connect(
        mongo_settings.database,
        host=mongo_settings.host,
        port=mongo_settings.port,
        username=mongo_settings.username,
        password=mongo_settings.password,
        uuidRepresentation="standard",
    )
