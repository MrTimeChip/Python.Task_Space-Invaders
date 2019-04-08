from gameobject import Gameobject
import pygame


class Enemy(Gameobject):
    def __init__(self, x: int, y: int, width: int = 20, height: int = 20, health: int = 100, window=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self._window = window
        self._window_width = window.get_width()
        self._window_height = window.get_height()
        self.rect = None

    def update(self):
        """ Called every tick """
        self.draw(self._window)

    def draw(self, window, sprite_path: str = 'Sprites/Enemies/Enemy_3.png'):
        """ Draw an object in a certain window """
        image = pygame.transform.scale(pygame.image.load(sprite_path), (self.width, self.height))
        self.rect = image.get_rect(left=self.x, top=self.y)
        window.blit(image, (self.x, self.y))

    def get_rect(self):
        """ Returns the Rect of the image """
        return self.rect

    def receive_damage(self, damage: int):
        self.health -= damage

    def is_destroyed(self):
        """ Checks if object is destroyed """
        return self.health <= 0

