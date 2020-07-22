import pygame
import time
import random

from models.ship import Player, Enemy
from utils.collide import collide

from constants import WIDTH, HEIGHT, BG, CANVAS

def game():
    run = True
    FPS = 60
    lives = 5
    level = 0
    player_vel = 5
    laser_vel = 10

    main_font = pygame.font.SysFont('comicsans', 50)
    lost_font = pygame.font.SysFont('robotoblack', 60)
    win_font = pygame.font.SysFont('comicsans', 70)

    enemies = []
    wave_length = 0
    enemy_vel = 1

    player = Player(300, 585)

    clock = pygame.time.Clock()

    lost = False
    win = False
    boss_entry = True

    def redraw_window():
        CANVAS.blit(BG, (0, 0))

        # Draw Text
        level_label = main_font.render(f'Level: {level}', 1, (255, 255, 255))
        lives_label = main_font.render(f'Lives: {lives}', 1, (255, 255, 255))

        CANVAS.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        CANVAS.blit(lives_label, (10, 10))

        player.draw(CANVAS)

        for enemyShip in enemies:
            enemyShip.draw(CANVAS)

        if win:
            win_label = win_font.render('WINNER :)', 1, (0, 209, 0))
            CANVAS.blit(win_label, (WIDTH//2 - win_label.get_width()//2, 350))

        if lost:
            lost_label = lost_font.render('GAME OVER :(', 1, (255, 0, 0))
            CANVAS.blit(lost_label, (WIDTH//2 - lost_label.get_width()//2, 350))

        if level >= 10 and boss_entry:
            last_label = lost_font.render('BOSS LEVEL!!', 1, (255, 0, 0))
            CANVAS.blit(last_label, (WIDTH//2 - last_label.get_width()//2, 350))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives > 0:
            if player.health <= 0:
                lives -= 1
                player.health = 100
        else:
            lost = True
            redraw_window()
            time.sleep(3)
            run = False

        if level == 10 and boss_entry:
            redraw_window()
            time.sleep(2)
            boss_entry = False
        elif level > 10:
            win = True
            redraw_window()
            time.sleep(3)
            run = False

        if len(enemies) == 0:
            level += 5
            wave_length += 4

            for i in range(wave_length if level < 10 else 1):
                enemies.append(Enemy(
                    random.randrange(50, WIDTH - 100),
                    random.randrange(-1200, -100),
                    random.choice(['easy', 'medium', 'hard']) if level < 10 else 'boss')
                )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()

        # Return to main page
        if keys[pygame.K_BACKSPACE]:
            run = False

        # Left Key
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and (player.x - player_vel) > 0:
            player.x -= player_vel
        # Right Key
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and (player.x + player_vel + player.get_width()) < WIDTH:
            player.x += player_vel
        # Up Key
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and (player.y - player_vel) > 0:
            player.y -= player_vel
        # Down Key
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and (player.y + player_vel + player.get_height()) < HEIGHT:
            player.y += player_vel
        # Shoot Laser
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, 2 * FPS) == 1:
                enemy.shoot()

            if collide(enemy, player):
                if enemy.ship_type == 'boss':
                    if enemy.boss_max_health - 5 <= 0:
                        enemies.remove(enemy)
                        enemy.boss_max_health = 100
                        player.health -= 100
                    else:
                        enemy.boss_max_health -= 5
                        player.health -= 100
                else:
                    player.health -= 10
                    enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_vel, enemies)