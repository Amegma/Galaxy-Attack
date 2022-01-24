import pygame
import sys

from .background import slow_bg_obj
from models.icon_button import IconButton
from models.controls import audio_cfg, display_cfg
from config import config
from constants import Image, Font


def settings():
    characters_title_font = pygame.font.Font(Font.edit_undo_font, 50)

    go_back_btn = IconButton(Image.GO_BACK_IMAGE, (config.starting_x + 30, 30))

    run = True
    while run:
        slow_bg_obj.update()
        slow_bg_obj.render()

        characters_title_label = characters_title_font.render(
            "Settings", 1, (255, 255, 0))
        config.CANVAS.blit(characters_title_label, (config.center_x -
                                                    characters_title_label.get_width()//2, 130))
        config.CANVAS.blit(Image.TOOLS_IMAGE, (config.center_x -
                                               Image.TOOLS_IMAGE.get_width()//2 - 170, 120))
        config.CANVAS.blit(Image.TOOLBOX_IMAGE, (config.center_x -
                                                 Image.TOOLBOX_IMAGE.get_width()//2 + 170, 129))

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
