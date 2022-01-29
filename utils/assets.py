import pygame
import os

from utils.resource_path import resource_path


class Assets:
    class image:
        def load(root_path, image_path):
            return pygame.image.load(resource_path(os.path.join(root_path, image_path)))

        def scale(image, factor):
            return pygame.transform.scale(image, (image.get_width()*factor, image.get_height()*factor))
