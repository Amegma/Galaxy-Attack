import pygame
import os

from utils.resource_path import resource_path


class Config:
    def __init__(self):
        # ROOT VARS
        self.TITLE = 'GALAXY ATTACK'
        self.WIDTH = 750
        self.HEIGHT = 750

        # Load Background Image
        backgroundImage = pygame.image.load(resource_path(
            os.path.join('assets', 'graphics', 'background-black.png')))

        # Set Background Dimensions
        self.BG = pygame.transform.scale(
            backgroundImage, (self.WIDTH, self.HEIGHT))

        self.FPS = 60
        self.clock = pygame.time.Clock()

        self.CANVAS = pygame.display.set_mode(
            (self.WIDTH, self.HEIGHT), pygame.RESIZABLE)

        self.monitor_size = [pygame.display.Info().current_w,
                             pygame.display.Info().current_h]

        self.screen_rect = self.CANVAS.get_rect()
        self.center_x = self.screen_rect.centerx
        self.starting_x = 0
        self.ending_x = self.WIDTH

        self.center_y = self.screen_rect.centery
        self.starting_y = 0
        self.ending_y = self.HEIGHT

    def setCanvas(self, window):
        self.CANVAS = window
        self.screen_rect = self.CANVAS.get_rect()

    def update(self, width, height):
        self.center_x = width//2
        self.center_y = height//2
        self.ending_x = width
        self.ending_y = height


config = Config()
