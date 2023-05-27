from uuid import UUID, uuid4

import pytest


@pytest.fixture
def table_dataset_id() -> UUID:
    return uuid4()
