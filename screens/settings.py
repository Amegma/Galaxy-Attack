import pygame
import sys

from .background import slow_bg_obj
from models.icon_button import IconButton
from models.controls import audio_cfg, display_cfg
from config import config
from constants import Image, Font, Colors, Text

from models.slider import Slider


def settings():
    settings_title_font = pygame.font.Font(Font.edit_undo_font, 50)
    settings_right_font = pygame.font.Font(Font.edit_undo_font, 50)
    settings_left_font = pygame.font.Font(Font.edit_undo_font, 46)

    go_back_btn = IconButton(Image.GO_BACK_IMAGE, (config.starting_x + 65, 50))

    plus_btn = IconButton(Image.PLUS_IMAGE, (config.center_x + 235, 260))
    minus_btn = IconButton(Image.MINUS_IMAGE, (config.center_x + 70, 260))

    run = True
    while run:
        slow_bg_obj.update()
        slow_bg_obj.render()

        settings_title_label = settings_title_font.render(
            Text.SETTINGS, 1, Colors.YELLOW)
        config.CANVAS.blit(settings_title_label, (config.center_x -
                                                  settings_title_label.get_width()//2, 130))
        config.CANVAS.blit(Image.TOOLS_IMAGE, (config.center_x -
                                               Image.TOOLS_IMAGE.get_width()//2 - 150, 120))
        config.CANVAS.blit(Image.TOOLBOX_IMAGE, (config.center_x -
                                                 Image.TOOLBOX_IMAGE.get_width()//2 + 150, 129))

        settings_left_label = settings_left_font.render(
            'VOLUME', 1, Colors.GREEN)
        config.CANVAS.blit(settings_left_label, (config.center_x -
                                                 settings_left_label.get_width()//2 - 160, 240))
        settings_right_label = settings_right_font.render(
            f'{audio_cfg.volume}', 1, Colors.WHITE)
        config.CANVAS.blit(settings_right_label, (config.center_x -
                                                  settings_right_label.get_width()//2 + 155, 240))

        go_back_btn.draw()

        minus_btn.draw()

        plus_btn.draw()

        # audio_cfg.display_volume()
        config.framespersec.tick(config.FPS)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_f:
                    display_cfg.toggle_full_screen()
                if event.key == pygame.K_BACKSPACE:
                    run = False

            # Mouse click events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if go_back_btn.isOver():
                        run = False
                    if plus_btn.isOver():
                        audio_cfg.inc_volume(5)
                    if minus_btn.isOver():
                        audio_cfg.dec_volume(5)

            # Mouse hover events
            if event.type == pygame.MOUSEMOTION:
                if go_back_btn.isOver():
                    go_back_btn.outline = True
                else:
                    go_back_btn.outline = False

            # keys = pygame.key.get_pressed()
            # if keys[pygame.K_BACKSPACE]:
            #     run = False
