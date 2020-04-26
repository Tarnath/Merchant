import pygame
from merchant.rendering import renderer
from merchant.rendering import scene
from merchant.rendering import base_ui_objects
from merchant.rendering import shapes

running = True

pygame.init()

(width, height) = (1400, 675)
display = pygame.display.set_mode((width, height))
pygame.display.flip()

renderer = renderer.Renderer(display)
test_scene = scene.Scene(scene.BASE_LAYER)
renderer.add_scene(test_scene)

button = base_ui_objects.Button(scene.Position(50, 50), shapes.Rectangle(50, 30), "Test")
test_scene.add_object(button)

while running:
    renderer.render()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()