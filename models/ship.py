import pygame

from utils.assets import Assets
from models.laser import Laser
from models.explosion import Explosion, explosion_group
from models.controls import audio_cfg
from models.scores import scores
from config import config
from constants import Path, Image, Colors, Sound


class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
        self.CoolDown = 25
        self.boss_max_health = 99
        self.SCORE = 0
        self.KILLS = 0
        self.level = 0

    def draw(self):
        # drawing lasers before the ship so that it doesn't appea
        # like the lasers appear from above the ship
        for laser in self.lasers:
            laser.draw()

        # making ship's coordinates centered in the sprite
        Assets.image.draw(
            self.ship_img, (config.starting_x+self.x, self.y), True, True)

    def move_lasers(self, vel, obj):
        self.coolDown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(config.HEIGHT):
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
            Sound.PLAYER_LASER_SOUND.play()
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

    def get_score(self):
        return self.SCORE

    def get_kills(self):
        return self.KILLS

    def get_level(self):
        return self.level

    def set_level(self):
        self.level += 1


class Player(Ship):
    def __init__(self, x, y, health=100, mouse_movement=False):
        super().__init__(x, y, health)
        self.ship_img = Image.PLAYER_SPACE_SHIP
        self.laser_img = Image.PLAYER_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        self.mouse_movement = mouse_movement
        self.run = True
        self.vel = 5

    def move_with_keyboard(self):
        keys = pygame.key.get_pressed()
        action = {'LEFT': keys[pygame.K_LEFT] or keys[pygame.K_a],
                  'RIGHT': keys[pygame.K_RIGHT] or keys[pygame.K_d],
                  'UP': keys[pygame.K_UP] or keys[pygame.K_w],
                  'DOWN': keys[pygame.K_DOWN] or keys[pygame.K_s],
                  'SHOOT': keys[pygame.K_SPACE],
                  'QUIT': keys[pygame.K_BACKSPACE]}

        # Return to main page
        if action['QUIT']:
            audio_cfg.play_music(Path.MENU_MUSIC_PATH)
            self.run = False
        # Left Key
        if action['LEFT'] and (self.x - self.vel) > self.get_width()/2:
            self.x -= self.vel
        # Right Key
        if action['RIGHT'] and (self.x + self.vel + self.get_width()/2) < config.WIDTH:
            self.x += self.vel
        # Up Key
        if action['UP'] and (self.y - self.vel) > 0:
            self.y -= self.vel
        # Down Key
        if action['DOWN'] and (self.y + self.vel + self.get_height()) < config.HEIGHT:
            self.y += self.vel
        # Shoot Laser
        if action['SHOOT']:
            self.shoot()

    def move_with_mouse(self):
        cx, cy = pygame.mouse.get_pos()
        button = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        # Movement
        if cx > self.get_width()/2 and cx < config.WIDTH - self.get_width()/2 \
                and cy > 0 and cy < config.HEIGHT:
            self.x = cx
            self.y = cy
        # Shoot Laser
        if button[0] or keys[pygame.K_SPACE]:
            self.shoot()
        # Return to main page
        if button[2] or keys[pygame.K_BACKSPACE]:
            score_obj = {
                "status": False,
                "level": self.get_level(),
                "score": self.get_score(),
                "kills": self.get_kills(),
            }
            scores.append(False, self.get_level(), self.get_score(), self.get_kills())
            audio_cfg.play_music(Path.MENU_MUSIC_PATH)
            self.run = False

    def move(self):
        if(self.mouse_movement):
            self.move_with_mouse()
        else:
            self.move_with_keyboard()

    def move_lasers(self, vel, objs):
        self.coolDown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(config.HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        if obj.ship_type == 'boss':
                            if self.boss_max_health - 10 <= 0:
                                self.SCORE += 1000
                                self.KILLS += 1
                                objs.remove(obj)
                                self.boss_max_health = 100
                            else:
                                self.boss_max_health -= 10
                        else:
                            self.SCORE += 50
                            self.KILLS += 1
                            # enemy ship death explosion
                            explosion = Explosion(obj.x, obj.y)
                            explosion_group.add(explosion)
                            objs.remove(obj)

                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self):
        super().draw()
        self.healthBar()

    def healthBar(self):
        x_offset, y_offset = self.ship_img.get_size()
        pygame.draw.rect(config.CANVAS, Colors.RED, (config.starting_x + self.x -
                         x_offset/2, self.y + y_offset/2 + 10, int(self.ship_img.get_width()), 10))
        pygame.draw.rect(config.CANVAS, Colors.GREEN, (config.starting_x + self.x - x_offset/2, self.y +
                         y_offset/2 + 10, int(self.ship_img.get_width() * (self.health/self.max_health)), 10))


class Enemy(Ship):
    TYPE_MODE = {
        'easy': (Image.EASY_SPACE_SHIP, Image.RED_LASER, 10),
        'medium': (Image.MEDIUM_SPACE_SHIP, Image.BLUE_LASER, 18),
        'hard': (Image.HARD_SPACE_SHIP, Image.GREEN_LASER, 25),
        'boss': (Image.BOSS_SHIP, Image.FLAME_LASER, 100)
    }

    ship_type = ''

    def __init__(self, x, y, ship_type, health=100):
        super().__init__(x, y, health)
        self.ship_type = ship_type
        self.ship_img, self.laser_img, self.damage = self.TYPE_MODE[self.ship_type]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel

    def move_lasers(self, vel, obj):
        self.coolDown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(config.HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                # display collisions if enemy lasers hit the player
                sm_explosion = Explosion(laser.x, laser.y, size=30)
                explosion_group.add(sm_explosion)
                obj.health -= self.damage
                self.lasers.remove(laser)

    def shoot(self):
        if self.cool_down_counter == 0 and self.y > 0:
            Sound.ENEMY_LASER_SOUND.play()
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
