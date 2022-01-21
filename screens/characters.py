import os
import pygame

from .background import slow_bg_obj
from models.icon_button import IconButton
from models.controls import audio_cfg, display_cfg
from config import Config
from constants import Image, Font


def characters():
    characters_title_font = pygame.font.Font(Font.edit_undo_font, 50)

    go_back_btn = IconButton(Image.GO_BACK_IMAGE, (Config.starting_x + 30, 30))

    run = True
    while run:
        slow_bg_obj.update()
        slow_bg_obj.render(Config.CANVAS)

        characters_title_label = characters_title_font.render(
            'Characters', 1, (0, 255, 255))
        Config.CANVAS.blit(characters_title_label, (Config.center_x -
                                                    characters_title_label.get_width()//2, 130))
        Config.CANVAS.blit(Image.CHARACTERS_IMAGE, (Config.center_x -
                                                    Image.CHARACTERS_IMAGE.get_width()//2 - 170, 120))
        Config.CANVAS.blit(Image.CHARACTERS_IMAGE_2, (Config.center_x -
                                                      Image.CHARACTERS_IMAGE.get_width()//2 + 170, 129))

        Config.CANVAS.blit(Image.EASY_SPACE_SHIP, (Config.center_x -
                                                   Image.EASY_SPACE_SHIP.get_width()//2 - 240, 220))
        Config.CANVAS.blit(Image.MEDIUM_SPACE_SHIP, (Config.center_x -
                                                     Image.MEDIUM_SPACE_SHIP.get_width()//2 - 240, 315))
        Config.CANVAS.blit(Image.HARD_SPACE_SHIP, (Config.center_x -
                                                   Image.HARD_SPACE_SHIP.get_width()//2 - 240, 435))

        Config.CANVAS.blit(Image.PLAYER_SPACE_SHIP, (Config.center_x -
                                                     Image.PLAYER_SPACE_SHIP.get_width()//2 + 135, 270))

        Config.CANVAS.blit(Image.BOSS_SHIP, (Config.center_x -
                           Image.BOSS_SHIP.get_width()//2 + 30, 450))

        go_back_btn.draw()

        audio_cfg.display_volume(Config.CANVAS)
        Config.framespersec.tick(Config.FPS)
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
