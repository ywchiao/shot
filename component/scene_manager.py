
import json

from pathlib import Path
from random import randint

from mob import Mob

from .scene import Scene

from event import dispatcher

from logcat import LogCat

class SceneManager:
    @LogCat.log_func
    def __init__(self):
        self._cache = {}

        path = Path(f"./data/scenes")

        for f in list(path.glob("./*.json")):
            with f.open() as fin:
                desc = json.load(fin)

                self.add_scene(desc["title"], self.create_scene(desc))

    @LogCat.log_func
    def add_scene(self, title, scene):
        self._cache[title] = scene

    @LogCat.log_func
    def create_scene(self, desc):
        scene = Scene()

        for i in range(desc["mob"]):
            mob = Mob()

            scene.add_object(mob)

            dispatcher.fire_event("cmd_respawn", mob.entity)

        return scene

    @LogCat.log_func
    def get_scene(self, title):
        if title in self._cache:
            scene = self._cache[title]
        else:
            scene = None

        return scene

# scene_manager.py
