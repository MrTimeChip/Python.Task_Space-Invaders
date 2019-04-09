import pygame


class Timer:
    """Simple timer class"""
    def __init__(self, time: int = 0):
        """
        Initializes timer.
        :param time: time in ms.
        """
        self.time = time
        self.start_tick = pygame.time.get_ticks()
        self._started = False

    def start_timer(self, time: int) -> bool:
        """
        Starts timer, and checks if it's done.
        True, if passed more, than time variable.
        False, otherwise.
        :param time: time in ms.
        :return: bool
        """
        if self._started:
            if pygame.time.get_ticks() - self.start_tick >= time:
                self._started = False
                return True
            else:
                return False
        else:
            self.time = time
            self.start_tick = pygame.time.get_ticks()
            self._started = True
        return False
