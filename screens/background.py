from config import config


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
        x = config.center_x - self.rectBGimg.width / 2
        config.CANVAS.blit(self.bgimage, (x, self.bgY1))
        config.CANVAS.blit(self.bgimage, (x, self.bgY2))


bg_obj = ScrollBackground(config.BG)
slow_bg_obj = ScrollBackground(config.BG, 1.5)
