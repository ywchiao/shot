
from .scene import Scene

from logcat import LogCat

class SceneManager:
    @LogCat.log_func
    def __init__(self):
        self._cache = {}

        self._current = None

    def current_scene(self):
        return self._cache[self._current]

    def new_scene(self, entity, title):
        self._cache[entity] = Scene(title)

        self._current = entity

    def change_scene(self, scene):
        succ = True

        if scene in self._cache:
            self._current = scene
        else:
            succ = False

        return succ

# scene_manager.py
