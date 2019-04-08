import pygame


class Gameobject(object):

    def get_rect(self):
        """ Returns the Rect of the image """
        pass

    def draw(self, window, sprite_path: str = 'Sprites/Player/Player.png'):
        """ Draw an object in a certain window """
        pass

    def update(self):
        """ Called every tick """
        pass

    def is_destroyed(self):
        """ Checks if object is destroyed """
        pass


