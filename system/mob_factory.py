
from component import config

from util import load_module

from .system import System

from logcat import LogCat

class MobFactory(System):
    @LogCat.log_func
    def __init__(self):
        super().__init__()

        self._cache = {}

        self.on("cmd_mob_new", self._mob_create)

    @LogCat.log_func
    def _mob_create(self, e, mob_class):
        if not mob_class in self._cache:
            module = load_module(mob_class, f"{config.mobs}/{mob_class}.py")
            self._cache[mob_class] = getattr(module, mob_class.capitalize())

        mob = self._cache[mob_class]()

        self.emit(
            "cmd_load_sprite", mob.entity, frames=(2, 3)
        )

        self.emit("cmd_respawn", mob.entity)
        self.emit("cmd_obj_inited", e.source, entity=mob.entity)

# mob_factory.py
