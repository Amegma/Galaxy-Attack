import pygame
import os
import time
import random

from models.ship import Player, Enemy
from utils.collide import collide
from constants import TITLE, WIDTH, HEIGHT

pygame.font.init()

# Load Control Image
controlImage = pygame.image.load(os.path.join('assets', 'joystick.png'))

# Load Background Image
backgroundImage = pygame.image.load(os.path.join('assets', 'background-black.png'))

# Canvas Dimensions
CANVAS = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# Set Background Dimensions
BG = pygame.transform.scale(backgroundImage, (WIDTH, HEIGHT))

def main():
    run = True
    FPS = 60
    lives = 5
    level = 0
    player_vel = 5
    laser_vel = 10

    main_font = pygame.font.SysFont('comicsans', 50)
    lost_font = pygame.font.SysFont('robotoblack', 60)

    enemies = []
    wave_length = 0
    enemy_vel = 1

    player = Player(300, 585)

    clock = pygame.time.Clock()

    lost = False

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

        if lost:
            lost_label = lost_font.render('GAME OVER :(', 1, (255, 0, 0))
            CANVAS.blit(lost_label, (WIDTH//2 - lost_label.get_width()//2, 350))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives > 0 >= player.health:
            lives -= 1
            player.health = 100

        if lives <= 0:
            lost = True
            redraw_window()
            time.sleep(3)
            run = False

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(
                    random.randrange(50, WIDTH - 100),
                    random.randrange(-1200, -100),
                    random.choice(['red', 'blue', 'green'])
                )
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
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

            if random.randrange(0, 2 * 60) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_vel, enemies)

def controls():
    run = True

    control_title_font = pygame.font.SysFont('comicsans', 60)
    control_font = pygame.font.SysFont('comicsans', 40)
    keys_font = pygame.font.SysFont('comicsans', 40)

    while run:
        CANVAS.blit(BG, (0, 0))

        control_title_label = control_title_font.render('Controls', 1, (0, 0, 209))
        CANVAS.blit(control_title_label, (WIDTH//2 - control_title_label.get_width()//2 - 30, 175))
        CANVAS.blit(controlImage, (WIDTH//2 + control_title_label.get_width()//2 - 10, 152))

        shoot_label = control_font.render('Shoot', 1, (0, 225, 0))
        CANVAS.blit(shoot_label, (125, 255))
        shoot_key_label = keys_font.render('[spacebar]', 1, (240, 0, 0))
        CANVAS.blit(shoot_key_label, (470, 255))

        shoot_label = control_font.render('Move Left', 1, (0, 225, 0))
        CANVAS.blit(shoot_label, (125, 310))
        shoot_key_label = keys_font.render('[left] or [a]', 1, (240, 0, 0))
        CANVAS.blit(shoot_key_label, (470, 310))

        shoot_label = control_font.render('Move Right', 1, (0, 225, 0))
        CANVAS.blit(shoot_label, (125, 365))
        shoot_key_label = keys_font.render('[right] or [d]', 1, (240, 0, 0))
        CANVAS.blit(shoot_key_label, (470, 365))

        shoot_label = control_font.render('Move Down', 1, (0, 225, 0))
        CANVAS.blit(shoot_label, (125, 420))
        shoot_key_label = keys_font.render('[down] or [s]', 1, (240, 0, 0))
        CANVAS.blit(shoot_key_label, (470, 420))

        shoot_label = control_font.render('Move Up', 1, (0, 225, 0))
        CANVAS.blit(shoot_label, (125, 475))
        shoot_key_label = keys_font.render('[up] or [w]', 1, (240, 0, 0))
        CANVAS.blit(shoot_key_label, (470, 475))

        control_title_label = control_font.render('[BackSpace]', 1, (255, 255, 255))
        CANVAS.blit(control_title_label, (30, 30))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_BACKSPACE]:
            run = False

def main_menu():
    title_font = pygame.font.SysFont('comicsans', 70)
    sub_title_font = pygame.font.SysFont('robotoblack', 20)
    control_font = pygame.font.SysFont('segoeuiblack', 30)

    run = True
    while run:
        CANVAS.blit(BG, (0, 0))

        title_label = title_font.render('Start the Game :)', 1, (0, 209, 0))
        CANVAS.blit(title_label, (WIDTH//2 - title_label.get_width()//2, 350))
        sub_title_label = sub_title_font.render('PRESS ENTER', 1, (249, 166, 2))
        CANVAS.blit(sub_title_label, (WIDTH//2 - sub_title_label.get_width()//2, 410))

        # Control Page
        control_label = control_font.render('Controls [c]', 1, (255, 255, 255))
        CANVAS.blit(control_label, (30, 15))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_c]:
            controls()

        if keys[pygame.K_RETURN]:
            main()
    pygame.quit()

main_menu()