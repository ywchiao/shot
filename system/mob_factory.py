
from component import config

from util import load_module

from .system import System

from logcat import LogCat

class MobFactory(System):
    @LogCat.log_func
    def __init__(self):
        super().__init__()

        self.on("cmd_mob_create", self._mob_create)

    @LogCat.log_func
    def _mob_create(self, entity, cls_name):
        module = load_module(cls_name, f"{config.mobs}/{cls_name}.py")
        cls = getattr(module, cls_name.capitalize())

        mob = cls()

        self.emit(
            "cmd_load_sprite", mob.entity, frames=(2, 3)
        )

        self.emit("cmd_respawn", mob.entity)

# mob_factory.py
