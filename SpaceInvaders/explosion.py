from gameobject import Gameobject
import pygame
from timer import Timer


class Explosion(Gameobject):
    """
    Explosion class. A simple effect.
    """
    def __init__(self,
                 x: int,
                 y: int,
                 width: int = 15,
                 height: int = 15,
                 window=None,
                 sprite_path: str = 'Sprites/Effects/Explosion.png'):
        """
        Initializes the explosion.
        :param x: x coordinate to spawn at.
        :param y: y coordinate to spawn at.
        :param width: sprite width.
        :param height: sprite height.
        :param window: window to render in.
        :param sprite_path: path to the player sprite.
        """
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
        image = pygame.transform.scale(pygame.image.load(self._sprite_path),
                                       (self.width, self.height))
        self.rect = image.get_rect(left=self.x, top=self.y)
        window.blit(image, (self.x, self.y))

    def update(self):
        """ Called every tick """
        self.draw(self._window)

    def is_destroyed(self):
        """
        Checks if explosion is destroyed.
        True, if 100ms passed since initializing
        False, otherwise
        :return:
        """
        return self._timer.start_timer(100)
