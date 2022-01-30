import pygame

from utils.assets import Assets
from config import config
from constants import Font, Colors


class Button:
    def __init__(self, color, outline_color, pos, size, text=''):
        self.color = color
        self.outline_color = outline_color
        self.pos = pos  # pos is a tuple (x, y)
        self.size = size  # size is a tuple (width, height)
        self.text = text
        self.outline = False
        self.default_outline = pygame.Rect(
            self.pos[0]-5, self.pos[1]-5, self.size[0]+10, self.size[1]+10)
        self.on_over_outline = pygame.Rect(
            self.pos[0]-6, self.pos[1]-6, self.size[0]+12, self.size[1]+12)
        self.rect = self.default_outline

    def draw(self):
        default_inner_rect = (
            self.pos[0], self.pos[1], self.size[0], self.size[1])
        onover_inner_rect = (
            self.pos[0]+1, self.pos[1]+1, self.size[0]-2, self.size[1]-2)
        inner_rect = onover_inner_rect if self.outline == True else default_inner_rect

        pygame.draw.rect(config.CANVAS, self.outline_color, self.on_over_outline if self.outline ==
                         True else self.default_outline, 0, 7)

        pygame.draw.rect(config.CANVAS, self.color, inner_rect, 0, 6)

        if self.text != '':
            font = pygame.font.Font(Font.neue_font, 40)
            Assets.text.draw(self.text, font, Colors.WHITE,
                      (self.pos[0] + self.size[0]/2, self.pos[1] + self.size[1]/2), True, True)

    def isOver(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
