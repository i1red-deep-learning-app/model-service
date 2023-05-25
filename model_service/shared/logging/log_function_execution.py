import functools
import logging
import time
from collections.abc import Callable
from typing import TypeVar

TFunction = TypeVar("TFunction", bound=Callable)


def log_function_execution(log_level: int = logging.INFO) -> Callable[[TFunction], TFunction]:
    def decorator(function: TFunction) -> TFunction:
        logger = logging.getLogger(function.__module__)

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            logger.log(log_level, msg=f"Start execution of `{function.__qualname__}`")
            start_time = time.perf_counter()

            result = function(*args, **kwargs)

            finish_time = time.perf_counter()
            logger.log(log_level, msg=f"Finish execution of `{function.__name__}` in {finish_time - start_time:.2f}s")
            return result

        return wrapper

    return decorator
