import pygame
from merchant.rendering import scene
from merchant.rendering import colors


class Renderer:
    def __init__(self, display: pygame.display):
        self.__display: pygame.display = display
        self.__scenes = []

    def add_scene(self, added_scene: scene.Scene):
        self.__scenes.append(added_scene)

    def __byLayer(self, scene: scene.Scene):
        return scene.layer

    def render(self):
        self.__display.fill(colors.WHITE)

        self.__scenes.sort(key= self.__byLayer)
        for current_scene in self.__scenes:
            current_scene.render(self.__display)

        pygame.display.flip()


class RenderingError(BaseException):
    pass
