from config import config
from utils.assets import Assets


class ScrollBackground():
    def __init__(self, bg_img, moving_speed=3):
        self.bgimage = bg_img
        self.rectBGimg = self.bgimage.get_rect()

        self.bgY1 = 0

        self.bgY2 = - self.rectBGimg.height

        self.moving_speed = moving_speed

    def update(self):
        self.bgY1 += self.moving_speed
        self.bgY2 += self.moving_speed
        if self.bgY1 >= self.rectBGimg.height:
            self.bgY1 = - self.rectBGimg.height
        if self.bgY2 >= self.rectBGimg.height:
            self.bgY2 = - self.rectBGimg.height

    def render(self):
        Assets.image.draw(self.bgimage, (config.center_x, self.bgY1), True)
        Assets.image.draw(self.bgimage, (config.center_x, self.bgY2), True)


bg_obj = ScrollBackground(config.BG)
slow_bg_obj = ScrollBackground(config.BG, 1.5)
