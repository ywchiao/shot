
from random import randint

from mob import Mob

from component import scene_manager

from .system import System

from logcat import LogCat

class SceneFactory(System):
    @LogCat.log_func
    def __init__(self):
        super().__init__()

        self.on("cmd_scene", self._scene)

    def _scene(self, entity, desc=None):
        scene_manager.update(desc["title"])

        for i in range(desc["mobs"]):
            self.emit("cmd_mob", None, { "scene": desc["title"] })

            self.emit("cmd_respawn", mob.entity)

    @LogCat.log_func
    def get_scene(self, title):
        if title in self._cache:
            scene = self._cache[title]
        else:
            scene = None

        return scene

# scene_factory.py
