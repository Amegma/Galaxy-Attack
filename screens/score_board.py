import pygame
import sys

from .background import slow_bg_obj
from models.icon_button import IconButton
from models.controls import audio_cfg, display_cfg
from models.scores import scores
from utils.assets import Assets
from config import config
from constants import Image, Font, Text, Colors


def score_board():
    score_title_font = pygame.font.Font(Font.edit_undo_font, 50)
    score_font = pygame.font.Font(Font.neue_font, 35)

    go_back_btn = IconButton(Image.GO_BACK_IMAGE)

    run = True
    while run:
        slow_bg_obj.update()
        slow_bg_obj.render()

        Assets.text.draw(Text.SCOREBOARD, score_title_font, Colors.GREEN,
                         (config.center_x, 90), True, False, True)
        Assets.image.draw(Image.TROPHY_IMAGE, (config.center_x + 160, 90))

        if len(scores.get_scores()) == 0:
            Assets.text.draw('You Haven\'t Played Yet!', score_font, Colors.CYAN,
                             (config.center_x, 180), True)
        else:
            Assets.image.draw(Image.LEVELS_IMAGE,
                              (config.center_x-105, 160), True)
            Assets.image.draw(Image.KILLS_IMAGE,
                              (config.center_x+52, 160), True)
            Assets.image.draw(Image.SCORE_IMAGE,
                              (config.center_x+222, 160), True)

            for i, item in enumerate(scores.get_top_5()):
                if item.status:
                    Assets.image.draw(
                        Image.WON_IMAGE, (config.center_x-245, 240 + i*100), True, True)
                else:
                    Assets.image.draw(Image.SKULL_IMAGE_2,
                                      (config.center_x-245, 240 + i*100), True, True)
                Assets.text.draw(str(item.level), score_font, Colors.CYAN,
                                 (config.center_x-105, 220 + i*100), True)
                Assets.text.draw(str(item.kills), score_font, Colors.RED,
                                 (config.center_x+52, 220 + i*100), True)
                Assets.text.draw(str(item.score), score_font, Colors.YELLOW,
                                 (config.center_x+222, 220 + i*100), True)

        go_back_btn.draw((config.starting_x + 65, 50), True, True)

        audio_cfg.display_volume()
        config.clock.tick(config.FPS)
        pygame.display.flip()

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
