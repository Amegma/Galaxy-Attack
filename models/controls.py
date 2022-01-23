import pygame

from config import Config
from constants import Image, soundList, Font


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
            Config.CANVAS.blit(Image.MUTE_ICON,
                        (Config.starting_x + 20, Config.ending_y - 52))
            vol_lbl_text = " --"
        else:
            Config.CANVAS.blit(Image.VOL_ICON,
                        (Config.starting_x + 20, Config.ending_y - 52))
            vol_lbl_text = str(self.volume).rjust(3, " ")

        vol_label = control_font.render(vol_lbl_text, 1, (255, 255, 255))
        Config.CANVAS.blit(vol_label, (Config.starting_x + 70, Config.ending_y - 57))

    def play_music(self, path):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1)


class DisplayControls:
    def toggle_full_screen():
        screen = pygame.display.get_surface()
        if (screen.get_flags() & pygame.FULLSCREEN):
            pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        else:
            info = pygame.display.Info()
            pygame.display.set_mode(
                (info.current_w, info.current_h), pygame.FULLSCREEN)


audio_cfg = AudioControls(soundList)
display_cfg = DisplayControls
