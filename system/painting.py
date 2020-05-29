
from collections import deque

from component import scene_manager
from component import sprite_origin
from component import sprite_drawing
from component import sprite_sheet

from .system import System

from logcat import LogCat

class Painting(System):
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
    def _repaint(self, entity):
        # 清除畫面，只剩下背景
        self.emit("cmd_clear", entity)

        queue = deque([scene_manager.current_scene])

        while queue:
            node = queue.popleft()

            if node:
                queue.extend(node.children)

                # 通知 *node* 在 window 上將自己畫 (render) 出來
                self.emit("cmd_render", node.value, window=entity)

# painting.py
