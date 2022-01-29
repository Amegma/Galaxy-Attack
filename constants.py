import pygame
import os

from utils.resource_path import resource_path
from utils.assets import Assets

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
    karmatic_arcade_font = resource_path(
        os.path.join(Path.FONT_PATH, 'karmatic_arcade.ttf'))


class Image:
    TITLE_LOGO = Assets.image.load(Path.GRAPHICS_PATH, 'title_logo.png')
    TITLE_LOGO = Assets.image.scale(TITLE_LOGO, 2/7)

    # Load Enemy Ships
    EASY_SPACE_SHIP = Assets.image.load(Path.GRAPHICS_PATH, 'easy.png')
    MEDIUM_SPACE_SHIP = Assets.image.load(Path.GRAPHICS_PATH, 'medium.png')
    HARD_SPACE_SHIP = Assets.image.load(Path.GRAPHICS_PATH, 'hard.png')
    BOSS_SHIP = Assets.image.load(Path.GRAPHICS_PATH, 'boss.png')

    UFO_SPACE_SHIP = Assets.image.load(Path.GRAPHICS_PATH, 'ufo.png')
    UFO_SPACE_SHIP = Assets.image.scale(UFO_SPACE_SHIP, 1/7)

    # Load Player
    PLAYER_SPACE_SHIP = Assets.image.load(
        Path.GRAPHICS_PATH, 'retro-spaceship.png')
    PLAYER_LASER = Assets.image.load(
        Path.GRAPHICS_PATH, 'pixel_laser_cosmic.png')

    # Load Lasers
    RED_LASER = Assets.image.load(Path.GRAPHICS_PATH, 'pixel_laser_red.png')
    BLUE_LASER = Assets.image.load(Path.GRAPHICS_PATH, 'pixel_laser_blue.png')
    GREEN_LASER = Assets.image.load(
        Path.GRAPHICS_PATH, 'pixel_laser_green.png')
    FLAME_LASER = Assets.image.load(
        Path.GRAPHICS_PATH, 'pixel_laser_flame.png')

    # Load audio image
    VOL_ICON = Assets.image.load(Path.GRAPHICS_PATH, 'audio.png')
    MUTE_ICON = Assets.image.load(Path.GRAPHICS_PATH, 'mute.png')

    DEMON_ICON = Assets.image.load(Path.GRAPHICS_PATH, 'demon.png')
    DEMON_ICON = Assets.image.scale(DEMON_ICON, 1/11)

    # Load Controls Image
    CONTROL_IMAGE = Assets.image.load(Path.GRAPHICS_PATH, 'joystick.png')
    TROPHY_IMAGE = Assets.image.load(Path.GRAPHICS_PATH, 'trophy.png')
    SHIPS_IMAGE = Assets.image.scale(MEDIUM_SPACE_SHIP, 5/6)
    SHIPS_IMAGE_2 = Assets.image.scale(HARD_SPACE_SHIP, 3/4)
    TOOLBOX_IMAGE = Assets.image.load(Path.GRAPHICS_PATH, 'toolbox.png')
    TOOLBOX_IMAGE = Assets.image.scale(TOOLBOX_IMAGE, 1/2)

    TOOLS_IMAGE = Assets.image.load(Path.GRAPHICS_PATH, 'tools.png')
    TOOLS_IMAGE = Assets.image.scale(TOOLS_IMAGE, 1/4)
    TOOLS_IMAGE = pygame.transform.rotate(TOOLS_IMAGE, -45)

    GO_BACK_IMAGE = Assets.image.load(Path.GRAPHICS_PATH, 'back2.png')
    GO_BACK_IMAGE = Assets.image.scale(GO_BACK_IMAGE, 6/25)

    EXIT_IMAGE = Assets.image.load(Path.GRAPHICS_PATH, 'exit.png')
    EXIT_IMAGE = Assets.image.scale(EXIT_IMAGE, 1/3)

    # Load Hearts
    HEART_IMAGE = Assets.image.load(Path.GRAPHICS_PATH, 'heart.png')

    PLUS_IMAGE = Assets.image.load(Path.GRAPHICS_PATH, 'plus.png')
    PLUS_IMAGE = Assets.image.scale(PLUS_IMAGE, 1/6)
    MINUS_IMAGE = Assets.image.load(Path.GRAPHICS_PATH, 'minus.png')
    MINUS_IMAGE = Assets.image.scale(MINUS_IMAGE, 1/6)

    PAUSE_IMAGE = Assets.image.load(Path.GRAPHICS_PATH, 'pause.png')
    PAUSE_IMAGE = Assets.image.scale(PAUSE_IMAGE, 1/7)


class Sound:
    PLAYER_LASER_SOUND = Assets.sound.load(Path.SOUND_PATH, 'ownlaser.wav')
    ENEMY_LASER_SOUND = Assets.sound.load(Path.SOUND_PATH, 'enemylaser.wav')
    EXPLODE_SOUND = Assets.sound.load(Path.SOUND_PATH, 'explode.wav')
    LASER_HIT_SOUND = Assets.sound.load(Path.SOUND_PATH, 'laser_hit.wav')


# adding sounds to the list
soundList.append(Sound.PLAYER_LASER_SOUND)
soundList.append(Sound.ENEMY_LASER_SOUND)
soundList.append(Sound.EXPLODE_SOUND)
soundList.append(Sound.LASER_HIT_SOUND)


class Colors:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BACKGROUND_BLACK = (7, 8, 16)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    GREEN2 = (0, 209, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)  # CYAN
    MAGENTA = (255, 0, 255)
    PURPLE = (131, 1, 123)
    ORANGE = (238, 98, 17)
    GREY = (200, 200, 200)
    TRANS = (1, 1, 1)


class Text:
    SHIPS = 'SHIPS'
    SETTINGS = 'SETTINGS'
    CONTROLS = 'CONTROLS'
    SCOREBOARD = 'SCOREBOARD'
    SCOREBOARD_2 = 'SCORE BOARD'
