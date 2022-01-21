import os
import pygame
import time
import random

from models.ship import Player, Enemy
from models.explosion import Explosion, explosion_group
from models.controls import audio_cfg, display_cfg
from utils.collide import collide
from .background import bg_obj

from constants import Config, \
    HEART_IMAGE,\
    score_list,\
    neue_font,\
    edit_undo_font,\
    MENU_MUSIC_PATH,\
    GAME_MUSIC_PATH


def game(isMouse=False):
    lives = 5
    level = 0
    laser_vel = 10

    main_font = pygame.font.Font(edit_undo_font, 50)
    sub_font = pygame.font.Font(neue_font, 40)
    sub_small_font = pygame.font.Font(neue_font, 35)
    lost_font = pygame.font.Font(edit_undo_font, 55)
    win_font = pygame.font.Font(edit_undo_font, 55)

    # load and play ingame music
    audio_cfg.play_music(GAME_MUSIC_PATH)

    enemies = []
    wave_length = 0
    enemy_vel = 1

    player = Player(300, 585, mouse_movement=isMouse)
    pygame.mouse.set_visible(False)

    lost = False
    win = False
    boss_entry = True
    pause = False

    explosion_group.empty()

    def redraw_window(pause=False):
        if not pause:
            bg_obj.update()
        bg_obj.render(Config.CANVAS)

        # Draw Text
        level_label = sub_small_font.render(f'{level} / 10', 1, (0, 255, 255))
        score_label = sub_font.render(f'{player.get_score()}', 1, (0, 255, 0))

        player.draw(Config.CANVAS)

        for enemyShip in enemies:
            enemyShip.draw(Config.CANVAS)

        # blit player stats after enemyShips to prevent the later
        # from being drawn over the stats

        # Lives
        for index in range(1, lives + 1):
            Config.CANVAS.blit(
                HEART_IMAGE, (Config.starting_x + 37 * index - 10, 20))

        # blit stats
        Config.CANVAS.blit(level_label, (Config.starting_x + 35, 75))
        Config.CANVAS.blit(
            score_label, (Config.ending_x - score_label.get_width() - 30, 20))

        if win:
            score_list.append(player.get_score())
            win_label = win_font.render('WINNER :)', 1, (0, 209, 0))
            Config.CANVAS.blit(win_label, (Config.center_x -
                                           win_label.get_width()//2, 350))

        if lost:
            score_list.append(player.get_score())
            lost_label = lost_font.render('GAME OVER :(', 1, (255, 0, 0))
            Config.CANVAS.blit(lost_label, (Config.center_x -
                                            lost_label.get_width()//2, 350))

        if level >= 10 and boss_entry:
            last_label = lost_font.render('BOSS LEVEL!!', 1, (255, 0, 0))
            Config.CANVAS.blit(last_label, (Config.center_x -
                                            last_label.get_width()//2, 350))

        if pause:
            # if paused display the "game is paused" screen
            pause_label = main_font.render('Game Paused', 1, (0, 255, 255))
            Config.CANVAS.blit(pause_label, (Config.center_x -
                                             pause_label.get_width()//2, 350))

            key_msg = sub_font.render('Press [p] to unpause', 1, (0, 0, 255))
            Config.CANVAS.blit(key_msg, (Config.center_x -
                                         key_msg.get_width()//2, 400))

        # explosion group
        explosion_group.draw(Config.CANVAS)
        explosion_group.update()

        audio_cfg.display_volume(Config.CANVAS)
        pygame.display.update()
        Config.framespersec.tick(Config.FPS)

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
                    random.randrange(50, Config.WIDTH - 100),
                    random.randrange(-1200, -100),
                    random.choice(['easy', 'medium', 'hard']) if level < 10 else 'boss')
                )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    pygame.mouse.set_visible(True)
                    pause = True
                if event.key == pygame.K_m:
                    audio_cfg.toggle_mute()
                if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                    audio_cfg.inc_volume(5)
                if event.key == pygame.K_MINUS:
                    audio_cfg.dec_volume(5)
                if event.key == pygame.K_f:
                    display_cfg.toggle_full_screen()

        while pause:
            # create a fresh screen
            redraw_window(pause)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_BACKSPACE:
                        player.run = False
                        pause = False
                        audio_cfg.play_music(MENU_MUSIC_PATH)
                        break
                    if event.key == pygame.K_m:
                        audio_cfg.toggle_mute()
                    if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                        audio_cfg.inc_volume(5)
                    if event.key == pygame.K_MINUS:
                        audio_cfg.dec_volume(5)
                    if event.key == pygame.K_p:
                        pygame.mouse.set_visible(False)
                        pause = False
                        break

        player.move()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, 2 * Config.FPS) == 1:
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
            elif enemy.y + enemy.get_height()/2 > Config.HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_vel, enemies)
