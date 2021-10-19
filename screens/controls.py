import pygame

from constants import WIDTH,\
    controlImage,\
    BG,\
    CANVAS, \
    soundList

class AudioControls:
    def __init__(self, soundList):
        self.soundList = soundList
        self.volume = 100
        self.muted = False
        self.prev_volume = -1

        for soundItem in self.soundList:
            soundItem.set_volume(self.volume)

    def set_volume(self, level):
        self.volume = level
        for soundItem in soundList:
            soundItem.set_volume(level)

    def dec_volume(self, amt):
        amt = max(0, self.volume - amt)
        self.set_volume(amt)

    def inc_volume(self, amt):
        amt = min(100, self.volume + amt)
        self.set_volume(amt)

    def toggle_mute(self):
        if self.muted:
            self.set_volume(self.prev_volume)
            self.muted = False
        else:
            self.prev_volume = self.volume
            self.muted = True
            self.set_volume(0)

audio_cfg = AudioControls(soundList)

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

        left_label = control_font.render('Move Left', 1, (0, 225, 0))
        CANVAS.blit(left_label, (125, 310))
        left_key_label = keys_font.render('[left] or [a]', 1, (240, 0, 0))
        CANVAS.blit(left_key_label, (470, 310))

        right_label = control_font.render('Move Right', 1, (0, 225, 0))
        CANVAS.blit(right_label, (125, 365))
        right_key_label = keys_font.render('[right] or [d]', 1, (240, 0, 0))
        CANVAS.blit(right_key_label, (470, 365))

        down_label = control_font.render('Move Down', 1, (0, 225, 0))
        CANVAS.blit(down_label, (125, 420))
        down_key_label = keys_font.render('[down] or [s]', 1, (240, 0, 0))
        CANVAS.blit(down_key_label, (470, 420))

        up_label = control_font.render('Move Up', 1, (0, 225, 0))
        CANVAS.blit(up_label, (125, 475))
        up_key_label = keys_font.render('[up] or [w]', 1, (240, 0, 0))
        CANVAS.blit(up_key_label, (470, 475))

        escape_label = control_font.render('Return back to home', 1, (0, 225, 0))
        CANVAS.blit(escape_label, (125, 530))
        escape_key_label = keys_font.render('[backspace]', 1, (240, 0, 0))
        CANVAS.blit(escape_key_label, (470, 530))

        control_title_label = control_font.render('[Backspace]', 1, (255, 255, 255))
        CANVAS.blit(control_title_label, (30, 30))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_m:
                    audio_cfg.toggle_mute()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_BACKSPACE]:
            run = False
        if keys[pygame.K_PLUS]:
            audio_cfg.inc_volume(5)
        if keys[pygame.K_MINUS]:
            audio_cfg.dec_volume(5)
