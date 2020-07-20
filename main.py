import pygame
import os
import time
import random
pygame.font.init()

# Load Enemy Ships
RED_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_red_small.png'))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_blue_small.png'))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_green_small.png'))

# Load Player Ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_yellow.png'))

# Load Lasers
RED_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_red.png'))
BLUE_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_blue.png'))
GREEN_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_green.png'))
YELLOW_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_yellow.png'))

# Load Background Image
backgroundImage = pygame.image.load(os.path.join('assets', 'background-black.png'))

# Canvas Dimensions
WIDTH, HEIGHT = 600, 600
CANVAS = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SPACE INVADERS')

# Set Background Dimensions
BG = pygame.transform.scale(backgroundImage, (WIDTH, HEIGHT))

class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
        self.width = 50
        self.height = 50

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, self.width, self.height))

def main():
    run = True
    FPS = 60
    lives = 5
    level = 1
    player_vel = 5
    main_font = pygame.font.SysFont('comicsans', 35)

    ship = Ship(WIDTH//2 - 25, 500)

    clock = pygame.time.Clock()

    def redraw_window():
        CANVAS.blit(BG, (0, 0))
        # Draw Text
        level_label = main_font.render(f'Level: {level}', 1, (255, 255, 255))
        lives_label = main_font.render(f'Lives: {lives}', 1, (255, 255, 255))

        CANVAS.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        CANVAS.blit(lives_label, (10, 10))

        ship.draw(CANVAS)

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and (ship.x - player_vel) > 0:  # Left Key
            ship.x -= player_vel
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and (ship.x + player_vel + ship.width) < WIDTH:  # Right Key
            ship.x += player_vel
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and (ship.y - player_vel) > 0:  # Up Key
            ship.y -= player_vel
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and (ship.y + player_vel + ship.height) < HEIGHT:  # Down Key
            ship.y += player_vel


main()