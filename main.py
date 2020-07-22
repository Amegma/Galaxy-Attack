import pygame
import os

from screens.game import game
from screens.controls import controls
from constants import TITLE, WIDTH, HEIGHT

pygame.font.init()

# Load Control Image
startImage = pygame.image.load(os.path.join('assets', 'play.png'))

# Load Control Image
controlImage = pygame.image.load(os.path.join('assets', 'joystick.png'))

# Load ScoreBoard Image
trophyImage = pygame.image.load(os.path.join('assets', 'trophy.png'))

# Load Boss Ship
BOSS_SHIP = pygame.image.load(os.path.join('assets', 'boss.png'))

# Load Player
PLAYER_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'retro-spaceship.png'))
PLAYER_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_cosmic.png'))

# Load Background Image
backgroundImage = pygame.image.load(os.path.join('assets', 'background-black.png'))

# Set Background Dimensions
BG = pygame.transform.scale(backgroundImage, (WIDTH, HEIGHT))

# Canvas Dimensions
CANVAS = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

def main():
    title_font = pygame.font.SysFont('comicsans', 70)
    sub_title_font = pygame.font.SysFont('robotoblack', 20)
    control_font = pygame.font.SysFont('segoeuiblack', 30)

    run = True
    while run:
        CANVAS.blit(BG, (0, 0))

        title_label = title_font.render('Start the Game', 1, (0, 209, 0))
        CANVAS.blit(title_label, (WIDTH//2 - title_label.get_width()//2 - 15, 350))
        CANVAS.blit(startImage, (WIDTH//2 + title_label.get_width()//2, 351))
        sub_title_label = sub_title_font.render('PRESS ENTER', 1, (249, 166, 2))
        CANVAS.blit(sub_title_label, (WIDTH//2 - sub_title_label.get_width()//2, 410))

        # Ships
        CANVAS.blit(BOSS_SHIP, (285, 75))
        CANVAS.blit(PLAYER_SPACE_SHIP, (WIDTH//2 - 50, 575))
        CANVAS.blit(PLAYER_LASER, (WIDTH//2 - 50, 475))

        # Control Page
        control_label = control_font.render('[c]', 1, (255, 255, 255))
        CANVAS.blit(control_label, (90, 25))
        CANVAS.blit(controlImage, (30, 15))

        # ScoreBoard Page
        score_label = control_font.render('[s]', 1, (255, 255, 255))
        CANVAS.blit(score_label, (WIDTH - 67, 25))
        CANVAS.blit(trophyImage, (WIDTH - 130, 25))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_c]:
            controls()

        if keys[pygame.K_RETURN]:
            game()

    pygame.quit()

main()