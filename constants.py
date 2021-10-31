import pygame
import os

TITLE = 'SPACE INVADERS'
WIDTH = 750
HEIGHT = 750

FPS = 60
framespersec = pygame.time.Clock()

score_list = []

# list of all game sounds
soundList = []

# Initialize Sound System
pygame.mixer.init()

# font location
FONT_PATH = os.path.join('assets', 'fonts')

# Load Controls Image
startImage = pygame.image.load(os.path.join('assets', 'graphics', 'play.png'))
controlImage = pygame.image.load(os.path.join('assets', 'graphics', 'joystick.png'))
trophyImage = pygame.image.load(os.path.join('assets', 'graphics', 'trophy.png'))

# Load Hearts
heartImage = pygame.image.load(os.path.join('assets', 'graphics', 'heart.png'))

# Load Boss Ship
BOSS_SHIP = pygame.image.load(os.path.join('assets', 'graphics', 'boss.png'))

# Load Enemy Ships
EASY_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'graphics', 'easy.png'))
MEDIUM_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'graphics', 'medium.png'))
HARD_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'graphics', 'hard.png'))

# Load Player
PLAYER_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'graphics', 'retro-spaceship.png'))
PLAYER_LASER = pygame.image.load(os.path.join('assets', 'graphics', 'pixel_laser_cosmic.png'))

# Load Lasers
RED_LASER = pygame.image.load(os.path.join('assets', 'graphics', 'pixel_laser_red.png'))
BLUE_LASER = pygame.image.load(os.path.join('assets', 'graphics', 'pixel_laser_blue.png'))
GREEN_LASER = pygame.image.load(os.path.join('assets', 'graphics', 'pixel_laser_green.png'))
FLAME_LASER = pygame.image.load(os.path.join('assets', 'graphics', 'pixel_laser_flame.png'))
PLAYER_LASER_SOUND = pygame.mixer.Sound(os.path.join('assets', 'sounds', 'ownlaser.wav'))
ENEMY_LASER_SOUND = pygame.mixer.Sound(os.path.join('assets', 'sounds', 'enemylaser.wav'))

# load music
GAME_MUSIC_PATH = os.path.join('assets', 'sounds', 'ingame.wav')
MENU_MUSIC_PATH = os.path.join('assets', 'sounds', 'menu.wav')

# adding sounds to the list
soundList.append(PLAYER_LASER_SOUND)
soundList.append(ENEMY_LASER_SOUND)

# Load Background Image
backgroundImage = pygame.image.load(os.path.join('assets', 'graphics', 'background-black.png'))

# Set Background Dimensions
BG = pygame.transform.scale(backgroundImage, (WIDTH, HEIGHT))

# Canvas Dimensions
CANVAS = pygame.display.set_mode((WIDTH, HEIGHT))
