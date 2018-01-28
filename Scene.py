import pygame
from GameConstants import *
class Scene:

    def __init__(self,game):
        self.__game = game
        self.__texts = []

    def render(self):
        for text in self.__texts:
            self.__game.screen.blit(text[0],text[1])


    def get_game(self):
        return self.__game

    def handle_events(self, events):
        pressed_keys = pygame.key.get_pressed()

        for event in events:
            if event.type == pygame.QUIT:
                exit()

    def clear_text(self):
        self.__texts = []

    def add_text(self, string, x=0, y=0, color = (255,255,255), background = (0,0,0), size = 17):
        font = pygame.font.Font(GameConstants.FONT_PATH,size)
        self.__texts.append([font.render(string,True,color,background), (x,y)])
