
import math

class MoveSystem:
    def __init__(self):
        pass

    def update(self, degree, drift, offset=(0, 0)):
        theta = (degree / 180) * math.pi

        drift[0] += (
            offset[0] * math.cos(theta) +
            offset[1] * math.sin(theta)
        )

        drift[1] += (
            - offset[0] * math.sin(theta) +
            offset[1] * math.cos(theta)
        )

        drift[0], x_offset = math.modf(drift[0])
        drift[1], y_offset = math.modf(drift[1])

        return (int(x_offset), int(y_offset))

# move_system.py
