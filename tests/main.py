import os
from typing import Final

import pytest


TESTS_DIR: Final[str] = os.path.dirname(os.path.abspath(__file__))


if __name__ == "__main__":
    test_dir = os.path.dirname(os.path.abspath(__file__))
    pytest.main([TESTS_DIR, "-v"])
