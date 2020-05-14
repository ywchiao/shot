
import logging

class LogCat:
    _logger = logging.getLogger(__qualname__)

    @classmethod
    def dump_obj(cls, obj):
        cls._logger.debug(f"Dump_Obj: {str(obj)}")

    @classmethod
    def log(cls, string):
        cls._logger.info(string)

    @classmethod
    def log_func(cls, func):
        def wrapped_func(*args, **kwargs):
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)

            cls._logger.debug(f"{func.__qualname__}({signature})")

            return func(*args, **kwargs)

        return wrapped_func

# logcat.py
