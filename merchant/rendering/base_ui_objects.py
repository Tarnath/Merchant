import pygame
from merchant.rendering import scene
from merchant.rendering import shapes
from merchant.rendering import colors
from merchant.rendering import text
from merchant.rendering import renderer


class Box(scene.Object):

    def __init__(self, position: scene.Position, dimensions: shapes.Rectangle, layer: int):
        super().__init__(position, layer)
        self.dimensions: shapes.Rectangle = dimensions
        self.border_color: pygame.Color = colors.BLACK
        self.border_width: int = 2

    def render(self, display: pygame.display):
        rect = pygame.Rect(self.position.x, self.position.y, self.dimensions.width, self.dimensions.height)
        pygame.draw.rect(display, self.border_color, rect, self.border_width)


class Button(Box):

    def __init__(self, position: scene.Position, dimensions: shapes.Rectangle, text: str = ""):
        super().__init__(position, dimensions, scene.UI_LAYER)
        self.text: str = text
        self.text_color: pygame.Color = colors.BLACK

    def render(self, display: pygame.display):
        super().render(display)
        text_size = text.load_basic_font().size(self.text)

        if text_size[0] > self.dimensions.width:
            raise renderer.RenderingError("text too long for containing box (%s > %s), increase dimensions or adapt text"
                                          % (text_size[0], self.dimensions.width))

        if text_size[1] > self.dimensions.height:
            raise renderer.RenderingError("text too high for containing box (%s > %s) , increase dimensions"
                                          % (text_size[1], self.dimensions.height))

        x = (self.dimensions.width - text_size[0]) / 2
        y = (self.dimensions.height - text_size[1]) / 2
        text.render_text(text.load_basic_font(), self.position.shift_by(x, y), display, self.text)
