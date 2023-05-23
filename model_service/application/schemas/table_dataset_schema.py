from pydantic import BaseModel


class TableDatasetSchema(BaseModel):
    user: str
    file_key: str
    label_column: str
