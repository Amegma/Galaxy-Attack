import pygame

from screens.game import game
from screens.controls import controls
from constants import TITLE,\
    WIDTH,\
    BOSS_SHIP,\
    PLAYER_SPACE_SHIP,\
    PLAYER_LASER,\
    startImage,\
    controlImage,\
    trophyImage,\
    BG,\
    CANVAS

pygame.font.init()

pygame.display.set_caption(TITLE)

def main():
    title_font = pygame.font.SysFont('comicsans', 70)
    sub_title_font = pygame.font.SysFont('comicsans', 30)
    control_font = pygame.font.SysFont('comicsans', 40)

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
        CANVAS.blit(control_label, (90, 35))
        CANVAS.blit(controlImage, (30, 15))

        # ScoreBoard Page
        score_label = control_font.render('[s]', 1, (255, 255, 255))
        CANVAS.blit(score_label, (WIDTH - 67, 35))
        CANVAS.blit(trophyImage, (WIDTH - 130, 25))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            run = False

        if keys[pygame.K_c]:
            controls()

        if keys[pygame.K_RETURN]:
            game()

    pygame.quit()

main()