import pygame

from constants import Colors, Font
from utils.outlineImage import outlineImage
from utils.assets import Assets


class IconButton:
    def __init__(self, image, subtitle=''):
        self.image = image
        self.outline = False
        self.subtitle = subtitle
        self.rect = pygame.Rect(
            0, 0, self.image.get_width(), self.image.get_height())

    def draw(self, pos, isCenterX=False, isCenterY=False):
        new_pos = pos
        if isCenterX == True:
            new_pos = (new_pos[0] - self.image.get_width()//2, new_pos[1])
        if isCenterY == True:
            new_pos = (new_pos[0], new_pos[1] - self.image.get_height()//2)

        if self.outline == True:
            outlineImage(self.image, new_pos)

        self.rect = pygame.Rect(
            new_pos[0], new_pos[1], self.image.get_width(), self.image.get_height())

        Assets.image.draw(self.image, self.rect)

        subtitle_font = pygame.font.Font(Font.neue_font, 20)

        if self.subtitle != '':
            Assets.text.draw(self.subtitle, subtitle_font, Colors.WHITE,
                             (pos[0], pos[1] + 35), True)

    def isOver(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
