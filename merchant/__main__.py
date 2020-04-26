import pygame
from merchant.rendering import renderer
from merchant.rendering import scene
from merchant.rendering import base_ui_objects
from merchant.rendering import shapes

from merchant.events import handler
from merchant.events import listeners

import sys

running = True

pygame.init()

(width, height) = (1400, 675)
display = pygame.display.set_mode((width, height))
pygame.display.flip()

renderer = renderer.Renderer(display)
test_scene = scene.Scene(scene.BASE_LAYER)
renderer.add_scene(test_scene)

eventHandler = handler.EventHandler()

button = base_ui_objects.Button(scene.Position(50, 50), shapes.Rectangle(50, 30), "Test")
test_scene.add_object(button)

def log(event):
    if event == pygame.MOUSEBUTTONDOWN:
        sys.stdout.write("click\n")
    if event == pygame.MOUSEBUTTONUP:
        sys.stdout.write("click\n")

button.trigger_action = log

eventHandler.add_listener(listeners.ClickListener(button))

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    eventHandler.trigger_listeners(events)
    renderer.render()

pygame.quit()