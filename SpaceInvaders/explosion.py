from gameobject import Gameobject
import pygame
from timer import Timer


class Explosion(Gameobject):
    def __init__(self,
                 x: int,
                 y: int,
                 width: int = 15,
                 height: int = 15,
                 window=None,
                 sprite_path: str = 'Sprites/Effects/Explosion.png'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self._window = window
        self.rect = None
        self._sprite_path = sprite_path
        self._timer = Timer()

    def get_rect(self):
        """ Returns the Rect of the image """
        return self.rect

    def draw(self, window, ):
        """ Draw an object in a certain window """
        image = pygame.transform.scale(pygame.image.load(self._sprite_path), (self.width, self.height))
        self.rect = image.get_rect(left=self.x, top=self.y)
        window.blit(image, (self.x, self.y))

    def update(self):
        """ Called every tick """
        self.draw(self._window)

    def is_destroyed(self):
        """ Checks if object is destroyed """
        return self._timer.start_timer(100)
