import pygame
import sys

from .background import slow_bg_obj
from models.icon_button import IconButton
from models.controls import audio_cfg, display_cfg
from config import config
from constants import Image, score_list, Font, Text, Colors


def score_board():
    score_title_font = pygame.font.Font(Font.edit_undo_font, 50)
    score_font = pygame.font.Font(Font.neue_font, 35)

    score_list.sort()
    score_list.reverse()

    go_back_btn = IconButton(Image.GO_BACK_IMAGE, (config.starting_x + 65, 50))

    run = True
    while run:
        slow_bg_obj.update()
        slow_bg_obj.render()

        score_title_label = score_title_font.render(
            Text.SCOREBOARD_2, 1, Colors.GREEN)
        config.CANVAS.blit(score_title_label, (config.center_x -
                                               score_title_label.get_width()//2 - 30, 168))
        config.CANVAS.blit(Image.TROPHY_IMAGE, (config.center_x +
                                                score_title_label.get_width()//2 - 10, 163))

        if len(score_list) == 0:
            score_label = score_font.render(
                'You Haven\'t Played Yet!', 1, Colors.CYAN)
            config.CANVAS.blit(score_label, (config.center_x -
                                             score_label.get_width()//2, 250))

        i = 0
        for score in score_list[:5]:
            score_label = score_font.render(str(score), 1, (0, 255, 255))
            config.CANVAS.blit(score_label, (config.center_x -
                                             score_label.get_width() + 20, 250 + i * 40))
            i += 1

        go_back_btn.draw()

        audio_cfg.display_volume()
        config.framespersec.tick(config.FPS)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_m:
                    audio_cfg.toggle_mute()
                if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                    audio_cfg.inc_volume(5)
                if event.key == pygame.K_MINUS:
                    audio_cfg.dec_volume(5)
                if event.key == pygame.K_f:
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
                    go_back_btn.outline = "onover"
                else:
                    go_back_btn.outline = "default"

            # keys = pygame.key.get_pressed()
            # if keys[pygame.K_BACKSPACE]:
            #     run = False
