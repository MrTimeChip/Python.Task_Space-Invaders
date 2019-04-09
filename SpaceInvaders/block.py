from gameobject import Gameobject
from damage_receiver import DamageReceiver
import pygame
import random
import game

damage_sprites ={
    '1': 'Sprites/Effects/Block_damage_1.png',
    '2': 'Sprites/Effects/Block_damage_2.png'
}


class Block(Gameobject, DamageReceiver):
    def __init__(self,
                 x: int,
                 y: int,
                 width: int = 60,
                 height: int = 50,
                 health: int = 10,
                 window=None,
                 sprite_path: str = 'Sprites/Player/Block.png'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self._window = window
        self._sprite_path = sprite_path
        self.health = health
        self.damage_x = 0
        self.damage_y = 0
        self._image = None
        self.rect = None

    def get_rect(self):
        return self.rect

    def draw(self, window):
        """ Draw an object in a certain window """
        image = pygame.transform.scale(pygame.image.load(self._sprite_path), (self.width, self.height))
        self._image = image
        self.rect = image.get_rect(left=self.x, top=self.y)
        window.blit(image, (self.x, self.y))

    def update(self):
        self.draw(self._window)

    def is_destroyed(self):
        return self.health <= 0

    def receive_damage(self, damage: int):
        sprite_number = random.randint(1, 2)
        game.add_gameobject(BlockDamage(self.damage_x,
                                        self.damage_y,
                                        self,
                                        sprite_path=damage_sprites[str(sprite_number)],
                                        window=self._window))


class BlockDamage(Gameobject):
    def __init__(self,
                 x: int,
                 y: int,
                 parent_block,
                 width: int = 30,
                 height: int = 30,
                 window=None,
                 sprite_path: str = 'Sprites/Effects/Block_damage_1.png'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self._window = window
        self._sprite_path = sprite_path
        self.parent_block = parent_block
        self.rect = None

    def get_rect(self):
        return self.rect

    def draw(self, window):
        """ Draw an object in a certain window """
        image = pygame.transform.scale(pygame.image.load(self._sprite_path), (self.width, self.height))
        self.rect = image.get_rect(left=self.x, top=self.y)
        window.blit(image, (self.x, self.y))

    def update(self):
        self.draw(self._window)

    def is_destroyed(self):
        """ Checks if object is destroyed """
        return self.parent_block.is_destroyed()
