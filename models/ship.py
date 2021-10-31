import pygame
from models.laser import Laser
from screens.background import slow_bg_obj
from screens.controls import audio_cfg
from constants import HEIGHT, \
    WIDTH, \
    EASY_SPACE_SHIP, \
    MEDIUM_SPACE_SHIP, \
    HARD_SPACE_SHIP, \
    PLAYER_SPACE_SHIP, \
    BOSS_SHIP, \
    FLAME_LASER, \
    PLAYER_LASER, \
    RED_LASER, \
    BLUE_LASER, \
    GREEN_LASER, \
    PLAYER_LASER_SOUND, \
    ENEMY_LASER_SOUND, \
    MENU_MUSIC_PATH


class Ship:
    CoolDown = 25
    boss_max_health = 99
    SCORE = 0

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        # drawing lasers before the ship so that it doesn't appea
        # like the lasers appear from above the ship
        for laser in self.lasers:
            laser.draw(window)

        # making ship's coordinates centered in the sprite
        background_width = slow_bg_obj.rectBGimg.width
        screen_rect = window.get_rect()
        center_x = screen_rect.centerx
        starting_x = center_x - background_width//2
        x_offset, y_offset = self.ship_img.get_size()
        window.blit(self.ship_img, (starting_x+self.x-x_offset/2, self.y-y_offset/2))

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
            PLAYER_LASER_SOUND.play()
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

    def get_score(self):
        return self.SCORE

class Player(Ship):
    def __init__(self, x, y, health=100, mouse_movement = False):
        super().__init__(x, y, health)
        self.ship_img = PLAYER_SPACE_SHIP
        self.laser_img = PLAYER_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        self.mouse_movement = mouse_movement
        self.run  = True
        self.vel = 5

    def move_with_keyboard(self):
        keys = pygame.key.get_pressed()
        action = {'LEFT' : keys[pygame.K_LEFT] or keys[pygame.K_a],
                'RIGHT' : keys[pygame.K_RIGHT] or keys[pygame.K_d],
                'UP' : keys[pygame.K_UP] or keys[pygame.K_w],
                'DOWN' : keys[pygame.K_DOWN] or keys[pygame.K_s],
                'SHOOT': keys[pygame.K_SPACE],
                'QUIT': keys[pygame.K_BACKSPACE]}
        
         # Return to main page
        if action['QUIT']:
            audio_cfg.play_music(MENU_MUSIC_PATH)
            self.run = False
        # Left Key
        if action['LEFT'] and (self.x - self.vel) > self.get_width()/2:
            self.x -= self.vel
        # Right Key
        if action['RIGHT'] and (self.x + self.vel + self.get_width()/2) < WIDTH:
            self.x += self.vel
        # Up Key
        if action['UP'] and (self.y - self.vel) > 0:
            self.y -= self.vel
        # Down Key
        if action['DOWN'] and (self.y + self.vel + self.get_height()) < HEIGHT:
            self.y += self.vel
        # Shoot Laser
        if action['SHOOT']:
            self.shoot()

    def move_with_mouse(self):
        cx, cy = pygame.mouse.get_pos()
        button = pygame.mouse.get_pressed()        
        keys = pygame.key.get_pressed()
        # Movement
        if cx > self.get_width()/2 and cx < WIDTH - self.get_width()/2 \
            and cy > 0 and cy < HEIGHT :
            self.x = cx
            self.y = cy
        # Shoot Laser
        if  button[0] or keys[pygame.K_SPACE]:
            self.shoot()
        # Return to main page
        if button[2] or keys[pygame.K_BACKSPACE]:
            audio_cfg.play_music(MENU_MUSIC_PATH)
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
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        self.SCORE += 50
                        if obj.ship_type == 'boss':
                            if self.boss_max_health - 10 <= 0:
                                objs.remove(obj)
                                self.boss_max_health = 100
                            else:
                                self.boss_max_health -= 10
                        else:
                            objs.remove(obj)

                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.healthBar(window)

    def healthBar(self, window):
        background_width = slow_bg_obj.rectBGimg.width
        screen_rect = window.get_rect()
        center_x = screen_rect.centerx
        starting_x = center_x - background_width//2
        x_offset, y_offset = self.ship_img.get_size()
        pygame.draw.rect(window, (255, 0, 0), (starting_x + self.x - x_offset/2,
                                               self.y + y_offset/2 + 10,
                                               int(self.ship_img.get_width()),
                                               10))
        pygame.draw.rect(window, (0, 255, 0), (starting_x + self.x - x_offset/2,
                                               self.y + y_offset/2 + 10,
                                               int(self.ship_img.get_width() * (self.health/self.max_health)),
                                               10))

class Enemy(Ship):
    TYPE_MODE = {
        'easy': (EASY_SPACE_SHIP, RED_LASER, 10),
        'medium': (MEDIUM_SPACE_SHIP, BLUE_LASER, 18),
        'hard': (HARD_SPACE_SHIP, GREEN_LASER, 25),
        'boss': (BOSS_SHIP, FLAME_LASER, 100)
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
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= self.damage
                self.lasers.remove(laser)

    def shoot(self):
        if self.cool_down_counter == 0 and self.y > 0:
            ENEMY_LASER_SOUND.play()
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
