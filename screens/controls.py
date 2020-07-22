import pygame
import os

from constants import WIDTH, HEIGHT

# Load Control Image
controlImage = pygame.image.load(os.path.join('assets', 'joystick.png'))

# Load Background Image
backgroundImage = pygame.image.load(os.path.join('assets', 'background-black.png'))

# Set Background Dimensions
BG = pygame.transform.scale(backgroundImage, (WIDTH, HEIGHT))

# Canvas Dimensions
CANVAS = pygame.display.set_mode((WIDTH, HEIGHT))

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