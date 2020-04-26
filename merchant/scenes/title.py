from merchant.rendering import scene


class Title:

    def __init__(self):
        self.__scene = scene.Scene(scene.BASE_LAYER)
        self.__scene.add_object()