import enemy
import game
from player import Player
from block import Block


enemies_sprite_paths ={
    '1': 'Sprites/Enemies/Enemy_1.png',
    '2': 'Sprites/Enemies/Enemy_2.png',
    '3': 'Sprites/Enemies/Enemy_3.png'
}


class Level:
    def __init__(self, name: str, level_str: str, next_level_name: str = None, shift_x: int = 0, shift_y: int = 0):
        self.name = name
        self.level_str = level_str
        self.next_level_name = next_level_name
        self.shift_x = shift_x
        self.shift_y = shift_y


def load_level(level_name: str, window):
    screen_width = window.get_width()
    screen_height = window.get_height()
    game.enemy_count = 0
    level = levels[level_name]
    level_str = level.level_str
    row = 1
    column = 1
    for i in range(2):
        game.add_gameobject(Block(screen_width//2 - 140 * (i + 1) - 30, screen_height - 130, window=window))
        game.add_gameobject(Block(screen_width // 2 + 140 * (i + 1) - 30, screen_height - 130, window=window))
    for char in level_str:
        if char in enemies_sprite_paths:
            column += 1
            path = enemies_sprite_paths[char]
            game.enemy_count += 1
            game.add_gameobject(enemy.Enemy(level.shift_x + (screen_width//5 + 60 * column),
                                            level.shift_y + screen_height//5 + 60 * row,
                                            50,
                                            50,
                                            window=window,
                                            sprite_path=path))
        elif char == 'n':
            row += 1
            column = 1
        elif char == '0':
            column += 1
    game.player = Player(screen_width//2 - 30, screen_height - 40, 60, 40, window=window)
    game.spawn_player()


levels = {
    'first': Level('first', '3333n2222n1111', 'second', shift_y=-100),
    'second': Level('second', '33333n02220n11111', 'third', -25, -100),
    'third': Level('third', '0303030n3030303n0202020n1010101', 'end', -100, -100)
}
