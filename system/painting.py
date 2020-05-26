
from collections import deque

from component import position
from component import scene_manager
from component import sprite_origin
from component import sprite_drawing
from component import sprite_sheet

from core import Element

from logcat import LogCat

class Painting(Element):
    @LogCat.log_func
    def __init__(self):
        super().__init__()

        self.on("cmd_load_sprite", self._load_sprite)
        self.on("cmd_repaint", self._repaint)

    @LogCat.log_func
    def _load_sprite(self, entity, frames=(0, 0)):
        anime_frames = [
            sprite_sheet.get_sprite(i) for i in frames
        ]

        sprite_origin.update(entity, anime_frames)
        sprite_drawing.update(entity, anime_frames)

    @LogCat.log_func
    def _render_sprite(self, window, entity):
        sprite = sprite_drawing.get_value(entity).next

        if sprite:
            rect = sprite.get_rect()
            rect.center = position.get_value(entity).value

            window.blit(sprite, rect)

    @LogCat.log_func
    def _render(self, window, scene):
        queue = deque([scene.root])

        while queue:
            node = queue.popleft()

            if node:
                queue.extend(node.children)

                if node.value and node.visible:
                    self._render_sprite(window, node.entity)


    @LogCat.log_func
    def _repaint(self, entity, window, background):
        scene = scene_manager.get_scene("sample")

        # 清除畫面，只剩下背景
        window.blit(background, (0, 0))

        self._render(window, scene)

# painting.py
