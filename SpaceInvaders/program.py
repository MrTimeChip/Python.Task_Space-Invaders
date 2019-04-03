import pygame
import background
from player import Player
from game import Game

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Space Invaders")

background.setup_stars(25, 5, win)

player = Player(220, 450, 30, 20, window=win)
Game.window = win
Game.add_gameobject(player)
Game.game_loop()
