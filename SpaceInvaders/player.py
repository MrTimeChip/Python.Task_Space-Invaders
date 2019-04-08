import pygame
import projectile
import game
from gameobject import Gameobject


class Player(Gameobject):
    _move_directions = ['LEFT', 'RIGHT', 'UP', 'DOWN']

    def __init__(self, x: int, y: int, width: int, height: int, speed: int = 5, window=None):
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
        self.speed = speed
        self._window = window
        self._window_width = window.get_width()
        self._window_height = window.get_height()
        self.rect = None
        self._start_tick_shooting = 300

    def update(self):
        """ Called every tick """
        self.draw(self._window)
        self.handle_keys()

    def draw(self, window, sprite_path: str = 'Sprites/Player/Player.png'):
        """ Draw an object in a certain window """
        image = pygame.transform.scale(pygame.image.load(sprite_path), (self.width, self.height))
        self.rect = image.get_rect(left=self.x, top=self.y)
        window.blit(image, (self.x, self.y))

    def get_rect(self):
        """ Returns the Rect of the image """
        return self.rect

#Оно мне надо?
    def update_window(self, window):
        """ Updates player window """
        self._window = window
        self._window_width = window.get_width()
        self._window_height = window.get_height()

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

    def shoot(self) -> projectile.Projectile:
        self._start_tick_shooting = pygame.time.get_ticks()
        bullet = projectile.Projectile(self.x + 9, self.y - 20, 10, 50, window=self._window)
        return bullet

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move('LEFT')
        if keys[pygame.K_RIGHT]:
            self.move('RIGHT')
        if keys[pygame.K_x]:
            if pygame.time.get_ticks() - self._start_tick_shooting > 500:
                game.add_gameobject(self.shoot())

    def is_destroyed(self):
        """ Checks if object is destroyed """
        return False

    def is_in_bounds(self, direction) -> bool:
        """ Checks if player is in bounds of display when moving """
        if direction not in self._move_directions:
            raise ValueError('Wrong direction!')
        else:
            if direction == 'LEFT':
                return self.x - self.speed > 0
            if direction == 'RIGHT':
                return self.x + self.speed < self._window_width - self.width
            if direction == 'UP':
                return self.y - self.speed > 0
            if direction == 'DOWN':
                return self.y + self.speed < self._window_height - self.height

