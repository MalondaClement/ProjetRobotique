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
	def __init__(self,nb_ligne, nb_colonne): 
		self.nb_ligne=nb_ligne
		self.nb_colonne=nb_colonne
		self.matrice=np.zeros((nb_ligne,nb_colonne))
		self.list_rob=[]
		self.list_obj=[]
		#cree les mur
		
	def cree_mur(self):
		for i in range(0,self.nb_ligne):
			for j in range(0,self.nb_colonne):
				if (i == 0) or (j==0) or (i==self.nb_ligne-1) or (j==self.nb_colonne-1):
				    self.matrice[i,j] =1
	def est_dans_matrice(self,o):
		if o.x-o.largeur//2>0 and o.x+o.largeur//2<self.nb_colonne and o.y-o.longueur//2>0 and o.y+o.longueur//2<self.nb_ligne:
			return True
	def est_vide(self,o):
		for p in range(i.y - i.longueur//2,i.y + i.longueur//2):
			for q in range(i.x - i.largeur//2,i.x + i.largeur//2):
				if self.matrice[p,q]!=0:
					return False
		return True
				 
	def remplir_matrice(self,i,val):
		for p in range(i.y - i.longueur//2,i.y + i.longueur//2):
			for q in range(i.x - i.largeur//2,i.x + i.largeur//2):
					self.matrice[p,q]=val

	def inserer_robot(self,r):
			if self.est_dans_matrice(r) and self.est_vide:
				self.matrice[r.y,r.x]=2
				self.list_rob.append(r)
		#parcoure la liste des obstacles meme principe que pour le robot
	def inserer_obs(self,o):
		if self.est_dans_matrice(o) and self.est_vide:
			self.remplir_matrice(o,1)
			self.list_obj.append(o)
				
#on rentre des coordonnee ca nous renvoie le chiffre contenu dans la case de la matrice
	def get_object(self,x,y):
		return int(self.matrice[x,y])
		#0:vide, 1:obstacle, 2:robot


def calcul_angle(p):
	a=m.atan(p.largeur/p.longueur)
	return a

def calcul_hypo(p):
	a=m.pow(p.largeur/2,2)+m.pow(p.longueur/2,2)
	return m.sqrt(a)

	

			 
	
"""#jeu de test:
p=Obstacle(4,8,4,2,6)
#m=Obstacle(6,15,1)

b=Robot(5,15,m.pi/2)
a=Arene(20,10)
print (a.matrice)
a.cree_mur()
print (a.matrice)
a.inserer_robot(b)
a.inserer_obs(p)
print (a.matrice)"""

