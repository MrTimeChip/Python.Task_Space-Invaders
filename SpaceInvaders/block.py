from gameobject import Gameobject
from damage_receiver import DamageReceiver
import pygame
import random
import game

damage_sprites = {
    '1': 'Sprites/Effects/Block_damage_1.png',
    '2': 'Sprites/Effects/Block_damage_2.png'
}


class Block(Gameobject, DamageReceiver):
    """
    Block clas. The only defence for the player.
    """
    def __init__(self,
                 x: int,
                 y: int,
                 width: int = 60,
                 height: int = 50,
                 health: int = 10,
                 window=None,
                 sprite_path: str = 'Sprites/Player/Block.png'):
        """
        Initializes the block.
        :param x: x coordinate to spawn at.
        :param y: y coordinate to spawn at.
        :param width: sprite width.
        :param height: sprite height.
        :param health: block health.
        :param window: window to render in.
        :param sprite_path: path to the player sprite.
        """
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
        """ Returns the Rect of the image """
        return self.rect

    def draw(self, window):
        """ Draw an object in a certain window """
        image = pygame.transform.scale(pygame.image.load(self._sprite_path),
                                       (self.width, self.height))
        self._image = image
        self.rect = image.get_rect(left=self.x, top=self.y)
        window.blit(image, (self.x, self.y))
        if game.DEBUG_MODE:
            pygame.draw.rect(window, pygame.Color('yellow'), self.rect, 3)

    def update(self):
        """ Called every tick """
        self.draw(self._window)

    def is_destroyed(self):
        """
        Checks if block is destroyed.
        True, if health <= 0
        False, otherwise
        :return:
        """
        return self.health <= 0

    def receive_damage(self, damage: int):
        """
        Receives damage.
        :param damage: damage to substract from health.
        """
        num = random.randint(1, 2)
        game.add_gameobject(BlockDamage(self.damage_x,
                                        self.damage_y,
                                        self,
                                        sprite_path=damage_sprites[str(num)],
                                        window=self._window))
        self.health -= damage


class BlockDamage(Gameobject):
    """A block damage object, that looks cool. (No)"""
    def __init__(self,
                 x: int,
                 y: int,
                 parent_block,
                 width: int = 30,
                 height: int = 30,
                 window=None,
                 sprite_path: str = 'Sprites/Effects/Block_damage_1.png'):
        """
        Initializes the block damage.
        :param x: x coordinate to spawn at.
        :param y: y coordinate to spawn at.
        :param parent_block: block, from which it was spawned.
        :param width: sprite width.
        :param height: sprite height.
        :param window: window to render in.
        :param sprite_path: path to the block damage sprite.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self._window = window
        self._sprite_path = sprite_path
        self.parent_block = parent_block
        self.rect = None

    def get_rect(self):
        """ Returns the Rect of the image """
        return self.rect

    def draw(self, window):
        """ Draw an object in a certain window """
        image = pygame.transform.scale(pygame.image.load(self._sprite_path),
                                       (self.width, self.height))
        self.rect = image.get_rect(left=self.x, top=self.y)
        window.blit(image, (self.x, self.y))
        if game.DEBUG_MODE:
            pygame.draw.rect(window, pygame.Color('blue'), self.rect, 3)

    def update(self):
        """Called every tick"""
        self.draw(self._window)

    def is_destroyed(self):
        """
        Checks if the block damage is destroyed.
        True, if parent block is destroyed
        False, otherwise
        :return:
        """
        return self.parent_block.is_destroyed()
