import pygame
import os
import ctypes

from utils.resource_path import resource_path


class Config:
    def __init__(self):
        # ROOT VARS
        self.TITLE = 'GALAXY ATTACK'
        self.WIDTH = 750
        self.HEIGHT = 750

        # Load Background Image
        self.backgroundImage = pygame.image.load(resource_path(
            os.path.join('assets', 'graphics', 'background-black-wide.png')))

        self.CANVAS = pygame.display.set_mode(
            (self.WIDTH, self.HEIGHT), pygame.RESIZABLE)

        self.monitor_size = pygame.display.Info().current_w, pygame.display.Info().current_h

        # Set Background Dimensions
        self.BG = pygame.transform.scale(
            self.backgroundImage, self.monitor_size)

        self.FPS = 60
        self.clock = pygame.time.Clock()

        
        self.screen_rect = self.CANVAS.get_rect()
        self.center_x = self.screen_rect.centerx
        self.starting_x = 0
        self.ending_x = self.WIDTH

        self.center_y = self.screen_rect.centery
        self.starting_y = 0
        self.ending_y = self.HEIGHT

    def update(self, width, height):
        self.CANVAS = pygame.display.set_mode(
            (width, height), pygame.RESIZABLE)
        self.WIDTH = width
        self.HEIGHT = height
        self.center_x = width//2
        self.center_y = height//2
        self.ending_x = width
        self.ending_y = height
        self.BG = pygame.transform.scale(
            self.backgroundImage, (self.WIDTH, self.HEIGHT))


config = Config()
