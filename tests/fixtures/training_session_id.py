from uuid import uuid4, UUID

import pytest


@pytest.fixture
def training_session_id() -> UUID:
    return uuid4()
