
from collections import deque

from component import scene_manager
from component import sprite_origin
from component import sprite_drawing
from component import sprite_manager
from component import ui

from .system import System

from logcat import LogCat

class Painting(System):
    @LogCat.log_func
    def __init__(self):
        super().__init__()

        self.on("cmd_load_sprite", self._load_sprite)
        self.on("cmd_repaint", self._repaint)

    @LogCat.log_func
    def _load_sprite(self, e, frames=(0, 0)):
        entity = e.target

        anime_frames = [
            sprite_manager.get_sprite(i) for i in frames
        ]

        sprite_origin.update(entity, anime_frames)
        sprite_drawing.update(entity, anime_frames)

    @LogCat.log_func
    def _repaint(self, e, screen=None):
        # 清除畫面，只剩下背景
        self.emit("cmd_clear", screen.entity)

        queue = deque([scene_manager.current_scene().root])

        while queue:
            node = queue.popleft()

            if node:
                queue.extend(node.children)

                # 通知 *node* 在 window 上將自己畫 (render) 出來
                self.emit("cmd_render", node.value, screen=screen)

        queue = deque([ui.root])

        while queue:
            node = queue.popleft()

            if node:
                queue.extend(node.children)

                # 通知 *node* 在 window 上將自己畫 (render) 出來
                self.emit("cmd_render", node.value, screen=screen)

# painting.py
