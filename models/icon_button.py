import os
import pygame

from constants import CANVAS


class IconButton:
    def __init__(self, image, pos):
        self.image = image
        self.pos = pos
        self.rect = pygame.Rect(
            self.pos[0], self.pos[1], self.image.get_width(), self.image.get_height())

    def draw(self):
        CANVAS.blit(self.image, self.rect)

    def isOver(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
