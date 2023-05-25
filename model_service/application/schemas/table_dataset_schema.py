from pydantic import BaseModel


class TableDatasetSchema(BaseModel):
    file_key: str
    label_column: str
