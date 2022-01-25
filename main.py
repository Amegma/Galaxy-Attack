import sys
import pygame
import argparse

from screens.game import game
from screens.controls import controls
from screens.score_board import score_board
from screens.ships import ships
from screens.settings import settings
from screens.background import slow_bg_obj
from models.button import Button
from models.icon_button import IconButton
from models.controls import audio_cfg, display_cfg
from config import config
from constants import Path, Image, Font, Colors, Text

# parsing arguments
ag = argparse.ArgumentParser()
ag.add_argument("--mute", help="disable all sounds", action="store_true")
args = vars(ag.parse_args())

if args["mute"]:
    audio_cfg.toggle_mute()

pygame.font.init()

pygame.display.set_caption(config.TITLE)
pygame.display.set_icon(Image.PLAYER_SPACE_SHIP)


def main():
    title_font = pygame.font.Font(Font.edit_undo_font, 82)

    audio_cfg.play_music(Path.MENU_MUSIC_PATH)

    mouse_btn = Button(Colors.BACKGROUND_BLACK, Colors.WHITE,
                       (config.center_x - 210, config.center_y + 42), (195, 66), "MOUSE")
    keyboard_btn = Button(Colors.BACKGROUND_BLACK, Colors.WHITE,
                          (config.center_x + 15, config.center_y + 42), (195, 66), "KEYBOARD")
    control_btn = IconButton(
        Image.CONTROL_IMAGE, (config.starting_x + 65, 53), Text.CONTROLS)
    ships_btn = IconButton(
        Image.SHIPS_IMAGE, (config.starting_x+65, 165), Text.SHIPS)
    trophy_btn = IconButton(
        Image.TROPHY_IMAGE, (config.ending_x - 65, 55), Text.SCOREBOARD)
    settings_btn = IconButton(
        Image.TOOLBOX_IMAGE, (config.ending_x - 65, 165), Text.SETTINGS)

    exit_btn = IconButton(
        Image.EXIT_IMAGE, (config.ending_x - 45, config.ending_y - 40))

    run = True
    while run:
        # print(config.ending_x, config.ending_y)
        pygame.mouse.set_visible(True)
        slow_bg_obj.update()
        slow_bg_obj.render()

        # Ships
        config.CANVAS.blit(Image.BOSS_SHIP, (config.center_x -
                           Image.BOSS_SHIP.get_width()//2, 110))
        config.CANVAS.blit(Image.FLAME_LASER, (config.center_x -
                           Image.FLAME_LASER.get_width()//2, 360))
        config.CANVAS.blit(Image.PLAYER_SPACE_SHIP, (config.center_x-46, 575))
        config.CANVAS.blit(Image.PLAYER_LASER, (config.center_x -
                           Image.PLAYER_LASER.get_width()//2, 490))

        mouse_btn.draw()
        keyboard_btn.draw()

        title_label = title_font.render('Start Game', 1, Colors.WHITE)
        config.CANVAS.blit(title_label, (config.center_x-title_label.get_width()//2,
                                         config.center_y-title_label.get_height() + 25))

        # Control Page
        control_btn.draw()

        # ScoreBoard Page
        trophy_btn.draw()

        # Settings Page
        settings_btn.draw()

        # Ships Page
        ships_btn.draw()

        audio_cfg.display_volume()

        exit_btn.draw()

        config.CANVAS.blit(Image.TITLE_LOGO, (config.center_x -
                           Image.TITLE_LOGO.get_width()//2, 50))

        pygame.display.update()
        config.framespersec.tick(config.FPS)  # capping frame rate to 60

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.VIDEORESIZE:
                if not display_cfg.fullscreen:
                    config.CANVAS = pygame.display.set_mode(
                        (event.w, event.h), pygame.RESIZABLE)
                    config.update(event.w, event.h)

            # Keyboard events
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_m:
                    audio_cfg.toggle_mute()
                if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                    audio_cfg.inc_volume(5)
                if event.key == pygame.K_MINUS:
                    audio_cfg.dec_volume(5)
                if event.key == pygame.K_f:
                    display_cfg.toggle_full_screen()

            # Mouse click events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if mouse_btn.isOver():
                        game(True)
                    if keyboard_btn.isOver():
                        game()
                    if control_btn.isOver():
                        controls()
                    if trophy_btn.isOver():
                        score_board()
                    if ships_btn.isOver():
                        ships()
                    if settings_btn.isOver():
                        settings()
                    if exit_btn.isOver():
                        run = False

            # Mouse hover events
            if event.type == pygame.MOUSEMOTION:
                if mouse_btn.isOver():
                    mouse_btn.outline = "onover"
                else:
                    mouse_btn.outline = "default"

                if keyboard_btn.isOver():
                    keyboard_btn.outline = "onover"
                else:
                    keyboard_btn.outline = "default"

                if control_btn.isOver():
                    control_btn.outline = "onover"
                else:
                    control_btn.outline = "default"

                if trophy_btn.isOver():
                    trophy_btn.outline = "onover"
                else:
                    trophy_btn.outline = "default"

                if settings_btn.isOver():
                    settings_btn.outline = "onover"
                else:
                    settings_btn.outline = "default"

                if ships_btn.isOver():
                    ships_btn.outline = "onover"
                else:
                    ships_btn.outline = "default"

                if exit_btn.isOver():
                    exit_btn.outline = "onover"
                else:
                    exit_btn.outline = "default"

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] or keys[pygame.K_q]:
            run = False

        if keys[pygame.K_c]:
            controls()

        if keys[pygame.K_s]:
            score_board()

    pygame.quit()
    sys.exit(0)


main()
