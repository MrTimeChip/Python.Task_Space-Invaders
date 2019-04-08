import pygame
import background
from enemy import Enemy
from player import Player
import game

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Space Invaders")

background.setup_stars(25, 5, win)

player = Player(220, 450, 30, 20, window=win)
for row in range(8):
    for column in range(3):
        game.add_gameobject(Enemy(120 + 30*row, 120 + 30*column, window=win))

BOSS = Enemy(190, 250, 100, 100, 200, window=win)
game.add_gameobject(BOSS)
game.window = win
game.player = player
game.spawn_player()
game.game_loop()
