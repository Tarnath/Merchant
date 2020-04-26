import pygame
from merchant.rendering import scene

BACKGROUND_LAYER = 0
BASE_LAYER = 10
UI_LAYER = 20
OVERLAY_LAYER = 30

class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def shift_by(self, x: int, y: int):
        return Position(self.x + x, self.y + y)


class Object(object):
    def __init__(self, position: scene.Position, layer : int):
        self.position: scene.Position = position
        self.layer: int = layer

    def render(self, screen: pygame.display):
        pass


class Scene:
    def __init__(self, layer: int):
        self.layer: int = layer
        self.__objects = []

    def add_object(self, object: scene.Object):
        self.__objects.append(object)

    def __byLayer(self, obj: scene.Object):
        return obj.layer

    def render(self, screen: pygame.display):
        self.__objects.sort(key=self.__byLayer)
        for obj in self.__objects:
            obj.render(screen)
