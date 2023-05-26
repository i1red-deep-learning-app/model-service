from bson import ObjectId
from mongoengine import Document, ObjectIdField, StringField, FloatField, DictField


class TrainingResultDocument(Document):
    id: ObjectId = ObjectIdField(db_field="_id", primary_key=True, default=ObjectId)
    user: str = StringField()
    training_session_id: ObjectId = ObjectIdField()
    loss: float = FloatField()
    validation_loss: float = FloatField()
    metrics: dict = DictField()
    weights_file_key: str = StringField()
