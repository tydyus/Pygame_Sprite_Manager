import pygame
from pygame.locals import *
from PIL import Image

from spriteM import *

class anime:

    def __init__(self, imgObj_spriteM, tick, frameListe, x, y):
        self.time = 0
        self.tick = tick
        self.img = imgObj_spriteM
        self.frame = frameListe
        self.etat = 0
        self.x = x
        self.y = y

    def render(self, x="none", y="none"):
        if x == "none":
            x = self.x
        if y == "none":
            y = self.y

        self.time += 1
        self.img.render(self.x, self.y, (self.etat))
        if self.time >= self.tick:
            self.time = 0
            if self.etat == (len(self.frame)-1):
                self.etat = 0
            self.etat += 1
            
        
            


