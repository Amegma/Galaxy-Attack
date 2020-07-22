import pygame
import os

TITLE = 'SPACE INVADERS'
WIDTH = 750
HEIGHT = 750

# Load Control Image
startImage = pygame.image.load(os.path.join('assets', 'play.png'))

# Load Control Image
controlImage = pygame.image.load(os.path.join('assets', 'joystick.png'))

# Load ScoreBoard Image
trophyImage = pygame.image.load(os.path.join('assets', 'trophy.png'))

# Load Boss Ship
BOSS_SHIP = pygame.image.load(os.path.join('assets', 'boss.png'))

# Load Enemy Ships
EASY_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'easy.png'))
MEDIUM_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'medium.png'))
HARD_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'hard.png'))

# Load Player
PLAYER_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'retro-spaceship.png'))
PLAYER_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_cosmic.png'))

# Load Lasers
RED_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_red.png'))
BLUE_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_blue.png'))
GREEN_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_green.png'))

# Load Background Image
backgroundImage = pygame.image.load(os.path.join('assets', 'background-black.png'))

# Set Background Dimensions
BG = pygame.transform.scale(backgroundImage, (WIDTH, HEIGHT))

# Canvas Dimensions
CANVAS = pygame.display.set_mode((WIDTH, HEIGHT))