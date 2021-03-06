
from component import facing
from component import position
from component import sprite_drawing

from .system import System

from logcat import LogCat

class Mob(System):
    def __init__(self):
        super().__init__()

        self._visible = True
        self._movable = True

        self._point = (0, 0)
        self._degree = 0

        self.on("cmd_object_respawned", self._respawned)
        self.on("cmd_render", self._render)
        self.on("cmd_update", self._update)

    @LogCat.log_func
    def set_movable(self, movable):
        self._movable = movable

    @LogCat.log_func
    def set_visible(self, visible):
        self._visible = visible

    @LogCat.log_func
    def _render(self, e, screen):
        entity = e.target

        if self._visible:
            sprite = sprite_drawing.get_value(entity).next

            if sprite:
                rect = sprite.get_rect()
                rect.center = position.get_value(entity).value

                screen.render(sprite, rect)

    @LogCat.log_func
    def _respawned(self, e):
        self._x, self._y = position.get_value(self._entity).value
        self._degree = facing.get_value(self._entity).degree

    @LogCat.log_func
    def _update(self, e):
        self.emit("cmd_forward", self._entity)

# mob.py
