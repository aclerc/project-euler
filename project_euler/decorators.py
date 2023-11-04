import functools
import time
from collections.abc import Callable


def print_run_time(func: Callable) -> Callable:
    """print the runtime of the decorated funtion"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):  # noqa ANN401
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"finished {func.__name__!r} in {run_time:.3f} secs")
        return value

    return wrapper_timer
