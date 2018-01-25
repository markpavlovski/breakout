import pygame
from GameConstants import *
from GameObject import *

class Pad(GameObject):
    def __init__(self,position,sprite):
        self.__increment = GameConstants.MOVEMENT_INCREMENT
        self.__speed = GameConstants.PAD_SPEED
        super(Pad,self).__init__(position,GameConstants.PAD_SIZE, sprite)

    def set_position(self,position):
        new_position = [position[0],position[1]]
        size = self.get_size()

        if new_position[0] + size[0] > GameConstants.SCREEN_SIZE[0]:
            new_position[0] = GameConstants.SCREEN_SIZE[0]-size[0]

        if new_position[0] <= 0:
            new_position[0] = 0

        super(Pad,self).set_position(new_position)

    def move_right(self):
        self.set_position((self.get_position()[0] + self.__increment * self.__speed, self.get_position()[1]))

    def move_left(self):
        self.set_position((self.get_position()[0] - self.__increment * self.__speed, self.get_position()[1]))
