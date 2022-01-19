import os
import pygame

from .background import slow_bg_obj
from models.icon_button import IconButton
from models.controls import audio_cfg, display_cfg

from constants import CONTROL_IMAGE,\
    GO_BACK_IMAGE, \
    CANVAS, \
    framespersec, \
    FPS, \
    edit_undo_font, \
    neue_font


def controls():
    run = True

    window_width = CANVAS.get_width()
    background_width = slow_bg_obj.rectBGimg.width
    screen_rect = CANVAS.get_rect()
    center_x = screen_rect.centerx
    starting_x = center_x - background_width//2

    control_title_font = pygame.font.Font(edit_undo_font, 50)
    control_font = pygame.font.Font(neue_font, 30)
    keys_font = pygame.font.Font(neue_font, 30)

    go_back_btn = IconButton(GO_BACK_IMAGE, (starting_x + 30, 30))

    while run:
        slow_bg_obj.update()
        slow_bg_obj.render(CANVAS)

        control_title_label = control_title_font.render(
            'Controls', 1, (0, 0, 209))
        CANVAS.blit(control_title_label, (window_width//2 -
                    control_title_label.get_width()//2 - 30, 130))
        CANVAS.blit(CONTROL_IMAGE, (window_width//2 +
                    control_title_label.get_width()//2 - 10, 112))

        shoot_label = control_font.render('Shoot', 1, (0, 225, 0))
        CANVAS.blit(shoot_label, (starting_x + 125, 215))
        shoot_key_label = keys_font.render('[spacebar]', 1, (240, 0, 0))
        CANVAS.blit(shoot_key_label, (starting_x + 470, 215))

        left_label = control_font.render('Move Left', 1, (0, 225, 0))
        CANVAS.blit(left_label, (starting_x + 125, 270))
        left_key_label = keys_font.render('[left] or [a]', 1, (240, 0, 0))
        CANVAS.blit(left_key_label, (starting_x + 470, 270))

        right_label = control_font.render('Move Right', 1, (0, 225, 0))
        CANVAS.blit(right_label, (starting_x + 125, 325))
        right_key_label = keys_font.render('[right] or [d]', 1, (240, 0, 0))
        CANVAS.blit(right_key_label, (starting_x + 470, 325))

        down_label = control_font.render('Move Down', 1, (0, 225, 0))
        CANVAS.blit(down_label, (starting_x + 125, 380))
        down_key_label = keys_font.render('[down] or [s]', 1, (240, 0, 0))
        CANVAS.blit(down_key_label, (starting_x + 470, 380))

        up_label = control_font.render('Move Up', 1, (0, 225, 0))
        CANVAS.blit(up_label, (starting_x + 125, 435))
        up_key_label = keys_font.render('[up] or [w]', 1, (240, 0, 0))
        CANVAS.blit(up_key_label, (starting_x + 470, 435))

        escape_label = control_font.render(
            'Return back to home', 1, (0, 225, 0))
        CANVAS.blit(escape_label, (starting_x + 125, 490))
        escape_key_label = keys_font.render('[backspace]', 1, (240, 0, 0))
        CANVAS.blit(escape_key_label, (starting_x + 470, 490))

        mute_label = control_font.render('Mute Audio', 1, (0, 225, 0))
        CANVAS.blit(mute_label, (starting_x + 125, 545))
        mute_key_label = keys_font.render('[m]', 1, (240, 0, 0))
        CANVAS.blit(mute_key_label, (starting_x + 470, 545))

        sfx_label = control_font.render('Volume Up/Down', 1, (0, 225, 0))
        CANVAS.blit(sfx_label, (starting_x + 125, 600))
        sfx_key_label = keys_font.render('[+]/[-]', 1, (240, 0, 0))
        CANVAS.blit(sfx_key_label, (starting_x + 470, 600))

        sfx_label = control_font.render('Toggle Full Screen', 1, (0, 225, 0))
        CANVAS.blit(sfx_label, (starting_x + 125, 655))
        sfx_key_label = keys_font.render('[f]', 1, (240, 0, 0))
        CANVAS.blit(sfx_key_label, (starting_x + 470, 655))

        # control_title_label = control_font.render(
        #     '[Backspace]', 1, (255, 255, 255))
        # CANVAS.blit(control_title_label, (starting_x + 30, 30))
        go_back_btn.draw()

        audio_cfg.display_volume(CANVAS)

        pygame.display.update()
        framespersec.tick(FPS)

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
