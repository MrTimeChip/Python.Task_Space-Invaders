import pygame
import sys
import background
from gameobject import Gameobject

score = 0
FPS = 60
pygame.font.init()
current_drawable_objects = []
window = None
player = None
clock = pygame.time.Clock()
font = pygame.font.SysFont('Comic Sans MS', 30)


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


def draw_fps():
    fps = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))
    window.blit(fps, (25, 25))


def draw_interface():
    window.fill((0, 0, 0))
    draw_fps()

    player_health_text = font.render('hp: ' + str(player.health), True, pygame.Color('white'))
    window.blit(player_health_text, (25, window.get_height() - 50))
    player_score_text = font.render('score: ' + str(score), True, pygame.Color('white'))
    window.blit(player_score_text, (window.get_width()//2 - 60, 25))


def update_gameobjects():
    draw_interface()
    background.draw_stars(0.3, window)

    for obj in current_drawable_objects:
        if obj.is_destroyed():
            current_drawable_objects.remove(obj)
            print('obj is destroyed, list size: ', len(current_drawable_objects))
        obj.update()

    pygame.display.update()


def game_loop():
    while True:
        clock.tick(FPS)

        handle_events()

        update_gameobjects()

