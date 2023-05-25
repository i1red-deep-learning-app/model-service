import functools
import logging
from collections.abc import Callable
from typing import TypeVar

TFunction = TypeVar("TFunction", bound=Callable)


def log_exceptions(function: TFunction) -> TFunction:
    logger = logging.getLogger(function.__module__)

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:
            logger.exception(e)
            raise e

    return wrapper
