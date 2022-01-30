from config import config
from constants import Colors
import pygame
pygame.init()

# ships_title_font = pygame.font.Font(Font.edit_undo_font, 50)
font = pygame.font.SysFont("Verdana", 12)


class Slider():
    def __init__(self, name, val, maxi, mini, pos):
        self.val = val  # start value
        self.maxi = maxi  # maximum at slider position right
        self.mini = mini  # minimum at slider position left
        self.xpos = pos  # x-location on screen
        self.ypos = 250
        self.surf = pygame.surface.Surface((200, 50))
        self.hit = False  # the hit attribute indicates slider movement due to mouse interaction

        # Static graphics - slider background #
        # self.surf.fill((100, 100, 100))
        pygame.draw.rect(self.surf, Colors.WHITE, [10, 30, 160, 5], 0)

        # dynamic graphics - button surface #
        self.button_surf = pygame.surface.Surface((20, 20))
        self.button_surf.fill(Colors.TRANS)
        self.button_surf.set_colorkey(Colors.TRANS)
        pygame.draw.circle(self.button_surf, Colors.BLACK, (10, 10), 6, 0)
        pygame.draw.circle(self.button_surf, Colors.WHITE, (10, 10), 4, 0)

    def draw(self):
        """ Combination of static and dynamic graphics in a copy of
    the basic slide surface
    """
        # static
        surf = self.surf.copy()

        # dynamic
        pos = (10+int((self.val-self.mini)/(self.maxi-self.mini)*100), 33)
        self.button_rect = self.button_surf.get_rect(center=pos)
        surf.blit(self.button_surf, self.button_rect)
        # move of button box to correct screen position
        self.button_rect.move_ip(self.xpos, self.ypos)

        # screen
        config.CANVAS.blit(surf, (self.xpos, self.ypos))

    def move(self):
        """
    The dynamic part; reacts to movement of the slider button.
    """
        self.val = (pygame.mouse.get_pos()[
                    0] - self.xpos - 10) / 80 * (self.maxi - self.mini) + self.mini
        if self.val < self.mini:
            self.val = self.mini
        if self.val > self.maxi:
            self.val = self.maxi
