import os
import pygame

from .background import slow_bg_obj
from models.icon_button import IconButton
from models.controls import audio_cfg, display_cfg
from config import Config
from constants import Image, Font


def characters():
    characters_title_font = pygame.font.Font(Font.edit_undo_font, 50)
    characters_info_font = pygame.font.Font(Font.neue_font, 22)

    go_back_btn = IconButton(Image.GO_BACK_IMAGE, (Config.starting_x + 30, 30))

    NEW_HEART_IMAGE = pygame.transform.scale(
        Image.HEART_IMAGE, (Image.HEART_IMAGE.get_width()*3/4, Image.HEART_IMAGE.get_height()*3/4))

    run = True
    while run:
        slow_bg_obj.update()
        slow_bg_obj.render(Config.CANVAS)

        characters_title_label = characters_title_font.render(
            "Characters", 1, (0, 255, 255))
        Config.CANVAS.blit(characters_title_label, (Config.center_x -
                                                    characters_title_label.get_width()//2, 130))
        Config.CANVAS.blit(Image.CHARACTERS_IMAGE, (Config.center_x -
                                                    Image.CHARACTERS_IMAGE.get_width()//2 - 170, 120))
        Config.CANVAS.blit(Image.CHARACTERS_IMAGE_2, (Config.center_x -
                                                      Image.CHARACTERS_IMAGE.get_width()//2 + 170, 129))

        # Name: Easy Spaceship; Health: 100; Damage: 10;
        Config.CANVAS.blit(Image.EASY_SPACE_SHIP, (Config.center_x -
                                                   Image.EASY_SPACE_SHIP.get_width()//2 - 240, 220))
        easy_ship_label = characters_info_font.render(
            'Easy Spaceship', 1, (0, 0, 255))
        Config.CANVAS.blit(easy_ship_label, (Config.center_x - 180, 220))
        easy_ship_label = characters_info_font.render(
            'Health: 100', 1, (0, 255, 0))
        Config.CANVAS.blit(easy_ship_label, (Config.center_x - 180, 247))
        easy_ship_label = characters_info_font.render(
            'Damage: 10', 1, (255, 0, 0))
        Config.CANVAS.blit(easy_ship_label, (Config.center_x - 180, 274))

        # Name: Medium Spaceship; Health: 100; Damage: 18;
        Config.CANVAS.blit(Image.MEDIUM_SPACE_SHIP, (Config.center_x -
                                                     Image.MEDIUM_SPACE_SHIP.get_width()//2 - 240, 315))
        medium_ship_label = characters_info_font.render(
            'Medium Spaceship', 1, (0, 0, 255))
        Config.CANVAS.blit(medium_ship_label, (Config.center_x - 180, 315))
        medium_ship_label = characters_info_font.render(
            'Health: 100', 1, (0, 255, 0))
        Config.CANVAS.blit(medium_ship_label, (Config.center_x - 180, 342))
        medium_ship_label = characters_info_font.render(
            'Damage: 18', 1, (255, 0, 0))
        Config.CANVAS.blit(medium_ship_label, (Config.center_x - 180, 369))

        # Name: Hard Spaceship; Health: 100; Damage: 25;
        Config.CANVAS.blit(Image.HARD_SPACE_SHIP, (Config.center_x -
                                                   Image.HARD_SPACE_SHIP.get_width()//2 - 240, 435))
        hard_ship_label = characters_info_font.render(
            'Hard Spaceship', 1, (0, 0, 255))
        Config.CANVAS.blit(hard_ship_label, (Config.center_x - 180, 425))
        hard_ship_label = characters_info_font.render(
            'Health: 100', 1, (0, 255, 0))
        Config.CANVAS.blit(hard_ship_label, (Config.center_x - 180, 452))
        hard_ship_label = characters_info_font.render(
            'Damage: 25', 1, (255, 0, 0))
        Config.CANVAS.blit(hard_ship_label, (Config.center_x - 180, 479))

        # Name: Your Spaceship; Lives: 5; Health: 100; Damage: 100
        Config.CANVAS.blit(Image.PLAYER_SPACE_SHIP, (Config.center_x -
                                                     Image.PLAYER_SPACE_SHIP.get_width()//2 + 240, 280))
        player_ship_label = characters_info_font.render(
            'Your Spaceship', 1, (0, 0, 255))
        Config.CANVAS.blit(player_ship_label, (Config.center_x + 100, 305))
        for index in range(1, 6):
            Config.CANVAS.blit(
                NEW_HEART_IMAGE, (Config.center_x + 75 + 25 * index, 332))
        player_ship_label = characters_info_font.render(
            'Health: 100', 1, (0, 255, 0))
        Config.CANVAS.blit(player_ship_label, (Config.center_x + 100, 359))
        player_ship_label = characters_info_font.render(
            'Damage: 100', 1, (255, 0, 0))
        Config.CANVAS.blit(player_ship_label, (Config.center_x + 100, 386))

        # Name: Boss Spaceship; Health: 1980; Damage: 100;
        Config.CANVAS.blit(Image.BOSS_SHIP, (Config.center_x -
                           Image.BOSS_SHIP.get_width()//2 + 20, 450))
        Config.CANVAS.blit(Image.DEMON_ICON, (Config.center_x + 140, 520))
        boss_ship_label = characters_info_font.render(
            'Boss Spaceship', 1, (0, 0, 255))
        Config.CANVAS.blit(boss_ship_label, (Config.center_x + 180, 525))
        boss_ship_label = characters_info_font.render(
            'Health: 1980', 1, (0, 255, 0))
        Config.CANVAS.blit(boss_ship_label, (Config.center_x + 180, 552))
        boss_ship_label = characters_info_font.render(
            'Damage: 100', 1, (255, 0, 0))
        Config.CANVAS.blit(boss_ship_label, (Config.center_x + 180, 579))

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
