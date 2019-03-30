import random
import pygame

stars = []


def setup_stars(stars_amount, stars_size, window):
    """
    Setting up stars.

    stars_amount = amount of stars
    stars_size = size of star (range from star_size // 3 to star_size)
    window = window to draw in
    """
    window_width = window.get_width()
    window_height = window.get_height()
    for i in range(stars_amount):
        x = random.randrange(0, window_width)
        y = random.randrange(0, window_height)
        color = random.randrange(120, 230)
        size = random.randrange(stars_size // 3, stars_size)
        stars.append([x, y, color, size])


def draw_stars(stars_speed, window):
    """ Drawing stars to the window """
    window_width = window.get_width()
    window_height = window.get_height()
    for star in stars:
        star[1] += stars_speed

        pygame.draw.rect(window, (star[2], star[2], star[2]), (star[0], star[1], star[3], star[3]))

        if star[1] > window_height:
            star[1] = random.randrange(-50, -5)
            star[0] = random.randrange(0, window_width)
