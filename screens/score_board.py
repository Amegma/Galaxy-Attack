import os
import pygame

from .background import slow_bg_obj
from models.icon_button import IconButton
from models.controls import audio_cfg, display_cfg
from utils.resource_path import resource_path

from constants import WIDTH, \
    CANVAS, \
    goBackImage, \
    center_x, \
    score_list, \
    trophyImage, \
    framespersec, \
    FPS, \
    FONT_PATH


def score_board():
    window_width = CANVAS.get_width()
    background_width = slow_bg_obj.rectBGimg.width
    starting_x = center_x - background_width//2

    score_title_font = pygame.font.Font(resource_path(
        os.path.join(FONT_PATH, 'edit_undo.ttf')), 50)
    score_font = pygame.font.Font(resource_path(
        os.path.join(FONT_PATH, 'neue.ttf')), 35)

    score_list.sort()
    score_list.reverse()

    go_back_btn = IconButton(goBackImage, (starting_x + 30, 30))

    run = True
    while run:
        slow_bg_obj.update()
        slow_bg_obj.render(CANVAS)

        score_title_label = score_title_font.render(
            'Score Board', 1, (0, 229, 0))
        CANVAS.blit(score_title_label, (window_width//2 -
                                        score_title_label.get_width()//2 - 30, 168))
        CANVAS.blit(trophyImage, (window_width//2 +
                                  score_title_label.get_width()//2 - 10, 163))

        i = 0
        for score in score_list[:5]:
            score_label = score_font.render(str(score), 1, (0, 255, 255))
            CANVAS.blit(score_label, (window_width//2 -
                        score_label.get_width() + 20, 250 + i * 40))
            i += 1

            # back_label = score_font.render('[Backspace]', 1, (255, 255, 255))
            # CANVAS.blit(back_label, (starting_x + 30, 30))
        go_back_btn.draw()

        audio_cfg.display_volume(CANVAS)
        framespersec.tick(FPS)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
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
