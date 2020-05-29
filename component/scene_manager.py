
from util import Node
from util import Table

from logcat import LogCat

class SceneManager:
    @LogCat.log_func
    def __init__(self):
        self._cache = Table(Node)

        self._current = "sample"

    @property
    def current_scene(self):
        return self._cache.get_value(self._current)

    def add_scene(self, entity):
        self._cache.update(entity)

        return self._cache.get_value(entity)

    def get_scene(self, entity):
        return self._cache.get_value(entity)

    def change_scene(self, entity):
        self._current = entity

# scene_manager.py
