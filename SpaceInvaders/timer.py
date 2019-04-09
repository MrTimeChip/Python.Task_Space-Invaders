import pygame


class Timer:
    def __init__(self, time: int = 0):
        self.time = time
        self.start_tick = pygame.time.get_ticks()
        self._started = False

    def start_timer(self, time: int):
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
