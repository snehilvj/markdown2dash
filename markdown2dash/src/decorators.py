from functools import wraps

from .utils import create_class_name


def class_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        name = func.__name__
        ret.className = "m2d-" + create_class_name(name)

        return ret

    return wrapper
