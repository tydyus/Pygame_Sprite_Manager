import pygame
from pygame.locals import *


from spriteM import *
from sprite_anime import *
from font import *

class img: # initialisation images et textes, et resize

		#resize
	facteur = 1
		#couleur
	# ex: color_font = (0,0,0)
		#font
	# ex: font_texte = "font/larabiefont_rg.ttf"


		#ex
	#monImage = spriteM("img/fondE.png",0,0)
	#font_monTexte = font("montexte", color_font,(0,0,"bas-droit"),15,font_texte)

	def resize(newsize): #newsize-> (x,y), valeur lors d'un screenResize
		#img.facteur = newsize[0]/854
		#spriteM.facteur = img.facteur

		return 1 #return 1 pour activer un refresh
