from GameConstants import *
from GameObject import *

class Pad(GameObject):
    def __init__(self,position,sprite):
        self.__game = game
        super(Pad,self).__init__(position,GameConstants.PAD_SIZE, sprite)
