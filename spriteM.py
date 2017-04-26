import pygame
from pygame.locals import *
from PIL import Image

class spriteM:

    
    counter = 0 #nombre d'image dans le sprite manager
    fenetre = pygame.display.set_mode((854, 480)) #l'on défini la fenetre de pygame dans le l'objet spriteM

    def __init__(self, path, x=0, y=0):
        
        spriteM.counter += 1
        self.name = "SpriteM_n." + str(spriteM.counter)
        self.x = x
        self.y = y
        self.img = {(self.name + "_0"):pygame.image.load(path).convert_alpha()}
        self.path = path
        

    def load(self, path, x="none", y="none", debug=0):    # met l'image en base de donnee à la place de celle d'origine

        if x == "none":
            x = self.x
        if y == "none":
            y = self.y

        self.path = path
        self.img = {(self.name + "_ 0"):pygame.image.load(path).convert_alpha()}
        if debug == 1:
            print(path, " à été mis en stock avec comme placement lors du rendu x:",x," y:",y)

    def frames(self, tx, ty, path="none"):
        if path != "none":
            load(path)
            
        nbrFramesX = int((self.img[(self.name +"_0")].get_size()[0] // tx)-1)
        nbrFramesY = int((self.img[(self.name +"_0")].get_size()[1] // ty)-1)
        
        imgC = {}
        for ii in range(nbrFramesY+1):
            for i in range(nbrFramesX+1):
                cropped = pygame.Surface((tx, ty))
                cropped.blit(self.img[(self.name +"_0")], ((tx*i), (ty*ii)))
                imgC[(self.name + "_" + str(i+(nbrFramesX*ii)))] = cropped
            
        self.img = imgC
            
    def render(self, x="none", y="none", frame=0, debug=0):
        if x == "none":
            x = self.x
        if y == "none":
            y = self.y
            
        spriteM.fenetre.blit(self.img[(self.name + "_" + str(frame))], (x,y))
        if debug == 1:
            print("img rendu en x:",self.x," y:",self.y)

    def render_rot(self, angle=0, x="none", y="none", frame=0, debug=0):

        if x == "none":
            x = self.x
        if y == "none":
            y = self.y

        image = self.img[(self.name + "_" + str(frame))]

        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        
        spriteM.fenetre.blit(rot_image, (x,y))
        
        if debug == 1:
            print("img rendu en x:",x," y:",y, ". Avec un angle de ",angle," dg.")

    
