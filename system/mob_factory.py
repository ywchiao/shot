
from random import randint

from entity import Entity

from .system import System

from logcat import LogCat

class MobFactory(System):
    @LogCat.log_func
    def __init__(self):
        super().__init__()

        self.on("cmd_mob", self._mob)

    @LogCat.log_func
    def _mob(self, entity, scene=""):
        entity = Entity.next()

        self.emit(
            "cmd_load_sprite", entity, frames=(2, 3)
        )

        self.emit("cmd_respawn", entity)

        if randint(0, 1):
            self.emit("cmd_rotate", entity, degree=1)
        else:
            self.emit("cmd_rotate", entity, degree=-1)

        self.emit("cmd_forward", entity)

        scene = scene_manager.get_scene(scene)
        scene.add_child(entity)

# mob_factory.py
