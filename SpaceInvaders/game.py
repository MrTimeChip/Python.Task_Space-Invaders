import pygame
import sys
import background
import level
import sound
from timer import Timer
from gameobject import Gameobject

pygame.font.init()
pygame.mixer.init()
clock = pygame.time.Clock()
timer_screen = Timer()

RES_WIDTH = 800
RES_HEIGHT = 600

DEBUG_MODE = False
FPS = 60

GAME_OVER = False
GAME_WIN = False
GAME_END = False

enemy_count = 0

current_score = 0
total_score = 0

current_level = None


window = None
player = None

active_gameobjects = []

font = pygame.font.SysFont('Impact', 30)
game_over_font = pygame.font.SysFont('Impact', 80)

background.setup_stars(25, 5, RES_WIDTH, RES_HEIGHT)


def add_gameobject(gameobject: Gameobject):
    """
    Adds gameobject to the game.
    (Adds to the active_gameobjects list)
    :param gameobject: gameobject to add.
    """
    if not isinstance(gameobject, Gameobject):
        raise ValueError('The object was not a gameobject!')
    active_gameobjects.append(gameobject)


def spawn_player():
    """Spawns a player"""
    add_gameobject(player)


def handle_events():
    """
    Handles the events of pygame.
    """
    global GAME_OVER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if GAME_OVER:
                if timer_screen.start_timer(700):
                    start_game()
            if GAME_WIN:
                if timer_screen.start_timer(700):
                    start_game(current_level.next_level_name)


def start_game(level_name: str = 'first'):
    """
    Starts a game from the beginning.
    :param level_name: a level name to start with. ('first' by def.)
        (for all level names, see level.py)
    """
    global GAME_OVER, GAME_WIN, current_level, current_score, total_score
    if level_name == 'end':
        end_game()
        return
    if level_name == 'first':
        total_score = 0
    total_score += current_score
    current_score = 0
    GAME_OVER = False
    GAME_WIN = False
    current_level = level.levels[level_name]
    level.load_level(level_name, window)


def end_game():
    """
    Ends the game.
    """
    global GAME_END, GAME_WIN, GAME_OVER, current_score, total_score
    GAME_WIN = False
    GAME_OVER = False
    GAME_END = True
    total_score += current_score
    current_score = 0


def draw_fps():
    """
    Draws FPS onto the screen.
    """
    fps = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))
    window.blit(fps, (25, 25))


def draw_game_over():
    """
    Draws Game over onto the screen.
    """
    game_over_text = game_over_font.render('YOU DIED', True, pygame.Color('white'))
    window.blit(game_over_text, (RES_WIDTH//2 - 140, RES_HEIGHT//2 - 100))
    continue_text = font.render('RESTART?', True, pygame.Color('white'))
    window.blit(continue_text, (RES_WIDTH // 2 - 130, RES_HEIGHT // 2))


def draw_game_end():
    """
    Draws Game end onto the screen.
    """
    game_end_text = game_over_font.render("YOU'VE FINISHED!", True, pygame.Color('white'))
    window.blit(game_end_text, (RES_WIDTH//2 - 270, RES_HEIGHT//2 - 100))
    congrats_text = font.render('CONGRATULATIONS!', True, pygame.Color('white'))
    window.blit(congrats_text, (RES_WIDTH // 2 - 120, RES_HEIGHT // 2))
    total_score_text = font.render('TOTAL SCORE: ' + str(total_score), True, pygame.Color('white'))
    window.blit(total_score_text, (RES_WIDTH // 2 - 100, RES_HEIGHT // 2 + 50))


def draw_game_win():
    """
    Draws Game win onto the screen.
    """
    game_over_text = game_over_font.render('YOU WON!', True, pygame.Color('white'))
    window.blit(game_over_text, (RES_WIDTH//2 - 140, RES_HEIGHT//2 - 100))
    next_lvl_text = font.render('NEXT LEVEL?', True, pygame.Color('white'))
    window.blit(next_lvl_text, (RES_WIDTH // 2 - 130, RES_HEIGHT // 2))


def draw_interface():
    """
    Draws all of the interface to the screen.
    Handles all 'draw_' functions.
    """
    window.fill((0, 0, 0))
    if DEBUG_MODE:
        draw_fps()

    if not GAME_OVER and not GAME_WIN and not GAME_END:
        player_health_text = font.render('HP: ' + str(player.health), True, pygame.Color('white'))
        window.blit(player_health_text, (25, RES_HEIGHT - 50))
        player_score_text = font.render('Score: ' + str(current_score), True, pygame.Color('white'))
        window.blit(player_score_text, (RES_WIDTH//2 - 60, 25))

    if GAME_END:
        draw_game_end()
    elif GAME_OVER:
        draw_game_over()
    elif GAME_WIN:
        draw_game_win()


def update_gameobjects():
    """
    Updates all gameobjects in active_gameobjects,
    by calling an Update function.
    """
    global GAME_WIN, enemy_count
    if enemy_count == 0:
        sound.play_game_win()
        GAME_WIN = True
        enemy_count = -1

    draw_interface()
    background.draw_stars(0.3, window)

    if not GAME_OVER and not GAME_WIN and not GAME_END:
        for obj in active_gameobjects:
            if obj.is_destroyed():
                active_gameobjects.remove(obj)
                print('obj is destroyed, list size: ', len(active_gameobjects))
            obj.update()
    else:
        active_gameobjects.clear()
    pygame.display.update()


def game_loop():
    """
    The main loop of the game.
    """
    while True:
        clock.tick(FPS)

        handle_events()

        update_gameobjects()
