
import pygame

class RotateSystem:
    def __init__(self):
        pass

    def update(self, surface, degree=0):
        return pygame.transform.rotate(surface, degree)

# rotate_system.py
