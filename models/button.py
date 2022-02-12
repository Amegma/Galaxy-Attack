import pygame

from utils.assets import Assets
from config import config
from constants import Font, Colors


class Button:
    def __init__(self, color, outline_color, text=''):
        self.color = color
        self.outline_color = outline_color
        self.text = text
        self.outline = False
        self.rect = pygame.Rect(0, 0, 0, 0)

    def draw(self, pos, size):
        self.default_outline = pygame.Rect(
            pos[0]-5, pos[1]-5, size[0]+10, size[1]+10)
        self.on_over_outline = pygame.Rect(
            pos[0]-6, pos[1]-6, size[0]+12, size[1]+12)
        self.rect = self.default_outline

        default_inner_rect = (pos[0], pos[1], size[0], size[1])
        onover_inner_rect = (pos[0]+1, pos[1]+1, size[0]-2, size[1]-2)
        inner_rect = onover_inner_rect if self.outline == True else default_inner_rect

        pygame.draw.rect(config.CANVAS, self.outline_color,
                         self.on_over_outline if self.outline == True else self.default_outline, 0, 7)

        pygame.draw.rect(config.CANVAS, self.color, inner_rect, 0, 6)

        if self.text != '':
            font = pygame.font.Font(Font.neue_font, 40)
            Assets.text.draw(self.text, font, Colors.WHITE,
                             (pos[0] + size[0]/2, pos[1] + size[1]/2), True, True)

    def isOver(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
