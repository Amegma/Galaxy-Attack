import pygame
import os

from utils.resource_path import resource_path
from constants import Path


class Config:
    def __init__(self):
        # ROOT VARS
        self.TITLE = 'GALAXY ATTACK'
        self.WIDTH = 750
        self.HEIGHT = 750

        # Load Background Image
        self.backgroundImage = pygame.image.load(resource_path(os.path.join(
            Path.GRAPHICS_PATH, 'background-black.png')))

        # Set Background Dimensions
        self.BG = pygame.transform.scale(
            self.backgroundImage, (self.WIDTH, self.HEIGHT))

        self.FPS = 60
        self.framespersec = pygame.time.Clock()

        self.CANVAS = pygame.display.set_mode(
            (self.WIDTH, self.HEIGHT), pygame.RESIZABLE)

        self.screen_rect = self.CANVAS.get_rect()
        self.center_x = self.screen_rect.centerx
        self.starting_x = 0
        self.ending_x = self.WIDTH

        self.center_y = self.screen_rect.centery
        self.starting_y = 0
        self.ending_y = self.HEIGHT


config = Config()