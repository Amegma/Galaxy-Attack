import pygame

from config import config
from constants import Colors


def outlineImage(image, pos):
    mask = pygame.mask.from_surface(image)
    mask_outline = mask.outline()
    mask_surf = pygame.Surface(image.get_size())
    for pixel in mask_outline:
        mask_surf.set_at(pixel, Colors.WHITE)
    mask_surf.set_colorkey((0, 0, 0))

    config.CANVAS.blit(mask_surf, (pos[0], pos[1]+2))
    config.CANVAS.blit(mask_surf, (pos[0], pos[1]+1))
    config.CANVAS.blit(mask_surf, (pos[0], pos[1]-1))
    config.CANVAS.blit(mask_surf, (pos[0], pos[1]-2))
    config.CANVAS.blit(mask_surf, (pos[0]+2, pos[1]))
    config.CANVAS.blit(mask_surf, (pos[0]+1, pos[1]))
    config.CANVAS.blit(mask_surf, (pos[0]-1, pos[1]))
    config.CANVAS.blit(mask_surf, (pos[0]-2, pos[1]))
    config.CANVAS.blit(mask_surf, (pos[0]+1, pos[1]+1))
    config.CANVAS.blit(mask_surf, (pos[0]+1, pos[1]-1))
    config.CANVAS.blit(mask_surf, (pos[0]-1, pos[1]+1))
    config.CANVAS.blit(mask_surf, (pos[0]-1, pos[1]-1))
