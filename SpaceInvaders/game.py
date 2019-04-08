import pygame
import sys
import background
from gameobject import Gameobject

FPS = 60

current_drawable_objects = []
window = None
player = None


def add_gameobject(gameobject: Gameobject):
    if not isinstance(gameobject, Gameobject):
        raise ValueError('The object was not a gameobject!')
    current_drawable_objects.append(gameobject)


def spawn_player():
    add_gameobject(player)


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def update_gameobjects():
    window.fill((0, 0, 0))
    background.draw_stars(10, window)

    for obj in current_drawable_objects:
        if obj.is_destroyed():
            current_drawable_objects.remove(obj)
            print('obj is destroyed, list size: ', len(current_drawable_objects))
        obj.update()

    pygame.display.update()


def game_loop():
    while True:
        pygame.time.delay(FPS)

        handle_events()

        update_gameobjects()









