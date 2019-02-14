import numpy as np
from robot import Robot

from obstacle import Obstacle
import math as m

#j'ai juste fait le cas ou la forme est un caree
class Arene(object):

#"""La classe arene permet la représentation des éléments dans l'arène pour faire nos calculs comme la détection d'obtacle.
#Elle gère une matrice dans laquelle chaque élément correpond à un "object" à cette position dans l'arene.
#Si 0 il n'y a rien, si 1 on a un obstacle, si 2 on a le robot.
#	:param nb_ligne: nb de lignes de la matrice correpond au pixels
#	:param nb_colonne: nb de colonnes de la matrice correpond au pixels
#	:param list_obj: liste d'élément de type obstacle à placer dans la matrice
#	:param list_rob: liste d'élément de type robotà mettre dans la matrice, dans un premier temps 1 seul
#"""
#initialise la matrice avec des zero partout
	def __init__(self,nb_ligne, nb_colonne,list_obj,list_rob): 
		self.nb_ligne=nb_ligne
		self.nb_colonne=nb_colonne
		self.matrice=np.zeros((nb_ligne,nb_colonne))
		self.list_rob=list_rob
		self.list_obj=list_obj
		#cree les mur
        for i in range(0,nb_ligne):
            for j in range(0,nb_colonne):
                if (i == 0) or (j==0) or (i==nb_ligne-1) or (j==nb_colonne-1):
                    self.matrice[j,i] =1
                        
        
        #mettre un robot dans la matrice
        for i in list_rob:
            if self.matrice[i.x - i.longueur//2,i.y - i.largeur//2]==0 and self.matrice[i.x + i.longueur//2,i.y + i.largeur//2]==0 and self.matrice[i.x + i.longueur//2,i.y - i.largeur//2]==0 and self.matrice[i.x - i.longueur//2,i.y + i.largeur//2]==0 :
                self.matrice[i.x,i.y]=2

        #parcoure la liste des obstacles meme principe que pour le robot
        for i in list_obj:
            if self.matrice[i.x - i.longueur//2,i.y - i.largeur//2]==0 and self.matrice[i.x + i.longueur//2,i.y + i.largeur//2]==0 and self.matrice[i.x + i.longueur//2,i.y - i.largeur//2]==0 and self.matrice[i.x - i.longueur//2,i.y + i.largeur//2]==0 :
                for p in range(i.y - i.largeur//2,i.y + i.largeur//2):
                    for q in range(i.x - i.longueur//2,i.x + i.longueur//2):

                        self.matrice[q,p]=1
				
#on rentre des coordonnee ca nous renvoie le chiffre contenu dans la case de la matrice
	def get_object(self,x,y):
		return int(self.matrice[x,y])
		#0:vide, 1:obstacle, 2:robot


def calcul_angle(L,l):
	a=m.atan(L/l)
	return a

def calcul_hypo(L,l):
	a=m.pow(L,2)+m.pow(l,2)
	return m.sqrt(a)

	

			 
	
"""#jeu de test:
#p=Obstacle(6,6,1)
#m=Obstacle(6,15,1)

b=Robot(10,10,m.pi/2)
b.largeur=3
b.longueur=5
a=Arene(22,18,[],[b])
print (a.matrice)
#print a.matrice[-1,-1]
#a.matrice[0,0]=1
#print a.matrice
#print a.get_object(0,0)"""

