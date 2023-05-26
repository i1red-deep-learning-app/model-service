from bson import ObjectId
from mongoengine import Document, StringField, ObjectIdField


class TableDatasetDocument(Document):
    id: ObjectId = ObjectIdField(db_field="_id", primary_key=True, default=ObjectId)
    user: str = StringField()
    file_key: str = StringField()
    label_column: str = StringField()
