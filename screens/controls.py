import pygame
import sys

from .background import slow_bg_obj
from utils.assets import Assets
from models.icon_button import IconButton
from models.controls import audio_cfg, display_cfg
from config import config
from constants import Image, Font, Colors, Text


def controls():
    run = True

    control_title_font = pygame.font.Font(Font.edit_undo_font, 50)
    control_font = pygame.font.Font(Font.neue_font, 30)
    keys_font = pygame.font.Font(Font.neue_font, 30)

    go_back_btn = IconButton(Image.GO_BACK_IMAGE, (config.starting_x + 65, 50))

    while run:
        slow_bg_obj.update()
        slow_bg_obj.render()

        Assets.text.draw(Text.CONTROLS, control_title_font, Colors.BLUE,
                         (config.center_x - 30, 130), True)
        Assets.image.draw(Image.CONTROL_IMAGE, (config.center_x + 95, 120))

        Assets.text.draw('Shoot', control_font, Colors.GREEN,
                         (config.starting_x + 125, 215))
        Assets.text.draw('[spacebar]', keys_font, Colors.RED,
                         (config.starting_x + 470, 215))

        Assets.text.draw('Move Left', control_font, Colors.GREEN,
                         (config.starting_x + 125, 270))
        Assets.text.draw('[left] or [a]', keys_font, Colors.RED,
                         (config.starting_x + 470, 270))

        Assets.text.draw('Move Right', control_font, Colors.GREEN,
                         (config.starting_x + 125, 325))
        Assets.text.draw('[right] or [d]', keys_font, Colors.RED,
                         (config.starting_x + 470, 325))

        Assets.text.draw('Move Down', control_font, Colors.GREEN,
                         (config.starting_x + 125, 380))
        Assets.text.draw('[down] or [s]', keys_font, Colors.RED,
                         (config.starting_x + 470, 380))

        Assets.text.draw('Move Up', control_font, Colors.GREEN,
                         (config.starting_x + 125, 435))
        Assets.text.draw('[up] or [w]', keys_font, Colors.RED,
                         (config.starting_x + 470, 435))

        Assets.text.draw('Return back to home', control_font, Colors.GREEN,
                         (config.starting_x + 125, 490))
        Assets.text.draw('[backspace]', keys_font, Colors.RED,
                         (config.starting_x + 470, 490))

        Assets.text.draw('Mute Audio', control_font, Colors.GREEN,
                         (config.starting_x + 125, 545))
        Assets.text.draw('[m]', keys_font, Colors.RED,
                         (config.starting_x + 470, 545))

        Assets.text.draw('Volume Up/Down', control_font, Colors.GREEN,
                         (config.starting_x + 125, 600))
        Assets.text.draw('[+]/[-]', keys_font, Colors.RED,
                         (config.starting_x + 470, 600))

        Assets.text.draw('Toggle Full Screen', control_font, Colors.GREEN,
                         (config.starting_x + 125, 655))
        Assets.text.draw('[f]', keys_font, Colors.RED,
                         (config.starting_x + 470, 655))

        go_back_btn.draw()

        audio_cfg.display_volume()

        pygame.display.update()
        config.clock.tick(config.FPS)

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
