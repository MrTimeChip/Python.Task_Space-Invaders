import pygame
import sys
import background
from gameobject import Gameobject

DEBUG_MODE = True
GAME_OVER = False

score = 0
FPS = 60
pygame.font.init()
active_gameobjects = []
window = None
player = None
clock = pygame.time.Clock()
font = pygame.font.SysFont('Impact', 30)
game_over_font = pygame.font.SysFont('Impact', 80)


def add_gameobject(gameobject: Gameobject):
    if not isinstance(gameobject, Gameobject):
        raise ValueError('The object was not a gameobject!')
    active_gameobjects.append(gameobject)


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


def draw_game_over():
    game_over_text = game_over_font.render('YOU DIED', True, pygame.Color('white'))
    window.blit(game_over_text, (window.get_width()//2 - 140, window.get_height()//2 - 100))
    continue_text = font.render('CONTINUE?', True, pygame.Color('white'))
    window.blit(continue_text, (window.get_width() // 2 - 130, window.get_height() // 2))


def draw_interface():
    window.fill((0, 0, 0))
    if DEBUG_MODE:
        draw_fps()

    player_health_text = font.render('hp: ' + str(player.health), True, pygame.Color('white'))
    window.blit(player_health_text, (25, window.get_height() - 50))
    player_score_text = font.render('score: ' + str(score), True, pygame.Color('white'))
    window.blit(player_score_text, (window.get_width()//2 - 60, 25))

    if GAME_OVER:
        draw_game_over()


def update_gameobjects():

    draw_interface()
    background.draw_stars(0.3, window)

    if not GAME_OVER:
        for obj in active_gameobjects:
            if obj.is_destroyed():
                active_gameobjects.remove(obj)
                print('obj is destroyed, list size: ', len(active_gameobjects))
            obj.update()
    else:
        active_gameobjects.clear()
    pygame.display.update()


def game_loop():
    while True:
        clock.tick(FPS)

        handle_events()

        update_gameobjects()

