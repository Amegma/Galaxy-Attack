import pygame
import sys

from .background import slow_bg_obj
from models.icon_button import IconButton
from models.controls import audio_cfg, display_cfg
from utils.assets import Assets
from config import config
from constants import Image, score_list, Font, Text, Colors


def score_board():
    score_title_font = pygame.font.Font(Font.edit_undo_font, 50)
    score_font = pygame.font.Font(Font.neue_font, 35)

    score_list.sort()
    score_list.reverse()

    go_back_btn = IconButton(Image.GO_BACK_IMAGE)

    run = True
    while run:
        slow_bg_obj.update()
        slow_bg_obj.render()

        Assets.text.draw(Text.SCOREBOARD_2, score_title_font, Colors.GREEN,
                         (config.center_x - 30, 168), True)
        Assets.image.draw(Image.TROPHY_IMAGE, (config.center_x + 130, 163))

        if len(score_list) == 0:
            Assets.text.draw('You Haven\'t Played Yet!', score_font, Colors.CYAN,
                             (config.center_x, 250), True)

        i = 0
        for score in score_list[:5]:
            Assets.text.draw(str(score), score_font, Colors.CYAN,
                             (config.center_x-20, 250 + i * 40), True)
            i += 1

        go_back_btn.draw((config.starting_x + 65, 50), True, True)

        audio_cfg.display_volume()
        config.clock.tick(config.FPS)
        pygame.display.update()

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

            # Mouse hover events
            if event.type == pygame.MOUSEMOTION:
                if go_back_btn.isOver():
                    go_back_btn.outline = True
                else:
                    go_back_btn.outline = False

            # keys = pygame.key.get_pressed()
            # if keys[pygame.K_BACKSPACE]:
            #     run = False
