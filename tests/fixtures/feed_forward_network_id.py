from uuid import uuid4, UUID

import pytest


@pytest.fixture
def feed_forward_network_id() -> UUID:
    return uuid4()
