import os
import pygame

from screens.background import slow_bg_obj
from constants import soundList, neue_font, VOL_ICON, MUTE_ICON


class AudioControls:
    def __init__(self, soundList):
        self.soundList = soundList
        self.volume = 100
        self.muted = True if self.volume == 0 else False
        self.prev_volume = -1

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
        else:
            self.prev_volume = self.volume
            self.set_volume(0)

    def display_volume(self, CANVAS):
        background_width = slow_bg_obj.rectBGimg.width
        screen_rect = CANVAS.get_rect()
        center_x = screen_rect.centerx
        starting_x = center_x - background_width//2

        control_font = pygame.font.Font(neue_font, 30)

        if self.muted:
            CANVAS.blit(MUTE_ICON, (starting_x + 20, 695))
            vol_lbl_text = " --"
        else:
            CANVAS.blit(VOL_ICON, (starting_x + 20, 695))
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
