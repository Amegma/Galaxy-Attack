import os
import pygame

from config import config
from constants import Colors, Font
from utils.outline_image import outline_image
from utils.draw import draw_text


class IconButton:
    def __init__(self, image, pos, subtitle=''):
        self.image = image
        self.pos = pos
        self.new_pos = (pos[0] - image.get_width()//2,
                        pos[1] - image.get_height()//2)
        self.outline = False
        self.subtitle = subtitle
        self.rect = pygame.Rect(
            self.new_pos[0], self.new_pos[1], self.image.get_width(), self.image.get_height())

    def draw(self):
        if self.outline == True:
            outline_image(self.image, self.new_pos)

        config.CANVAS.blit(self.image, self.rect)

        subtitle_font = pygame.font.Font(Font.neue_font, 20)

        if self.subtitle != '':
            draw_text(self.subtitle, subtitle_font, Colors.WHITE,
                      (self.pos[0], self.pos[1] + 35), True)

    def isOver(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
