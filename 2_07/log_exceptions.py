import logging
import ui
from functools import wraps

logging.basicConfig(
    filename="errors.log",
    level=logging.ERROR,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding='utf-8'
)


def log_error(display=True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logging.exception(e)
                if display:
                    ui.show_error(f'Error: {e}')
        return wrapper
    return decorator