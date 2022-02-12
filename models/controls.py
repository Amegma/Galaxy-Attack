import pygame

from utils.assets import Assets
from config import config
from constants import Image, soundList, Font, Colors


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

    def display_volume(self):
        control_font = pygame.font.Font(Font.neue_font, 30)

        if self.muted:
            Assets.image.draw(
                Image.MUTE_ICON, (config.starting_x+20, config.ending_y-52))
            vol_lbl_text = " --"
        else:
            Assets.image.draw(
                Image.VOL_ICON, (config.starting_x + 20, config.ending_y - 52))
            vol_lbl_text = str(self.volume).rjust(3, " ")

        Assets.text.draw(vol_lbl_text, control_font, Colors.WHITE,
                         (config.starting_x + 70, config.ending_y - 57))

    def play_music(self, path):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1)


class DisplayControls:
    def __init__(self):
        self.fullscreen = False

    def toggle_full_screen(self):
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            config.CANVAS = pygame.display.set_mode(
                config.monitor_size, pygame.FULLSCREEN)
        else:
            config.CANVAS = pygame.display.set_mode(
                (config.WIDTH, config.HEIGHT), pygame.RESIZABLE)


audio_cfg = AudioControls(soundList)
display_cfg = DisplayControls()
