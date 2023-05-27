from uuid import UUID

from mongoengine import Document, StringField, UUIDField


class TableDatasetDocument(Document):
    id: UUID = UUIDField(db_field="_id", primary_key=True)
    user: str = StringField()
    file_key: str = StringField()
    label_column: str = StringField()
