import pygame
import sys

from .background import slow_bg_obj
from models.icon_button import IconButton
from models.controls import audio_cfg, display_cfg
from utils.draw import draw_text
from config import config
from constants import Image, Font, Colors, Text


def ships():
    ships_title_font = pygame.font.Font(Font.edit_undo_font, 50)
    ships_info_font = pygame.font.Font(Font.neue_font, 22)

    go_back_btn = IconButton(Image.GO_BACK_IMAGE, (config.starting_x + 65, 50))

    NEW_HEART_IMAGE = pygame.transform.scale(
        Image.HEART_IMAGE, (Image.HEART_IMAGE.get_width()*3/4, Image.HEART_IMAGE.get_height()*3/4))

    run = True
    while run:
        slow_bg_obj.update()
        slow_bg_obj.render()

        draw_text(Text.SHIPS, ships_title_font, Colors.CYAN,
                  (config.center_x, 130), True)
        config.CANVAS.blit(Image.SHIPS_IMAGE, (config.center_x -
                                               Image.SHIPS_IMAGE.get_width()//2 - 110, 120))
        config.CANVAS.blit(Image.SHIPS_IMAGE_2, (config.center_x -
                                                 Image.SHIPS_IMAGE.get_width()//2 + 110, 129))

        # Name: Easy Spaceship; Health: 100; Damage: 10;
        config.CANVAS.blit(Image.EASY_SPACE_SHIP, (config.center_x -
                                                   Image.EASY_SPACE_SHIP.get_width()//2 - 270, 235))
        draw_text('Easy Spaceship', ships_info_font, Colors.BLUE,
                  (config.center_x - 210, 220))
        draw_text('Health: 100', ships_info_font,
                  Colors.GREEN, (config.center_x - 210, 247))
        draw_text('Damage: 10', ships_info_font,
                  Colors.RED, (config.center_x - 210, 274))

        # Name: Medium Spaceship; Health: 100; Damage: 18;
        config.CANVAS.blit(Image.MEDIUM_SPACE_SHIP, (config.center_x -
                                                     Image.MEDIUM_SPACE_SHIP.get_width()//2 - 270, 320))
        draw_text('Medium Spaceship', ships_info_font, Colors.BLUE,
                  (config.center_x - 210, 315))
        draw_text('Health: 100', ships_info_font,
                  Colors.GREEN, (config.center_x - 210, 342))
        draw_text('Damage: 18', ships_info_font,
                  Colors.RED, (config.center_x - 210, 369))

        # Name: Hard Spaceship; Health: 100; Damage: 25;
        config.CANVAS.blit(Image.HARD_SPACE_SHIP, (config.center_x -
                                                   Image.HARD_SPACE_SHIP.get_width()//2 - 270, 435))
        draw_text('Hard Spaceship', ships_info_font, Colors.BLUE,
                  (config.center_x - 210, 425))
        draw_text('Health: 100', ships_info_font,
                  Colors.GREEN, (config.center_x - 210, 452))
        draw_text('Damage: 25', ships_info_font,
                  Colors.RED, (config.center_x - 210, 479))

        # Name: Your Spaceship; Lives: 5; Health: 100; Damage: 100
        config.CANVAS.blit(Image.PLAYER_SPACE_SHIP, (config.center_x -
                           Image.PLAYER_SPACE_SHIP.get_width()//2 + 260, 290))
        draw_text('Your Spaceship', ships_info_font, Colors.BLUE,
                  (config.center_x + 70, 285))
        for index in range(1, 6):
            config.CANVAS.blit(
                NEW_HEART_IMAGE, (config.center_x + 45 + 25 * index, 312))
        draw_text('Health: 100', ships_info_font,
                  Colors.GREEN, (config.center_x + 70, 339))
        draw_text('Damage: 100', ships_info_font,
                  Colors.RED, (config.center_x + 70, 366))

        # Name: Boss Spaceship; Health: 1980; Damage: 100;
        config.CANVAS.blit(Image.BOSS_SHIP, (config.center_x -
                           Image.BOSS_SHIP.get_width()//2, 450))
        draw_text('Boss Spaceship', ships_info_font, Colors.BLUE,
                  (config.center_x + 150, 525))
        draw_text('Health: 1980', ships_info_font,
                  Colors.GREEN, (config.center_x + 150, 552))
        draw_text('Damage: 100', ships_info_font,
                  Colors.RED, (config.center_x + 150, 579))

        go_back_btn.draw()

        audio_cfg.display_volume()
        config.clock.tick(config.FPS)
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
                    go_back_btn.outline = True
                else:
                    go_back_btn.outline = False

            # keys = pygame.key.get_pressed()
            # if keys[pygame.K_BACKSPACE]:
            #     run = False
