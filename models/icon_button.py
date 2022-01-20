import os
import pygame

from constants import Config
from utils.outline_image import outline_image


class IconButton:
    def __init__(self, image, pos, outline="default"):
        self.image = image
        self.pos = pos
        self.outline = outline
        self.rect = pygame.Rect(
            self.pos[0], self.pos[1], self.image.get_width(), self.image.get_height())

    def draw(self):
        if self.outline == "onover":
            outline_image(self.image, self.pos)

        Config.CANVAS.blit(self.image, self.rect)

    def isOver(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
