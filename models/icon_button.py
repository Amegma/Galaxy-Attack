import os
import pygame

from constants import CANVAS


class IconButton:
    def __init__(self, image, pos):
        self.image = image
        self.pos = pos

    def draw(self):
        singleplayer_position = pygame.Rect(self.pos[0], self.pos[1], 100, 100)

        CANVAS.blit(self.image, singleplayer_position)
        # print(self.image.get_rect())
        if singleplayer_position.collidepoint(pygame.mouse.get_pos()):
            print("Working...")
