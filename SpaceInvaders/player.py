import pygame
import projectile
import game
from damage_receiver import DamageReceiver
from gameobject import Gameobject
from timer import Timer


class Player(Gameobject, DamageReceiver):
    _move_directions = ['LEFT', 'RIGHT', 'UP', 'DOWN']

    def __init__(self,
                 x: int,
                 y: int,
                 width: int,
                 height: int,
                 health: int = 3,
                 speed: int = 5,
                 window=None,
                 sprite_path: str = 'Sprites/Player/Player.png'):
        """
         Creating a new player instance.

         x = x position
         y = y position
         width = width of the player
         height = height of the player
         speed = speed of the player (5 by default)
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.speed = speed
        self._window = window
        self.rect = None
        self._timer = Timer()
        self._sprite_path = sprite_path

    def update(self):
        """ Called every tick """
        self.draw(self._window)
        self.handle_keys()

    def draw(self, window):
        """ Draw an object in a certain window """
        image = pygame.transform.scale(pygame.image.load(self._sprite_path), (self.width, self.height))
        self.rect = image.get_rect(left=self.x, top=self.y)
        window.blit(image, (self.x, self.y))
        if game.DEBUG_MODE:
            pygame.draw.rect(window, pygame.Color('white'), self.rect, 3)

    def get_rect(self):
        """ Returns the Rect of the image """
        return self.rect

    def move(self, direction):
        """ Moves player in a certain direction (using speed) """
        if direction not in self._move_directions:
            raise ValueError('Wrong direction!')
        else:
            in_bounds = self.is_in_bounds(direction)
            if direction == 'LEFT' and in_bounds:
                self.x -= self.speed
            if direction == 'RIGHT' and in_bounds:
                self.x += self.speed
            if direction == 'UP' and in_bounds:
                self.y -= self.speed
            if direction == 'DOWN' and in_bounds:
                self.y += self.speed

    def shoot(self):
        """ Shoots a projectile """
        bullet = projectile.Projectile(self.x + self.width//2 - 5, self.y - self.height, 10, Player, window=self._window)
        game.add_gameobject(bullet)

    def receive_damage(self, damage: int):
        self.health -= damage

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move('LEFT')
        if keys[pygame.K_RIGHT]:
            self.move('RIGHT')
        if keys[pygame.K_x]:
            if self._timer.start_timer(500):
                self.shoot()

    def is_destroyed(self):
        """ Checks if object is destroyed """
        if self.health <= 0:
            game.GAME_OVER = True
            return True
        return False

    def is_in_bounds(self, direction) -> bool:
        """ Checks if player is in bounds of display when moving """
        if direction not in self._move_directions:
            raise ValueError('Wrong direction!')
        else:
            if direction == 'LEFT':
                return self.x - self.speed > 0
            if direction == 'RIGHT':
                return self.x + self.speed < self._window.get_width() - self.width
            if direction == 'UP':
                return self.y - self.speed > 0
            if direction == 'DOWN':
                return self.y + self.speed < self._window.get_height() - self.height
