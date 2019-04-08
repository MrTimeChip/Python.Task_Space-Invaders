import pygame
from enemy import Enemy
from explosion import Explosion
from game import current_drawable_objects, add_gameobject
from gameobject import Gameobject


class Projectile(Gameobject):
    def __init__(self,
                 x: int,
                 y: int,
                 speed: int,
                 damage: int = 10,
                 width: int = 10,
                 height: int = 10,
                 window=None):
        self.x = x
        self.y = y
        self.speed = speed
        self.damage = damage
        self.width = width
        self.height = height
        self.rect = None
        self._window = window
        self._is_destroyed = False
        self._collided_gameobject = None

    def update(self):
        """ Called every tick """
        if not self._is_destroyed:
            self.draw(self._window)

            self.y -= self.speed

            if self.y < 0 or self.y > 500:
                self._is_destroyed = True

            if self.is_collided(current_drawable_objects):
                if isinstance(self._collided_gameobject, Enemy):
                    self._collided_gameobject.receive_damage(self.damage)
                    explosion = Explosion(self.x - 3, self.y - 7, window=self._window)
                    add_gameobject(explosion)
                    self._is_destroyed = True

    def draw(self, window, sprite_path: str = 'Sprites/Effects/Bullet.png'):
        """ Draw an object in a certain window """
        image = pygame.transform.scale(pygame.image.load(sprite_path), (self.width, self.height))
        self.rect = image.get_rect(left=self.x, top=self.y)
        window.blit(image, (self.x, self.y))

    def get_rect(self):
        """ Returns the Rect of the image """
        return self.rect

    def is_collided(self, objects_list):
        """ Check if collided with any gameobject """
        is_collided = False
        for obj in objects_list:
            if not obj.get_rect() == None:
                if self.rect.colliderect(obj.get_rect()):
                    is_collided = True
                    self._collided_gameobject = obj
                    break
        return is_collided

    def is_destroyed(self):
        """ Checks if object is destroyed """
        return self._is_destroyed

