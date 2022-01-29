import pygame
import time
import random

from models.ship import Player, Enemy
from models.explosion import Explosion, explosion_group
from models.controls import audio_cfg, display_cfg
from models.icon_button import IconButton
from utils.collide import collide
from utils.draw import draw_text
from .background import bg_obj

from config import config
from constants import Path, Image, score_list, Font, Colors

pause = False


def game(isMouse=False):
    global pause
    lives = 5
    level = 0
    laser_vel = 10

    sub_font = pygame.font.Font(Font.neue_font, 40)
    sub_small_font = pygame.font.Font(Font.neue_font, 35)
    lost_font = pygame.font.Font(Font.edit_undo_font, 55)
    win_font = pygame.font.Font(Font.edit_undo_font, 55)

    # load and play ingame music
    audio_cfg.play_music(Path.GAME_MUSIC_PATH)

    enemies = []
    wave_length = 0
    enemy_vel = 1

    player = Player(300, 585, mouse_movement=isMouse)
    pygame.mouse.set_visible(False)

    lost = False
    win = False
    boss_entry = True

    pause_btn = IconButton(
        Image.PAUSE_IMAGE, (config.center_x, 50))

    explosion_group.empty()

    def redraw_window():
        bg_obj.update()
        bg_obj.render()

        player.draw()

        for enemyShip in enemies:
            enemyShip.draw()

        pause_btn.draw()

        # Lives
        for index in range(1, lives + 1):
            config.CANVAS.blit(
                Image.HEART_IMAGE, (config.starting_x + 37 * index - 10, 30))

        # Draw Text
        draw_text(f'{level} / 10', sub_small_font, Colors.CYAN,
                  (config.starting_x + 35, 75))
        draw_text(f'{player.get_score()}', sub_font, Colors.GREEN,
                  (config.ending_x - 40, 20), True)

        if win:
            score_list.append(player.get_score())
            draw_text('WINNER :)', win_font, Colors.GREEN2,
                      (config.center_x, 350), True)

        if lost:
            score_list.append(player.get_score())
            draw_text('GAME OVER :(', lost_font, Colors.RED,
                      (config.center_x, 350), True)

        if level >= 10 and boss_entry:
            draw_text('BOSS LEVEL!!', lost_font, Colors.RED,
                      (config.center_x, 350), True)

        # explosion group
        explosion_group.draw(config.CANVAS)
        explosion_group.update()

        audio_cfg.display_volume()
        pygame.display.update()
        config.clock.tick(config.FPS)

    while player.run:
        redraw_window()
        if lives > 0:
            if player.health <= 0:
                lives -= 1
                player.health = 100
        else:
            lost = True
            redraw_window()
            time.sleep(3)
            player.run = False
            pygame.mouse.set_visible(True)

        if level == 10 and boss_entry:
            redraw_window()
            time.sleep(2)
            boss_entry = False
        elif level > 10:
            win = True
            redraw_window()
            time.sleep(3)
            player.run = False

        if len(enemies) == 0:
            level += 1
            wave_length += 4

            for i in range(wave_length if level < 10 else 1):
                enemies.append(Enemy(
                    random.randrange(50, config.WIDTH - 100),
                    random.randrange(-1200, -100),
                    random.choice(['easy', 'medium', 'hard']) if level < 10 else 'boss')
                )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if pause_btn.isOver():
                        pygame.mouse.set_visible(True)
                        pause = True
                        paused(player)

            if event.type == pygame.MOUSEMOTION:
                if pause_btn.isOver():
                    pause_btn.outline = True
                else:
                    pause_btn.outline = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    audio_cfg.toggle_mute()
                if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                    audio_cfg.inc_volume(5)
                if event.key == pygame.K_MINUS:
                    audio_cfg.dec_volume(5)
                if event.key == pygame.K_f:
                    display_cfg.toggle_full_screen()
                if event.key == pygame.K_p:
                    pygame.mouse.set_visible(True)
                    pause = True
                    paused(player)

        player.move()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, 2 * config.FPS) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.SCORE += 50
                if enemy.ship_type == 'boss':
                    if enemy.boss_max_health - 5 <= 0:
                        # note: this is not seen as game is paused as soon as boss health reaches zero
                        # should be fixed in future with a short delay in pausing
                        boss_crash = Explosion(player.x, player.y, size=100)
                        explosion_group.add(boss_crash)

                        enemies.remove(enemy)
                        enemy.boss_max_health = 100
                        player.health -= 100
                    else:
                        enemy.boss_max_health -= 5
                        player.health -= 100
                        # player death explosion
                        crash = Explosion(player.x, player.y)
                        explosion_group.add(crash)
                else:
                    player.health -= 10
                    crash = Explosion(enemy.x, enemy.y)
                    explosion_group.add(crash)
                    enemies.remove(enemy)
            elif enemy.y + enemy.get_height()/2 > config.HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_vel, enemies)


def paused(player):
    main_font = pygame.font.Font(Font.edit_undo_font, 50)
    sub_font = pygame.font.Font(Font.neue_font, 40)

    draw_text('Game Paused', main_font, Colors.CYAN,
              (config.center_x, 350), True)

    draw_text('Press [p] to unpause', sub_font, Colors.BLUE,
              (config.center_x, 400), True)

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
        config.clock.tick(15)


def unpause():
    global pause
    pause = False
