import numpy as np
from robot import Robot
from Obstacle import Obstacle
import math as m

#j'ai juste fait le cas ou la forme est un caree
class Arene(object):
#initialise la matrice avec des zero partout
    def __init__(self,nb_ligne, nb_colonne,list_obj,list_rob):
        self.nb_ligne=nb_ligne
        self.nb_colonne=nb_colonne
        self.matrice=np.zeros((nb_ligne,nb_colonne))
        self.list_rob=list_rob
        self.list_obj=list_obj
		#cree les mur
        j=0
        while j<nb_colonne:
                self.matrice[0,j]=1
                j=j+1
        j=0
        while j<nb_colonne:
                self.matrice[nb_ligne-1,j]=1
                j=j+1
        i=0
        while i<nb_ligne:
                self.matrice[i,0]=1
                i=i+1
        i=0
        while i<nb_ligne:
                self.matrice[i,nb_colonne-1]=1
                i=i+1
		
		#mettre un robot dans la matrice
        for i in list_rob:
                if self.matrice[i.x - i.longueur,i.y - i.largeur]==0 and self.matrice[i.x + i.longueur,i.y + i.largeur]==0 and self.matrice[i.x + i.longueur,i.y - i.largeur]==0 and self.matrice[i.x - i.longueur,i.y + i.largeur]==0 :
                        self.matrice[i.x,i.y]=2

		#parcoure la liste des obstacles meme principe que pour le robot
        for i in list_obj:
                if self.matrice[i.x - i.longueur,i.y - i.largeur]==0 and self.matrice[i.x + i.longueur,i.y + i.largeur]==0 and self.matrice[i.x + i.longueur,i.y - i.largeur]==0 and self.matrice[i.x - i.longueur,i.y + i.largeur]==0 :
                        self.matrice[i.x,i.y]=1
				
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

