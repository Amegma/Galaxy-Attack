import os
import pygame
import argparse

from screens.game import game
from screens.controls import controls
from screens.score_board import score_board
from screens.characters import characters
from screens.background import slow_bg_obj
from models.button import Button
from models.icon_button import IconButton
from models.controls import audio_cfg, display_cfg

from constants import Config,\
    BOSS_SHIP,\
    PLAYER_SPACE_SHIP,\
    PLAYER_LASER,\
    FLAME_LASER,\
    CONTROL_IMAGE,\
    CHARACTERS_IMAGE,\
    TROPHY_IMAGE,\
    MENU_MUSIC_PATH, \
    edit_undo_font

# parsing arguments
ag = argparse.ArgumentParser()
ag.add_argument("--mute", help="disable all sounds", action="store_true")
args = vars(ag.parse_args())

if args["mute"]:
    audio_cfg.toggle_mute()

pygame.font.init()

pygame.display.set_caption(Config.TITLE)


def main():
    title_font = pygame.font.Font(edit_undo_font, 82)

    audio_cfg.play_music(MENU_MUSIC_PATH)

    # window_width = CANVAS.get_width()
    background_width = slow_bg_obj.rectBGimg.width
    starting_x = Config.center_x - background_width//2
    ending_x = Config.center_x + background_width//2

    mouse_btn = Button((7, 8, 16), (255, 255, 255),
                       (Config.center_x - 210, Config.center_y + 22), (195, 66), "MOUSE")
    keyboard_btn = Button((7, 8, 16), (255, 255, 255),
                          (Config.center_x + 15, Config.center_y + 22), (195, 66), "KEYBOARD")
    control_btn = IconButton(CONTROL_IMAGE, (starting_x + 30, 15))
    characters_btn = IconButton(CHARACTERS_IMAGE, (starting_x + 30, 110))
    trophy_btn = IconButton(TROPHY_IMAGE, (ending_x - 85, 25))

    run = True
    while run:
        pygame.mouse.set_visible(True)
        slow_bg_obj.update()
        slow_bg_obj.render(Config.CANVAS)

        # Ships
        Config.CANVAS.blit(BOSS_SHIP, (Config.center_x -
                           BOSS_SHIP.get_width()//2, 50))
        Config.CANVAS.blit(FLAME_LASER, (Config.center_x -
                           FLAME_LASER.get_width()//2, 310))
        Config.CANVAS.blit(PLAYER_SPACE_SHIP, (Config.center_x-50, 575))
        Config.CANVAS.blit(PLAYER_LASER, (Config.center_x -
                           PLAYER_LASER.get_width()//2, 475))

        mouse_btn.draw()
        keyboard_btn.draw()

        title_label = title_font.render('Start Game', 1, (255, 255, 255))
        Config.CANVAS.blit(title_label, (Config.center_x-title_label.get_width()//2,
                                         Config.center_y-title_label.get_height() + 5))

        # Control Page
        control_btn.draw()

        # ScoreBoard Page
        trophy_btn.draw()

        # Characters Page
        characters_btn.draw()

        audio_cfg.display_volume(Config.CANVAS)
        pygame.display.update()
        Config.framespersec.tick(Config.FPS)  # capping frame rate to 60

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

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
                    if characters_btn.isOver():
                        characters()

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

                if characters_btn.isOver():
                    characters_btn.outline = "onover"
                else:
                    characters_btn.outline = "default"

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] or keys[pygame.K_q]:
            run = False

        if keys[pygame.K_c]:
            controls()

        if keys[pygame.K_s]:
            score_board()

    pygame.quit()


main()
