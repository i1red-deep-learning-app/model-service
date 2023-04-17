from bson import ObjectId
from mongoengine import Document, StringField, ObjectIdField, IntField


class TableDatasetModel(Document):
    id: ObjectId = ObjectIdField(db_field="_id", primary_key=True, default=ObjectId)
    user: str = StringField()
    file_key: str = StringField()
    number_of_features: int = IntField()
    label_column: str = StringField()
