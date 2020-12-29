
from .configuration import Configuration

from .facing_table import FacingTable
from .frame_table import FrameTable
from .vector_table import VectorTable

from .layout_manager import LayoutManager
from .scene_manager import SceneManager
from .window_manager import WindowManager

from .speed import Speed
from .sprite_manager import SpriteManager

from .status import Status

from .ui import UI

config = Configuration()

facing = FacingTable()
speed = Speed()

sprite_manager = SpriteManager()
sprite_origin = FrameTable()
sprite_drawing = FrameTable()

position = VectorTable()
moving_vector = VectorTable()

layout_manager = LayoutManager()
scene_manager = SceneManager()
window_manager = WindowManager()

status = Status()
ui = UI()

# __init__.py
