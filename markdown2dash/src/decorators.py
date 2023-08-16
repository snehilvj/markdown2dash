import inspect
from functools import wraps

from .utils import create_class_name


def class_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        name = func.__name__ if inspect.isfunction(func) else func.__self__.block_name
        ret.className = create_class_name(name)

        return ret

    return wrapper
