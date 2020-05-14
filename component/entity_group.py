
from logcat import LogCat

class EntityGroup:
    def __init__(self):
        self._cache = set()

    @LogCat.log_func
    def register(self, entity):
        self._cache.add(entity)

    @LogCat.log_func
    def remove(self, entity):
        if entity in self._cache:
            self._cache.remove(entity)

    @property
    def entities(self):
        return tuple(self._cache)

# entity_group.py
