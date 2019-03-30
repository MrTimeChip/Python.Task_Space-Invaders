import pygame
import player
import sys
import background


pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Space Invaders")

background.setup_stars(25, 5, win)


def handle_keys():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move('LEFT')
    if keys[pygame.K_RIGHT]:
        player.move('RIGHT')


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def draw_screen():
    win.fill((0, 0, 0))
    player.draw_player(win)
    background.draw_stars(10, win)
    pygame.display.update()


def game_loop():
    while True:
        pygame.time.delay(50)

        handle_events()
        handle_keys()

        draw_screen()


player = player.Player(220, 450, 30, 20, window=win)

game_loop()









