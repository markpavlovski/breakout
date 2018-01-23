from GameConstants import *
from GameObject import *

class Pad(GameObject):
    def __init__(self,position,sprite):
        super(Pad,self).__init__(position,GameConstants.PAD_SIZE, sprite)

    def set_position(self,position):
        new_position = [position[0],position[1]]
        size = self.get_size()

        if new_position[0] + size[0] > GameConstants.SCREEN_SIZE[0]:
            new_position[0] = GameConstants.SCREEN_SIZE[0]-size[0]

        super(Pad,self).set_position(new_position)
