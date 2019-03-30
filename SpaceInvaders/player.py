import pygame


class Player:
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

    def draw_player(self, window, sprite_path: str = 'Sprites/Player/Player.png'):
        """ Draw a player in a certain window """
        player_image = pygame.transform.scale(pygame.image.load(sprite_path), (self.width, self.height))
        window.blit(player_image, (self.x, self.y))

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

