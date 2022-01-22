import pygame
import os

from utils.resource_path import resource_path

score_list = []

# list of all game sounds
soundList = []

# Initialize Sound System
pygame.mixer.init()


class Path:
    # PATH VARS
    FONT_PATH = os.path.join('assets', 'fonts')
    EXPLOSION_PATH = os.path.join('assets', 'graphics', 'explosion')
    GRAPHICS_PATH = os.path.join('assets', 'graphics')
    SOUND_PATH = os.path.join('assets', 'sounds')

    # load music
    GAME_MUSIC_PATH = resource_path(os.path.join(SOUND_PATH, 'ingame.wav'))
    MENU_MUSIC_PATH = resource_path(os.path.join(SOUND_PATH, 'menu.wav'))


class Font:
    # FONT VARS
    edit_undo_font = resource_path(
        os.path.join(Path.FONT_PATH, 'edit_undo.ttf'))
    neue_font = resource_path(os.path.join(Path.FONT_PATH, 'neue.ttf'))


class Image:
    # Load Enemy Ships
    EASY_SPACE_SHIP = pygame.image.load(resource_path(
        os.path.join(Path.GRAPHICS_PATH, 'easy.png')))
    MEDIUM_SPACE_SHIP = pygame.image.load(resource_path(
        os.path.join(Path.GRAPHICS_PATH, 'medium.png')))
    HARD_SPACE_SHIP = pygame.image.load(resource_path(
        os.path.join(Path.GRAPHICS_PATH, 'hard.png')))
    BOSS_SHIP = pygame.image.load(resource_path(
        os.path.join(Path.GRAPHICS_PATH, 'boss.png')))

    UFO_SPACE_SHIP = pygame.image.load(resource_path(
        os.path.join(Path.GRAPHICS_PATH, 'ufo.png')))
    UFO_SPACE_SHIP = pygame.transform.scale(
        UFO_SPACE_SHIP, (UFO_SPACE_SHIP.get_width()/7, UFO_SPACE_SHIP.get_height()/7))

    # Load Player
    PLAYER_SPACE_SHIP = pygame.image.load(resource_path(
        os.path.join(Path.GRAPHICS_PATH, 'retro-spaceship.png')))
    PLAYER_LASER = pygame.image.load(resource_path(
        os.path.join(Path.GRAPHICS_PATH, 'pixel_laser_cosmic.png')))

    # Load Lasers
    RED_LASER = pygame.image.load(resource_path(
        os.path.join(Path.GRAPHICS_PATH, 'pixel_laser_red.png')))
    BLUE_LASER = pygame.image.load(resource_path(
        os.path.join(Path.GRAPHICS_PATH, 'pixel_laser_blue.png')))
    GREEN_LASER = pygame.image.load(resource_path(
        os.path.join(Path.GRAPHICS_PATH, 'pixel_laser_green.png')))
    FLAME_LASER = pygame.image.load(resource_path(
        os.path.join(Path.GRAPHICS_PATH, 'pixel_laser_flame.png')))

    # Load audio image
    VOL_ICON = pygame.image.load(resource_path(
        os.path.join(Path.GRAPHICS_PATH, 'audio.png')))
    MUTE_ICON = pygame.image.load(resource_path(
        os.path.join(Path.GRAPHICS_PATH, 'mute.png')))

    DEMON_ICON = pygame.image.load(resource_path(
        os.path.join(Path.GRAPHICS_PATH, 'demon.png')))
    DEMON_ICON = pygame.transform.scale(
        DEMON_ICON, (DEMON_ICON.get_width()/11, DEMON_ICON.get_height()/11))

    # Load Controls Image
    CONTROL_IMAGE = pygame.image.load(resource_path(
        os.path.join(Path.GRAPHICS_PATH, 'joystick.png')))
    TROPHY_IMAGE = pygame.image.load(resource_path(
        os.path.join(Path.GRAPHICS_PATH, 'trophy.png')))
    CHARACTERS_IMAGE = pygame.transform.scale(MEDIUM_SPACE_SHIP, (60, 60))
    CHARACTERS_IMAGE_2 = pygame.transform.scale(HARD_SPACE_SHIP, (60, 66*0.75))

    GO_BACK_IMAGE = pygame.image.load(resource_path(
        os.path.join(Path.GRAPHICS_PATH, 'back2.png')))
    # GO_BACK_IMAGE = pygame.transform.scale()
    GO_BACK_IMAGE = pygame.transform.scale(GO_BACK_IMAGE, (34*2.4, 19*2.4))

    # Load Hearts
    HEART_IMAGE = pygame.image.load(resource_path(
        os.path.join(Path.GRAPHICS_PATH, 'heart.png')))


# SFX VARS
PLAYER_LASER_SOUND = pygame.mixer.Sound(resource_path(
    os.path.join(Path.SOUND_PATH, 'ownlaser.wav')))
ENEMY_LASER_SOUND = pygame.mixer.Sound(resource_path(
    os.path.join(Path.SOUND_PATH, 'enemylaser.wav')))
EXPLODE_SOUND = pygame.mixer.Sound(resource_path(
    os.path.join(Path.SOUND_PATH, 'explode.wav')))
LASER_HIT_SOUND = pygame.mixer.Sound(resource_path(
    os.path.join(Path.SOUND_PATH, 'laser_hit.wav')))

# adding sounds to the list
soundList.append(PLAYER_LASER_SOUND)
soundList.append(ENEMY_LASER_SOUND)
soundList.append(EXPLODE_SOUND)
soundList.append(LASER_HIT_SOUND)
