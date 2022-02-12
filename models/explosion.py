import os
import pygame

from utils.assets import Assets
from constants import Path, Sound

explosion_group = pygame.sprite.Group()


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, size=60, num_frames=8):
        super().__init__()
        self.images = []
        for num in range(0, num_frames):
            img = Assets.image.load(Path.EXPLOSION_PATH, f"tile{num:03}.png")
            img = pygame.transform.scale(img, (size, size))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0
        # different sound based on explosion size
        if size < 40:
            Sound.LASER_HIT_SOUND.play()
        else:
            Sound.EXPLODE_SOUND.play()

    def update(self):
        explosion_speed = 4
        # update explosion animation
        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        # if the animation is complete, reset animation index
        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()
