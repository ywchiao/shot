
from component import config
from component import layout_manager
from component import scene_manager

from util import Node

from .system import System

from logcat import LogCat

class SceneFactory(System):
    @LogCat.log_func
    def __init__(self):
        super().__init__()

        self.on("cmd_scene_change", self._scene_change)
        self.on("cmd_obj_inited", self._add_object)

    def _scene_change(self, e, scene):
        if not scene_manager.change_scene(scene):
            layout = layout_manager.get_layout(scene, config.scenes)

            for key, value in layout["mobs"].items():
                for i in range(value):
                    self.emit("cmd_mob_new", None, mob_class=key)

            scene_manager.new_scene(scene, layout["name"])

    def _add_object(self, e, entity):
        scene = scene_manager.current_scene()

        scene.add_object(Node(entity))

# scene_factory.py
