
from .speed import Speed

from .entity_group import EntityGroup

from .facing_table import FacingTable
from .frame_table import FrameTable
from .vector_table import VectorTable

from .sprite_sheet import SpriteSheet

facing = FacingTable()
speed = Speed()

sprite_sheet = SpriteSheet("sprites.png")
sprite_origin = FrameTable()
sprite_drawing = FrameTable()

position = VectorTable()
moving_vector = VectorTable()

moving_objects = EntityGroup()
viewable_objects = EntityGroup()

# __init__.py
