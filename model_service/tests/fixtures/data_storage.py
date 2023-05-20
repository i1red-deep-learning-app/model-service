import io

import pandas as pd
import pytest

from model_service.domain.data_storage.abstract_data_storage import AbstractDataStorage
from model_service.infrastructure.fake.data_storage.fake_data_storage import FakeDataStorage


@pytest.fixture
def data_storage(file_key: str, data: pd.DataFrame) -> AbstractDataStorage:
    storage = FakeDataStorage()

    with io.BytesIO() as bytes_io:
        data.to_feather(bytes_io)
        storage.save_file(file_key, bytes_io.getvalue())

    return storage
