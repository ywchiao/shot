
from component import position
from component import sprite_origin
from component import sprite_drawing
from component import sprite_sheet

from component import viewable_objects

from event import dispatcher

from logcat import LogCat

class Painting:
    @LogCat.log_func
    def __init__(self):
        dispatcher.on("cmd_load_sprite", self._load_sprite)
        dispatcher.on("cmd_repaint", self._repaint)

    @LogCat.log_func
    def _load_sprite(self, entity, frames=(0, 0)):
        anime_frames = [
            sprite_sheet.get_sprite(i) for i in frames
        ]

        sprite_origin.update(entity, anime_frames)
        sprite_drawing.update(entity, anime_frames)

    @LogCat.log_func
    def _repaint(self, entity, window, background):
        # 清除畫面，只剩下背景
        window.blit(background, (0, 0))

        for entity in viewable_objects.entities:
            frame = sprite_drawing.get_value(entity).next

            if frame:
                rect = frame.get_rect()
                rect.center = position.get_value(entity).value

                window.blit(frame, rect)
            else:
                print(f"Frame can't be None. Something must be wrong.")

# painting.py
