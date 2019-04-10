import pygame
from damage_receiver import DamageReceiver
from explosion import Explosion
import game
from gameobject import Gameobject
from block import Block


class Projectile(Gameobject):
    """
    A simple projectile class, that can collide with objects and deal damage.
    """
    def __init__(self,
                 x: int,
                 y: int,
                 shooting_class,
                 width: int = 20,
                 height: int = 20,
                 speed: int = 10,
                 damage: int = 1,
                 window=None,
                 sprite_path: str = 'Sprites/Effects/Bullet.png'):
        """
        Initializes the projectile.
        :param x: x coordinate to spawn at.
        :param y: y coordinate to spawn at.
        :param shooting_class: class, that shot the projectile.
        :param width: sprite width.
        :param height: sprite height.
        :param speed: projectile speed.
        :param damage: damage to deal.
        :param window: window to render in.
        :param sprite_path: path to the player sprite.
        """
        self.x = x
        self.y = y
        self.speed = speed
        self.damage = damage
        self.width = width
        self.height = height
        self._shooting_class = shooting_class
        self.rect = None
        self._window = window
        self._is_destroyed = False
        self._collided_gameobject = None
        self._sprite_path = sprite_path

    def update(self):
        """ Called every tick """
        if not self._is_destroyed:
            self.draw(self._window)

            self.y -= self.speed

            if self.y < 0 or self.y > self._window.get_height():
                self._is_destroyed = True

            if self.is_collided(game.active_gameobjects):
                if isinstance(self._collided_gameobject, DamageReceiver):
                    if not isinstance(self._collided_gameobject, self._shooting_class):
                        if isinstance(self._collided_gameobject, Block):
                            self._collided_gameobject.damage_x = self.x
                            self._collided_gameobject.damage_y = self.y
                        self._collided_gameobject.receive_damage(self.damage)
                        explosion = Explosion(self.x - 3, self.y - 7, window=self._window)
                        game.add_gameobject(explosion)
                        self._is_destroyed = True

    def draw(self, window):
        """ Draw an object in a certain window """
        image = pygame.transform.scale(pygame.image.load(self._sprite_path), (self.width, self.height))
        self.rect = image.get_rect(left=self.x, top=self.y)
        window.blit(image, (self.x, self.y))
        if game.DEBUG_MODE:
            pygame.draw.rect(window, pygame.Color('green'), self.rect, 3)

    def get_rect(self):
        """ Returns the Rect of the image """
        return self.rect

    def is_collided(self, objects_list) -> bool:
        """
        Checks if the projectile has collided with anything.
        True, if collided
        False, otherwise
        :param objects_list: list of all gameobjects.
        :return: bool
        """
        is_collided = False
        for obj in objects_list:
            if not obj.get_rect() is None:
                if self.rect.colliderect(obj.get_rect()):
                    is_collided = True
                    self._collided_gameobject = obj
                    break
        return is_collided

    def is_destroyed(self):
        """ Checks if object is destroyed """
        return self._is_destroyed
