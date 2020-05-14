
from logcat import LogCat

class Table:
    @LogCat.log_func
    def __init__(self, cls=None):
        self._cls = cls

        self._cache = {}

    @LogCat.log_func
    def get_value(self, entity):
        obj = None

        if entity in self._cache:
            obj = self._cache[entity]
        elif self._cls:
            obj = self._cls()

        return obj;

    @LogCat.log_func
    def update(self, entity, value):
        self._cache[entity] = self._cls(value)

# table.py
