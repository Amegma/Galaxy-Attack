import pygame
from screens.background import slow_bg_obj

from constants import Config
from utils.collide import collide


class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        # making laser's coordinates centered in the sprite
        x_offset, y_offset = self.img.get_size()
        window.blit(self.img, (Config.starting_x +
                    self.x-x_offset/2, self.y-y_offset/2))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not(height >= self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)

    def get_width(self):
        return self.img.get_width()

    def get_height(self):
        return self.img.get_height()
