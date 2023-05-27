from uuid import UUID

from mongoengine import Document, StringField, FloatField, DictField, UUIDField


class TrainingResultDocument(Document):
    id: UUID = UUIDField(db_field="_id", primary_key=True)
    user: str = StringField()
    training_session_id: UUID = UUIDField()
    loss: float = FloatField()
    validation_loss: float = FloatField()
    metrics: dict = DictField()
    weights_file_key: str = StringField()
