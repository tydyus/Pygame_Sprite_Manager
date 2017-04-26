import pygame
from pygame.locals import *

class spriteM:

    #nombre d'image dans le sprite manager
    counter = 0
    #l'on défini la fenetre de pygame dans le l'objet spriteM
    fenetre = pygame.display.set_mode((854, 480))

    def __init__(self, path, x=0, y=0):
        
        spriteM.counter += 1

        self.x = x
        self.y = y
        self.img = pygame.image.load(path).convert_alpha()
        
        # met l'image en base de donnee à la place de celle d'origine
    def load(self, path, x="none", y="none", debug=0):

        if x == "none":
            x = self.x
        if y == "none":
            y = self.y
        
        self.img = pygame.image.load(path).convert_alpha()
        if debug == 1:
            print(path, " à été mis en stock avec comme placement lors du rendu x:",x," y:",y)

        # rend l'image dans la fenetre
    def render(self, x="none", y="none", debug=0):

        if x == "none":
            x = self.x
        if y == "none":
            y = self.y
            
        spriteM.fenetre.blit(self.img, (x,y))
        if debug == 1:
            print("img rendu en x:",self.x," y:",self.y)

    def render_rot(self, angle=0, x="none", y="none", debug=0):

        if x == "none":
            x = self.x
        if y == "none":
            y = self.y

        image = self.img

        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        
        spriteM.fenetre.blit(rot_image, (x,y))
        
        if debug == 1:
            print("img rendu en x:",x," y:",y, ". Avec un angle de ",angle," dg.")

    
