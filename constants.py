import pygame
import os

from utils.resource_path import resource_path
# from screens.background import slow_bg_obj

# ROOT VARS
TITLE = 'SPACE INVADERS'
WIDTH = 750
HEIGHT = 750

# Canvas Dimensions
CANVAS = pygame.display.set_mode((WIDTH, HEIGHT))

screen_rect = CANVAS.get_rect()
center_x = screen_rect.centerx
center_y = screen_rect.centery

# Load Background Image
backgroundImage = pygame.image.load(resource_path(os.path.join(
    'assets', 'graphics', 'background-black.png')))

# Set Background Dimensions
BG = pygame.transform.scale(backgroundImage, (WIDTH, HEIGHT))

FPS = 60
framespersec = pygame.time.Clock()

score_list = []

# list of all game sounds
soundList = []

# Initialize Sound System
pygame.mixer.init()

# PATH VARS
FONT_PATH = os.path.join('assets', 'fonts')
EXPLOSION_PATH = os.path.join('assets', 'graphics', 'explosion')

# FONT VARS
edit_undo_font = resource_path(os.path.join(FONT_PATH, 'edit_undo.ttf'))
neue_font = resource_path(os.path.join(FONT_PATH, 'neue.ttf'))

# Load Enemy Ships
EASY_SPACE_SHIP = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'easy.png')))
MEDIUM_SPACE_SHIP = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'medium.png')))
HARD_SPACE_SHIP = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'hard.png')))
BOSS_SHIP = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'boss.png')))

# Load Player
PLAYER_SPACE_SHIP = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'retro-spaceship.png')))
PLAYER_LASER = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'pixel_laser_cosmic.png')))

# Load Lasers
RED_LASER = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'pixel_laser_red.png')))
BLUE_LASER = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'pixel_laser_blue.png')))
GREEN_LASER = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'pixel_laser_green.png')))
FLAME_LASER = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'pixel_laser_flame.png')))

# Load audio image
VOL_ICON = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'audio.png')))
MUTE_ICON = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'mute.png')))

# Load Controls Image
CONTROL_IMAGE = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'joystick.png')))
TROPHY_IMAGE = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'trophy.png')))
CHARACTERS_IMAGE = pygame.transform.scale(MEDIUM_SPACE_SHIP, (60, 60))
CHARACTERS_IMAGE_2 = pygame.transform.scale(HARD_SPACE_SHIP, (60, 66*0.75))

GO_BACK_IMAGE = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'back2.png')))
# GO_BACK_IMAGE = pygame.transform.scale()
GO_BACK_IMAGE = pygame.transform.scale(GO_BACK_IMAGE, (34*2.4, 19*2.4))

# Load Hearts
HEART_IMAGE = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'heart.png')))

# load music
GAME_MUSIC_PATH = resource_path(os.path.join('assets', 'sounds', 'ingame.wav'))
MENU_MUSIC_PATH = resource_path(os.path.join('assets', 'sounds', 'menu.wav'))

# SFX VARS
PLAYER_LASER_SOUND = pygame.mixer.Sound(resource_path(
    os.path.join('assets', 'sounds', 'ownlaser.wav')))
ENEMY_LASER_SOUND = pygame.mixer.Sound(resource_path(
    os.path.join('assets', 'sounds', 'enemylaser.wav')))
EXPLODE_SOUND = pygame.mixer.Sound(resource_path(
    os.path.join('assets', 'sounds', 'explode.wav')))
LASER_HIT_SOUND = pygame.mixer.Sound(resource_path(
    os.path.join('assets', 'sounds', 'laser_hit.wav')))

# adding sounds to the list
soundList.append(PLAYER_LASER_SOUND)
soundList.append(ENEMY_LASER_SOUND)
soundList.append(EXPLODE_SOUND)
soundList.append(LASER_HIT_SOUND)
