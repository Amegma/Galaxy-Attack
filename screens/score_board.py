import os
import pygame

from constants import WIDTH, \
                      CANVAS, \
                      score_list, \
                      trophyImage, \
                      framespersec, \
                      FPS, \
                      FONT_PATH

from .controls import audio_cfg, display_cfg
from .background import slow_bg_obj

def score_board():
    run = True

    score_title_font = pygame.font.Font(os.path.join(FONT_PATH, 'edit_undo.ttf'), 50)
    score_font = pygame.font.Font(os.path.join(FONT_PATH, 'neue.ttf'), 35)

    score_list.sort()
    score_list.reverse()

    while run:
        slow_bg_obj.update()
        slow_bg_obj.render(CANVAS)

        window_width = CANVAS.get_width()
        background_width = slow_bg_obj.rectBGimg.width
        screen_rect = CANVAS.get_rect()
        center_x = screen_rect.centerx
        starting_x = center_x - background_width//2

        score_title_label = score_title_font.render('Score Board', 1, (0, 229, 0))
        CANVAS.blit(score_title_label, (window_width//2 - score_title_label.get_width()//2 - 30, 168))
        CANVAS.blit(trophyImage, (window_width//2 + score_title_label.get_width()//2 - 10, 163))

        i = 0
        for score in score_list[:5]:
            score_label = score_font.render(str(score), 1, (0, 255, 255))
            CANVAS.blit(score_label, (window_width//2 - score_label.get_width() + 20, 250 + i * 40))
            i += 1

        back_label = score_font.render('[Backspace]', 1, (255, 255, 255))
        CANVAS.blit(back_label, (starting_x + 30, 30))

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

        keys = pygame.key.get_pressed()
        if keys[pygame.K_BACKSPACE]:
            run = False
