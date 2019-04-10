import pygame
import random

laser_shot = {
    '1': 'Sounds/laser_shot_1.wav',
    '2': 'Sounds/laser_shot_2.wav',
    '3': 'Sounds/laser_shot_3.wav'
}


def play_laser_shot(volume: float = 1.0):
    number = random.randint(1, 3)
    shot_sound = pygame.mixer.Sound(laser_shot[str(number)])
    shot_sound.set_volume(volume)
    shot_sound.play()


def play_explosion(volume: float = 1.0):
    explosion_sound = pygame.mixer.Sound('Sounds/explosion.wav')
    explosion_sound.set_volume(volume)
    explosion_sound.play()


def play_game_win(volume: float = 1.0):
    game_win_sound = pygame.mixer.Sound('Sounds/game_win.wav')
    game_win_sound.set_volume(volume)
    game_win_sound.play()
