import os
import pygame

from constants import FONT_PATH


class Button:
    def __init__(self, color, outline_color, outline, pos, size, text=''):
        self.color = color
        self.outline_color = outline_color
        self.pos = pos  # pos is a tuple (x, y)
        self.size = size  # size is a tuple (width, height)
        self.text = text
        self.outline = outline
        self.default_outline = (
            self.pos[0]-5, self.pos[1]-5, self.size[0]+10, self.size[1]+10)
        self.on_over_outline = (
            self.pos[0]-6, self.pos[1]-6, self.size[0]+12, self.size[1]+12)

    def draw(self, win):
        pygame.draw.rect(win, self.outline_color, self.on_over_outline if self.outline ==
                         "onover" else self.default_outline, 0, 8)

        pygame.draw.rect(win, self.color, (self.pos[0], self.pos[1],
                         self.size[0], self.size[1]), 0, 7)

        if self.text != '':
            font = pygame.font.Font(os.path.join(
                FONT_PATH, 'neue.ttf'), 40)
            text = font.render(self.text, 1, (255, 255, 255))
            win.blit(text, (self.pos[0] + (self.size[0]/2 - text.get_width()/2),
                     self.pos[1] + (self.size[1]/2 - text.get_height()/2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.pos[0] and pos[0] < self.pos[1] + self.size[0]:
            if pos[1] > self.pos[1] and pos[1] < self.pos[1] + self.size[1]:
                return True

        return False
