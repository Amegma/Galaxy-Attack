import pygame

from models.controls import audio_cfg
from config import config
from constants import Font, Colors, Path

# pause = False


def paused(player):
    main_font = pygame.font.Font(Font.edit_undo_font, 50)
    sub_font = pygame.font.Font(Font.neue_font, 40)

    pause_label = main_font.render('Game Paused', 1, Colors.CYAN)
    config.CANVAS.blit(pause_label, (config.center_x -
                                     pause_label.get_width()//2, 350))

    key_msg = sub_font.render('Press [p] to unpause', 1, Colors.BLUE)
    config.CANVAS.blit(key_msg, (config.center_x -
                                 key_msg.get_width()//2, 400))

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pygame.mouse.set_visible(False)
                    unpause()
                if event.key == pygame.K_BACKSPACE:
                    player.run = False
                    unpause()
                    audio_cfg.play_music(Path.MENU_MUSIC_PATH)

        pygame.display.update()
        config.framespersec.tick(15)


def unpause():
    global pause
    pause = False
