from config import config


def draw_text(text, font, color, pos, isCenterX=False, isCenterY=False):
    text_label = font.render(text, 1, color)

    if isCenterX:
        pos = (pos[0] - text_label.get_width()//2, pos[1])
    if isCenterY:
        pos = (pos[0], pos[1] - text_label.get_height()//2)

    config.CANVAS.blit(text_label, pos)
