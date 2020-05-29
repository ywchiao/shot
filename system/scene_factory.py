
import json

from pathlib import Path

from component import config
from component import scene_manager

from util import Node

from .system import System

from logcat import LogCat

class SceneFactory(System):
    @LogCat.log_func
    def __init__(self):
        super().__init__()

        self.on("cmd_scene_load", self._scene_load)
        self.on("cmd_scene_change", self._scene_change)
        self.on("cmd_object_respawned", self._add_object)

    def _scene_change(self, entity, title):
        scene_manager.change_scene(title)

    def _scene_load(self, entity):
        path = Path(f"{config.scenes}/{entity}.json")

        with path.open() as fin:
            self._scene_build(json.load(fin))

    def _scene_build(self, desc):
        scene_manager.add_scene(desc["title"])

        for key, value in desc["mobs"].items():
            for i in range(value):
                self.emit("cmd_mob_create", None, cls_name=key)

    def _add_object(self, entity):
        scene = scene_manager.current_scene

        scene.add_child(Node(entity))

# scene_factory.py
