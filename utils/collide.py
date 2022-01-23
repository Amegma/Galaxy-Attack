def collide(obj1, obj2):
    # obj1 and obj2 coordinates refer to the middle point of the mask, so we have to compute
    # the coordinates of the upper-left corner of the sprite
    x_offset = int((obj2.x - obj2.get_width()/2) -
                   (obj1.x - obj1.get_width()/2))
    y_offset = int((obj2.y - obj2.get_height()/2) -
                   (obj1.y - obj1.get_height()/2))
    return obj1.mask.overlap(obj2.mask, (x_offset, y_offset)) != None
