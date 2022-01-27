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
    karmatic_arcade_font = resource_path(
        os.path.join(Path.FONT_PATH, 'karmatic_arcade.ttf'))


class Image:
    TITLE_LOGO = pygame.image.load(resource_path(
        os.path.join(Path.GRAPHICS_PATH, 'title_logo.png')))
    TITLE_LOGO = pygame.transform.scale(
        TITLE_LOGO, (TITLE_LOGO.get_width()*2/7, TITLE_LOGO.get_height()*2/7))

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
    SHIPS_IMAGE = pygame.transform.scale(MEDIUM_SPACE_SHIP, (60, 60))
    SHIPS_IMAGE_2 = pygame.transform.scale(HARD_SPACE_SHIP, (60, 66*0.75))
    TOOLBOX_IMAGE = pygame.image.load(resource_path(
        os.path.join(Path.GRAPHICS_PATH, 'toolbox.png')))
    TOOLBOX_IMAGE = pygame.transform.scale(
        TOOLBOX_IMAGE, (TOOLBOX_IMAGE.get_width()/2, TOOLBOX_IMAGE.get_height()/2))

    TOOLS_IMAGE = pygame.image.load(resource_path(
        os.path.join(Path.GRAPHICS_PATH, 'tools.png')))
    TOOLS_IMAGE = pygame.transform.scale(
        TOOLS_IMAGE, (TOOLS_IMAGE.get_width()/4, TOOLS_IMAGE.get_height()/4))
    TOOLS_IMAGE = pygame.transform.rotate(TOOLS_IMAGE, -45)

    GO_BACK_IMAGE = pygame.image.load(resource_path(
        os.path.join(Path.GRAPHICS_PATH, 'back2.png')))
    # GO_BACK_IMAGE = pygame.transform.scale()
    GO_BACK_IMAGE = pygame.transform.scale(GO_BACK_IMAGE, (34*2.4, 19*2.4))

    EXIT_IMAGE = pygame.image.load(resource_path(
        os.path.join(Path.GRAPHICS_PATH, 'exit.png')))
    EXIT_IMAGE = pygame.transform.scale(
        EXIT_IMAGE, (EXIT_IMAGE.get_width()/3, EXIT_IMAGE.get_height()/3))

    # Load Hearts
    HEART_IMAGE = pygame.image.load(resource_path(
        os.path.join(Path.GRAPHICS_PATH, 'heart.png')))

    PLUS_IMAGE = pygame.image.load(resource_path(
        os.path.join(Path.GRAPHICS_PATH, 'plus.png')))
    PLUS_IMAGE = pygame.transform.scale(
        PLUS_IMAGE, (PLUS_IMAGE.get_width()/6, PLUS_IMAGE.get_height()/6))
    MINUS_IMAGE = pygame.image.load(resource_path(
        os.path.join(Path.GRAPHICS_PATH, 'minus.png')))
    MINUS_IMAGE = pygame.transform.scale(
        MINUS_IMAGE, (MINUS_IMAGE.get_width()/6, MINUS_IMAGE.get_height()/6))


class Sound:
    PLAYER_LASER_SOUND = pygame.mixer.Sound(resource_path(
        os.path.join(Path.SOUND_PATH, 'ownlaser.wav')))
    ENEMY_LASER_SOUND = pygame.mixer.Sound(resource_path(
        os.path.join(Path.SOUND_PATH, 'enemylaser.wav')))
    EXPLODE_SOUND = pygame.mixer.Sound(resource_path(
        os.path.join(Path.SOUND_PATH, 'explode.wav')))
    LASER_HIT_SOUND = pygame.mixer.Sound(resource_path(
        os.path.join(Path.SOUND_PATH, 'laser_hit.wav')))


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
