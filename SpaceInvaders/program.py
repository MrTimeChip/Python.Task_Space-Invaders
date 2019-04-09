import pygame
import background
from enemy import Enemy
from player import Player
import game

RES_WIDTH = 800
RES_HEIGHT = 600

pygame.init()
win = pygame.display.set_mode((RES_WIDTH, RES_HEIGHT))

pygame.display.set_caption("Space Invaders")

background.setup_stars(25, 5, win)

#for row in range(8):
#    for column in range(3):
#        path = 'Sprites/Enemies/Enemy_' + str(3 - column) + '.png'
#        game.add_gameobject(Enemy(RES_WIDTH//5 + 60*row, RES_HEIGHT//5 + 60*column, 50, 50, window=win, sprite_path=path))
#BOSS = Enemy(190, 250, 100, 100, 200, window=win)
#game.add_gameobject(BOSS)

game.window = win
game.start_game()
game.game_loop()
