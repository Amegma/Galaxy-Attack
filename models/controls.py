import os
import pygame

from screens.background import slow_bg_obj
from constants import soundList, FONT_PATH
from utils.resource_path import resource_path


class AudioControls:
    def __init__(self, soundList):
        self.soundList = soundList
        self.volume = 100
        self.muted = False
        self.prev_volume = -1

        # volume icons
        self.VOL_ICON = pygame.image.load(resource_path(
            os.path.join('assets', 'graphics', 'audio.png')))
        self.MUTE_ICON = pygame.image.load(resource_path(
            os.path.join('assets', 'graphics', 'mute.png')))

        pygame.mixer.music.set_volume(self.volume / 100)
        for soundItem in self.soundList:
            soundItem.set_volume(self.volume / 100)

    def set_volume(self, level):
        if level == 0:
            self.muted = True
        if self.muted and level > 0:
            self.muted = False
            self.prev_volume = 50  # if you unmute at zero vol, defaults to 50
        self.volume = level
        pygame.mixer.music.set_volume(level / 100)
        for soundItem in soundList:
            soundItem.set_volume(level / 100)

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

    def display_volume(self, CANVAS):
        background_width = slow_bg_obj.rectBGimg.width
        screen_rect = CANVAS.get_rect()
        center_x = screen_rect.centerx
        starting_x = center_x - background_width//2

        control_font = pygame.font.Font(resource_path(
            os.path.join(FONT_PATH, "neue.ttf")), 30)

        if self.muted:
            CANVAS.blit(self.MUTE_ICON, (starting_x + 20, 695))
            vol_lbl_text = " --"
        else:
            CANVAS.blit(self.VOL_ICON, (starting_x + 20, 695))
            vol_lbl_text = str(self.volume).rjust(3, " ")

        vol_label = control_font.render(vol_lbl_text, 1, (255, 255, 255))
        CANVAS.blit(vol_label, (starting_x + 70, 695))

    def play_music(self, path):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1)


class DisplayControls:
    def toggle_full_screen():
        screen = pygame.display.get_surface()
        if (screen.get_flags() & pygame.FULLSCREEN):
            pygame.display.set_mode((750, 750))
        else:
            info = pygame.display.Info()
            pygame.display.set_mode(
                (info.current_w, info.current_h), pygame.FULLSCREEN)


audio_cfg = AudioControls(soundList)
display_cfg = DisplayControls
