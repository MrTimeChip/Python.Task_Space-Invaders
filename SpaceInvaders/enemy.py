from gameobject import Gameobject
from damage_receiver import DamageReceiver
from projectile import Projectile
import game
import pygame
import random
from timer import Timer


class Enemy(Gameobject, DamageReceiver):
    def __init__(self,
                 x: int,
                 y: int,
                 width: int = 25,
                 height: int = 25,
                 health: int = 1,
                 speed: int = 5,
                 score: int = 10,
                 window=None,
                 sprite_path: str = 'Sprites/Enemies/Enemy_3.png'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self._window = window
        self.speed = speed
        self.rect = None
        self.score = score
        self._sprite_path = sprite_path
        self._sprite_path_second = sprite_path[:-4] + '_2.png'
        self._first_sprite = True
        self._timer = Timer()
        self._move_timer = Timer()
        self._move_step_timer = Timer()
        self._move_multiplier = 1
        self._move_step_delay = 1300

    def update(self):
        """ Called every tick """
        self.draw(self._window)
        if self._move_step_timer.start_timer(self._move_step_delay + random.randint(50, 100)):
            self._move_step_delay -= 10
            self.move()
        if self._timer.start_timer(1000):
            if random.random() + game.score / 800 > 0.95:
                self.shoot()

    def draw(self, window):
        """ Draw an object in a certain window """
        image = pygame.transform.scale(pygame.image.load(self._sprite_path), (self.width, self.height))
        self.rect = image.get_rect(left=self.x, top=self.y)
        window.blit(image, (self.x, self.y))
        if game.DEBUG_MODE:
            pygame.draw.rect(window, pygame.Color('red'), self.rect, 3)

    def move(self):
        self.x += self.speed * self._move_multiplier
        self.y += self.speed//5
        self.change_sprite()
        if self._move_timer.start_timer(1000):
            self.change_sprite()
            self._move_multiplier *= -1
            self.y += self.speed
            self.speed += 2

    def get_rect(self):
        """ Returns the Rect of the image """
        return self.rect

    def receive_damage(self, damage: int):
        self.health -= damage

    def shoot(self):
        """ Shoots a projectile """
        bullet = Projectile(self.x + self.width//2 - 9, self.y + self.height, -10, Enemy, window=self._window)
        self.change_sprite()
        game.add_gameobject(bullet)

    def change_sprite(self):
        """ Changes current sprite to second """
        if not self._first_sprite:
            temp_path = self._sprite_path
            self._sprite_path = self._sprite_path_second
            self._sprite_path_second = temp_path
            self._first_sprite = True
        else:
            self._first_sprite = False

    def is_destroyed(self):
        """ Checks if object is destroyed """
        if self.health <= 0:
            game.score += self.score
            return True
        return False
