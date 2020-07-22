import pygame

from models.laser import Laser
from constants import HEIGHT, EASY_SPACE_SHIP, MEDIUM_SPACE_SHIP, HARD_SPACE_SHIP, PLAYER_SPACE_SHIP, PLAYER_LASER, RED_LASER, BLUE_LASER, GREEN_LASER

class Ship:
    CoolDown = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        self.coolDown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def coolDown(self):
        if self.cool_down_counter >= self.CoolDown:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = PLAYER_SPACE_SHIP
        self.laser_img = PLAYER_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_lasers(self, vel, objs):
        self.coolDown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.healthBar(window)

    def healthBar(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + self.ship_img.get_height() + 10, int(self.ship_img.get_width()), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.ship_img.get_height() + 10, int(self.ship_img.get_width() * (self.health/self.max_health)), 10))

class Enemy(Ship):
    TYPE_MODE = {
        'easy': (EASY_SPACE_SHIP, RED_LASER),
        'medium': (MEDIUM_SPACE_SHIP, BLUE_LASER),
        'hard': (HARD_SPACE_SHIP, GREEN_LASER)
    }

    def __init__(self, x, y, ship_type, damage=10, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.TYPE_MODE[ship_type]
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.damage = damage

    def move(self, vel):
        self.y += vel

    def move_lasers(self, vel, obj):
        self.coolDown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= self.damage
                self.lasers.remove(laser)

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x - 10, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1