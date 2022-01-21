import pygame
import os

from utils.resource_path import resource_path
from constants import Path


class Config:
    # ROOT VARS
    TITLE = 'SPACE INVADERS'
    WIDTH = 750
    HEIGHT = 750

    # Canvas Dimensions
    CANVAS = pygame.display.set_mode((WIDTH, HEIGHT))

    screen_rect = CANVAS.get_rect()
    center_x = screen_rect.centerx
    starting_x = 0
    ending_x = WIDTH

    center_y = screen_rect.centery
    starting_y = 0
    ending_y = HEIGHT

    # Load Background Image
    backgroundImage = pygame.image.load(resource_path(os.path.join(
        Path.GRAPHICS_PATH, 'background-black.png')))

    # Set Background Dimensions
    BG = pygame.transform.scale(backgroundImage, (WIDTH, HEIGHT))

    FPS = 60
    framespersec = pygame.time.Clock()
