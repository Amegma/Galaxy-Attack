import pygame
import os

from utils.resource_path import resource_path
from config import config


class Assets:
    class text:
        def draw(text, font, color, pos, isCenterX=False, isCenterY=False):
            text_label = font.render(text, 1, color)

            if isCenterX:
                pos = (pos[0] - text_label.get_width()//2, pos[1])
            if isCenterY:
                pos = (pos[0], pos[1] - text_label.get_height()//2)

            config.CANVAS.blit(text_label, pos)

    class image:
        def load(root_path, image_path):
            return pygame.image.load(resource_path(os.path.join(root_path, image_path)))

        def scale(image, factor):
            return pygame.transform.scale(image, (image.get_width()*factor, image.get_height()*factor))

        def draw(image, pos, isCenterX=False, isCenterY=False):
            if isCenterX:
                pos = (pos[0] - image.get_width()//2, pos[1])
            if isCenterY:
                pos = (pos[0], pos[1] - image.get_height()//2)

            config.CANVAS.blit(image, pos)

    class sound:
        def load(root_path, sound_path):
            return pygame.mixer.Sound(resource_path(os.path.join(root_path, sound_path)))

    class font:
        def load(root_path, font_path):
            return resource_path(os.path.join(root_path, font_path))
