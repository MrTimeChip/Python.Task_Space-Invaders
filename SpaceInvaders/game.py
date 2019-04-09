import pygame
import sys
import background
import level
from gameobject import Gameobject

DEBUG_MODE = True
GAME_OVER = False
GAME_WIN = False
GAME_END = False

enemy_count = 0
score = 0
total_score = 0
FPS = 60
current_level = None
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
    global GAME_OVER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if GAME_OVER:
                start_game()
            if GAME_WIN:
                start_game(current_level.next_level_name)


def start_game(level_name: str = 'first'):
    global GAME_OVER, GAME_WIN, current_level, score, total_score
    if level_name == 'end':
        end_game()
        return
    if level_name == 'first':
        total_score = 0
    total_score += score
    score = 0
    GAME_OVER = False
    GAME_WIN = False
    current_level = level.levels[level_name]
    level.load_level(level_name, window)


def end_game():
    global GAME_END, GAME_WIN, GAME_OVER, score, total_score
    GAME_WIN = False
    GAME_OVER = False
    GAME_END = True
    total_score += score
    score = 0


def draw_fps():
    fps = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))
    window.blit(fps, (25, 25))


def draw_game_over():
    game_over_text = game_over_font.render('YOU DIED', True, pygame.Color('white'))
    window.blit(game_over_text, (window.get_width()//2 - 140, window.get_height()//2 - 100))
    continue_text = font.render('CONTINUE?', True, pygame.Color('white'))
    window.blit(continue_text, (window.get_width() // 2 - 130, window.get_height() // 2))


def draw_game_end():
    game_end_text = game_over_font.render("YOU'VE FINISHED!", True, pygame.Color('white'))
    window.blit(game_end_text, (window.get_width()//2 - 240, window.get_height()//2 - 100))
    congrats_text = font.render('CONGRATULATIONS!', True, pygame.Color('white'))
    window.blit(congrats_text, (window.get_width() // 2 - 120, window.get_height() // 2))
    total_score_text = font.render('TOTAL SCORE: ' + str(total_score), True, pygame.Color('white'))
    window.blit(total_score_text, (window.get_width() // 2 - 100, window.get_height() // 2 + 50))


def draw_game_win():
    game_over_text = game_over_font.render('YOU WON!', True, pygame.Color('white'))
    window.blit(game_over_text, (window.get_width()//2 - 140, window.get_height()//2 - 100))
    next_lvl_text = font.render('NEXT LEVEL?', True, pygame.Color('white'))
    window.blit(next_lvl_text, (window.get_width() // 2 - 130, window.get_height() // 2))


def draw_interface():
    window.fill((0, 0, 0))
    if DEBUG_MODE:
        draw_fps()

    player_health_text = font.render('hp: ' + str(player.health), True, pygame.Color('white'))
    window.blit(player_health_text, (25, window.get_height() - 50))
    player_score_text = font.render('score: ' + str(score), True, pygame.Color('white'))
    window.blit(player_score_text, (window.get_width()//2 - 60, 25))

    if GAME_END:
        draw_game_end()
    elif GAME_OVER:
        draw_game_over()
    elif GAME_WIN:
        draw_game_win()


def update_gameobjects():
    global GAME_WIN
    if enemy_count == 0:
        GAME_WIN = True

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
    while True:
        clock.tick(FPS)

        handle_events()

        update_gameobjects()
