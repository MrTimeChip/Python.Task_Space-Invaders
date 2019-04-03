import pygame
import player
import sys
import background
from gameobject import Gameobject

current_drawable_objects = []
window = None


class Game:
    @staticmethod
    def add_gameobject(gameobject: Gameobject):
        if gameobject is not Gameobject:
            raise ValueError('The object was not a gameobject!')
        current_drawable_objects.append(gameobject)

    @staticmethod
    def handle_keys():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move('LEFT')
        if keys[pygame.K_RIGHT]:
            player.move('RIGHT')

    @staticmethod
    def handle_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    current_drawable_objects.append(player.shoot())

    @staticmethod
    def draw_screen():
        window.fill((0, 0, 0))
        background.draw_stars(10, window)

        for obj in current_drawable_objects:
            if obj.is_destroyed():
                current_drawable_objects.remove(obj)
                print('obj is destroyed, list size: ', len(current_drawable_objects))
            obj.draw(window)

        pygame.display.update()

    @staticmethod
    def game_loop():
        while True:
            pygame.time.delay(50)

            Game.handle_events()
            Game.handle_keys()

            Game.draw_screen()








