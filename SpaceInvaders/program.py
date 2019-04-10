import pygame
import game

RES_WIDTH = 800
RES_HEIGHT = 600

pygame.init()
win = pygame.display.set_mode((RES_WIDTH, RES_HEIGHT))

pygame.display.set_caption("Space Invaders")

game.RES_WIDTH = RES_WIDTH
game.RES_HEIGHT = RES_HEIGHT
game.window = win
game.start_game()
game.game_loop()
