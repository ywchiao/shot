
from .config import Config

from .facing_table import FacingTable
from .frame_table import FrameTable
from .vector_table import VectorTable

from .scene_manager import SceneManager
from .window_manager import WindowManager

from .speed import Speed
from .sprite_sheet import SpriteSheet

config = Config()

facing = FacingTable()
speed = Speed()

sprite_sheet = SpriteSheet("sprites.png")
sprite_origin = FrameTable()
sprite_drawing = FrameTable()

position = VectorTable()
moving_vector = VectorTable()

scene_manager = SceneManager()
window_manager = WindowManager()

# __init__.py
