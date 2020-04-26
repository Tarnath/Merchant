import pygame
from merchant.rendering import scene
from merchant.rendering import colors

def load_basic_font():
    return pygame.font.Font("Lato-Regular.ttf", 20)

def load_title_font():
    return pygame.font.Font("riesling.ttf", 80)

def render_text(font: pygame.font.Font, position: scene.Position, display: pygame.display, text: str):
    textSurfaceObj = font.render(text, True, colors.BLACK, None)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.topleft = (position.x, position.y)
    display.blit(textSurfaceObj, textRectObj)