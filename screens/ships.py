import pygame
import sys

from .background import slow_bg_obj
from models.icon_button import IconButton
from models.controls import audio_cfg, display_cfg
from config import config
from constants import Image, Font, Colors


def ships():
    ships_title_font = pygame.font.Font(Font.edit_undo_font, 50)
    ships_info_font = pygame.font.Font(Font.neue_font, 22)

    go_back_btn = IconButton(Image.GO_BACK_IMAGE, (config.starting_x + 30, 30))

    NEW_HEART_IMAGE = pygame.transform.scale(
        Image.HEART_IMAGE, (Image.HEART_IMAGE.get_width()*3/4, Image.HEART_IMAGE.get_height()*3/4))

    run = True
    while run:
        slow_bg_obj.update()
        slow_bg_obj.render()

        ships_title_label = ships_title_font.render(
            "Ships", 1, Colors.CYAN)
        config.CANVAS.blit(ships_title_label, (config.center_x -
                                               ships_title_label.get_width()//2, 130))
        config.CANVAS.blit(Image.SHIPS_IMAGE, (config.center_x -
                                               Image.SHIPS_IMAGE.get_width()//2 - 110, 120))
        config.CANVAS.blit(Image.SHIPS_IMAGE_2, (config.center_x -
                                                 Image.SHIPS_IMAGE.get_width()//2 + 110, 129))

        # Name: Easy Spaceship; Health: 100; Damage: 10;
        config.CANVAS.blit(Image.EASY_SPACE_SHIP, (config.center_x -
                                                   Image.EASY_SPACE_SHIP.get_width()//2 - 270, 235))
        easy_ship_label = ships_info_font.render(
            'Easy Spaceship', 1, Colors.BLUE)
        config.CANVAS.blit(easy_ship_label, (config.center_x - 210, 220))
        easy_ship_label = ships_info_font.render(
            'Health: 100', 1, Colors.GREEN)
        config.CANVAS.blit(easy_ship_label, (config.center_x - 210, 247))
        easy_ship_label = ships_info_font.render(
            'Damage: 10', 1, Colors.RED)
        config.CANVAS.blit(easy_ship_label, (config.center_x - 210, 274))

        # Name: Medium Spaceship; Health: 100; Damage: 18;
        config.CANVAS.blit(Image.MEDIUM_SPACE_SHIP, (config.center_x -
                                                     Image.MEDIUM_SPACE_SHIP.get_width()//2 - 270, 320))
        medium_ship_label = ships_info_font.render(
            'Medium Spaceship', 1, Colors.BLUE)
        config.CANVAS.blit(medium_ship_label, (config.center_x - 210, 315))
        medium_ship_label = ships_info_font.render(
            'Health: 100', 1, Colors.GREEN)
        config.CANVAS.blit(medium_ship_label, (config.center_x - 210, 342))
        medium_ship_label = ships_info_font.render(
            'Damage: 18', 1, Colors.RED)
        config.CANVAS.blit(medium_ship_label, (config.center_x - 210, 369))

        # Name: Hard Spaceship; Health: 100; Damage: 25;
        config.CANVAS.blit(Image.HARD_SPACE_SHIP, (config.center_x -
                                                   Image.HARD_SPACE_SHIP.get_width()//2 - 270, 435))
        hard_ship_label = ships_info_font.render(
            'Hard Spaceship', 1, Colors.BLUE)
        config.CANVAS.blit(hard_ship_label, (config.center_x - 210, 425))
        hard_ship_label = ships_info_font.render(
            'Health: 100', 1, Colors.GREEN)
        config.CANVAS.blit(hard_ship_label, (config.center_x - 210, 452))
        hard_ship_label = ships_info_font.render(
            'Damage: 25', 1, Colors.RED)
        config.CANVAS.blit(hard_ship_label, (config.center_x - 210, 479))

        # Name: Your Spaceship; Lives: 5; Health: 100; Damage: 100
        config.CANVAS.blit(Image.PLAYER_SPACE_SHIP, (config.center_x -
                           Image.PLAYER_SPACE_SHIP.get_width()//2 + 260, 290))
        player_ship_label = ships_info_font.render(
            'Your Spaceship', 1, Colors.BLUE)
        config.CANVAS.blit(player_ship_label, (config.center_x + 70, 285))
        for index in range(1, 6):
            config.CANVAS.blit(
                NEW_HEART_IMAGE, (config.center_x + 45 + 25 * index, 312))
        player_ship_label = ships_info_font.render(
            'Health: 100', 1, Colors.GREEN)
        config.CANVAS.blit(player_ship_label, (config.center_x + 70, 339))
        player_ship_label = ships_info_font.render(
            'Damage: 100', 1, Colors.RED)
        config.CANVAS.blit(player_ship_label, (config.center_x + 70, 366))

        # Name: Boss Spaceship; Health: 1980; Damage: 100;
        config.CANVAS.blit(Image.BOSS_SHIP, (config.center_x -
                           Image.BOSS_SHIP.get_width()//2, 450))
        # config.CANVAS.blit(Image.DEMON_ICON, (config.center_x + 140, 520))
        boss_ship_label = ships_info_font.render(
            'Boss Spaceship', 1, Colors.BLUE)
        config.CANVAS.blit(boss_ship_label, (config.center_x + 150, 525))
        boss_ship_label = ships_info_font.render(
            'Health: 1980', 1, Colors.GREEN)
        config.CANVAS.blit(boss_ship_label, (config.center_x + 150, 552))
        boss_ship_label = ships_info_font.render(
            'Damage: 100', 1, Colors.RED)
        config.CANVAS.blit(boss_ship_label, (config.center_x + 150, 579))

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
