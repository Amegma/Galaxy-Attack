from email.policy import default
import pygame
import sys

from .background import slow_bg_obj
from utils.assets import Assets
from models.icon_button import IconButton
from models.controls import audio_cfg, display_cfg
from config import config
from constants import Image, Font, Colors, Text


def controls():
    run = True

    current_page = 1
    total_pages = 4

    control_title_font = pygame.font.Font(Font.edit_undo_font, 50)
    control_title_font_2 = pygame.font.Font(Font.edit_undo_font, 45)
    control_font = pygame.font.Font(Font.neue_font, 30)
    control_font_2 = pygame.font.Font(Font.neue_font, 40)
    keys_font = pygame.font.Font(Font.neue_font, 30)

    go_back_btn = IconButton(Image.GO_BACK_IMAGE)
    back_btn = IconButton(Image.BACK_IMAGE)
    next_btn = IconButton(Image.NEXT_IMAGE)

    def moveControlPage():
        Assets.text.draw('MOVE', control_title_font, Colors.GREEN,
                         (config.center_x-245, 190))
        Assets.text.draw('/ AIM:', control_title_font, Colors.GREEN,
                         (config.center_x-245, 240))

        Assets.text.draw('MOUSE', control_title_font_2, Colors.MAGENTA,
                         (config.center_x+152, 190), True)
        Assets.image.draw(Image.MOUSE, (config.center_x+152, 240), True)

        Assets.text.draw('KEYBOARD', control_title_font_2, Colors.MAGENTA,
                         (config.center_x-245, 380))
        Assets.text.draw('OR', control_font_2, Colors.WHITE,
                         (config.center_x, 445), True)
        Assets.image.draw(Image.WASD_KEYS, (config.center_x-260, 440))
        Assets.image.draw(Image.ARROW_KEYS, (config.center_x+50, 440))

    def shootControlPage():
        Assets.text.draw('Shoot:', control_title_font, Colors.YELLOW,
                         (config.center_x-245, 190))

        Assets.text.draw('MOUSE', control_title_font_2, Colors.CYAN,
                         (config.center_x+152, 190), True)
        Assets.image.draw(Image.LEFT_MOUSE_CLICK,
                          (config.center_x+152, 240), True)

        Assets.text.draw('KEYBOARD', control_title_font_2, Colors.CYAN,
                         (config.center_x-245, 380))
        Assets.image.draw(Image.SPACEBAR_KEY, (config.center_x, 470))
        Assets.text.draw('SPACEBAR', control_font_2, Colors.WHITE,
                         (config.center_x-245, 460))

    def returnControlPage():
        Assets.text.draw('RETURN BACK', control_title_font, Colors.MAGENTA,
                         (config.center_x-245, 190))
        Assets.text.draw('TO HOME:', control_title_font, Colors.MAGENTA,
                         (config.center_x-245, 240))

        Assets.text.draw('MOUSE', control_title_font_2, Colors.ORANGE,
                         (config.center_x+152, 190), True)
        Assets.image.draw(Image.RIGHT_MOUSE_CLICK,
                          (config.center_x+152, 240), True)

        Assets.text.draw('KEYBOARD', control_title_font_2, Colors.ORANGE,
                         (config.center_x-245, 380))
        Assets.image.draw(Image.SPACEBAR_KEY, (config.center_x, 470))
        Assets.text.draw('SPACEBAR', control_font_2, Colors.WHITE,
                         (config.center_x-245, 460))

    def pageTwo():
        Assets.text.draw('Shoot', control_font, Colors.GREEN,
                         (config.starting_x + 125, 215))
        Assets.text.draw('[spacebar]', keys_font, Colors.RED,
                         (config.starting_x + 470, 215))

        Assets.text.draw('Move Left', control_font, Colors.GREEN,
                         (config.starting_x + 125, 270))
        Assets.text.draw('[left] or [a]', keys_font, Colors.RED,
                         (config.starting_x + 470, 270))

        Assets.text.draw('Move Right', control_font, Colors.GREEN,
                         (config.starting_x + 125, 325))
        Assets.text.draw('[right] or [d]', keys_font, Colors.RED,
                         (config.starting_x + 470, 325))

        Assets.text.draw('Move Down', control_font, Colors.GREEN,
                         (config.starting_x + 125, 380))
        Assets.text.draw('[down] or [s]', keys_font, Colors.RED,
                         (config.starting_x + 470, 380))

        Assets.text.draw('Move Up', control_font, Colors.GREEN,
                         (config.starting_x + 125, 435))
        Assets.text.draw('[up] or [w]', keys_font, Colors.RED,
                         (config.starting_x + 470, 435))

        Assets.text.draw('Return back to home', control_font, Colors.GREEN,
                         (config.starting_x + 125, 490))
        Assets.text.draw('[backspace]', keys_font, Colors.RED,
                         (config.starting_x + 470, 490))

        Assets.text.draw('Mute Audio', control_font, Colors.GREEN,
                         (config.starting_x + 125, 545))
        Assets.text.draw('[m]', keys_font, Colors.RED,
                         (config.starting_x + 470, 545))

        Assets.text.draw('Volume Up/Down', control_font, Colors.GREEN,
                         (config.starting_x + 125, 600))
        Assets.text.draw('[+]/[-]', keys_font, Colors.RED,
                         (config.starting_x + 470, 600))

        Assets.text.draw('Toggle Full Screen', control_font, Colors.GREEN,
                         (config.starting_x + 125, 655))
        Assets.text.draw('[f]', keys_font, Colors.RED,
                         (config.starting_x + 470, 655))

    while run:
        slow_bg_obj.update()
        slow_bg_obj.render()

        match current_page:
            case 1:
                moveControlPage()
            case 2:
                shootControlPage()
            case 3:
                returnControlPage()
            case 4:
                pageTwo()

        Assets.text.draw(Text.CONTROLS, control_title_font, Colors.BLUE,
                         (config.center_x, 100), True, False, True)
        Assets.image.draw(Image.CONTROL_IMAGE, (config.center_x + 125, 90))

        go_back_btn.draw((config.starting_x + 65, 50), True, True)
        back_btn.draw(
            (config.center_x-Image.BACK_IMAGE.get_width()-30, config.ending_y-125))
        next_btn.draw((config.center_x + 30, config.ending_y - 125))

        audio_cfg.display_volume()

        pygame.display.flip()
        config.clock.tick(config.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.VIDEORESIZE:
                if not display_cfg.fullscreen:
                    config.update(event.w, event.h)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_m:
                    audio_cfg.toggle_mute()
                if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                    audio_cfg.inc_volume(5)
                if event.key == pygame.K_MINUS:
                    audio_cfg.dec_volume(5)
                if event.key == pygame.K_f:
                    config.update(
                        config.monitor_size[0], config.monitor_size[1])
                    display_cfg.toggle_full_screen()
                if event.key == pygame.K_BACKSPACE:
                    run = False

            # Mouse click events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if go_back_btn.isOver():
                        run = False
                    if back_btn.isOver():
                        if current_page == 1:
                            current_page = total_pages
                        else:
                            current_page -= 1
                    if next_btn.isOver():
                        if current_page == total_pages:
                            current_page = 1
                        else:
                            current_page += 1

            # Mouse hover events
            if event.type == pygame.MOUSEMOTION:
                if go_back_btn.isOver():
                    go_back_btn.outline = True
                else:
                    go_back_btn.outline = False

                if back_btn.isOver():
                    back_btn.outline = True
                else:
                    back_btn.outline = False

                if next_btn.isOver():
                    next_btn.outline = True
                else:
                    next_btn.outline = False
