import numpy as np
from robot import Robot
from Obstacle import Obstacle
import math as m

#j'ai juste fait le cas ou la forme est un caree
class Arene(object):
#initialise la matrice avec des zero partout
	def __init__(self,nb_ligne, nb_colonne,list_obs,list_rob): 
		self.nb_ligne=nb_ligne
		self.nb_colonne=nb_colonne
		self.matrice=np.zeros((nb_ligne,nb_colonne))
		self.list_rob=list_rob
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
			tmp=0
			trouv=False
			#verifie si les coordonnees du centre du caree rentre dans la matrice
			if i.x<nb_colonne and i.x>0 and i.y<nb_ligne  and i.y>0:
				#verifie si le caree rentre dans la matrice
				if i.y-(i.longueur/2)>0 and i.x-(i.largeur/2)>0 and i.y+(i.longueur/2)<nb_ligne and i.x+(i.largeur/2)<nb_colonne:
					#verifie qu'il n'y a pas autre chose que du vide a l'emplacement du robot
					a=i.x-(i.largeur//2)
					b=i.y-(i.longueur//2)
					while a<=i.x+(i.largeur//2) and not trouv:
						while b<=i.y+(i.longueur//2)and not trouv:
							if self.matrice[b,a]!=0: 
								trouv=True
							b=b+1
						a=a+1
						b=i.y-(i.longueur//2)
					#on rempli la matrice
					a=i.x-(i.largeur//2)
					b=i.y-(i.longueur//2)
					while a<=i.x+(i.largeur//2)and not trouv:
						while b<=i.y+(i.longueur//2)and not trouv:
							self.matrice[b,a]=3
							b=b+1
						a=a+1
						b=i.y-(i.longueur//2)
					if not trouv:
						self.matrice[i.y,i.x]=2

		#parcoure la liste des obstacles meme principe que pour le robot
		for i in list_obs:
			trouv=False
			#verifie si les coordonnees du centre du caree rentre dans la matrice
			if i.x<nb_colonne and i.x>0 and i.y<nb_ligne  and i.y>0:
				#verifie si le caree rentre dans la matrice
				if i.y-(i.longueur/2)>0 and i.x-(i.largeur/2)>0 and i.y+(i.longueur/2)<nb_ligne and i.x+(i.largeur/2)<nb_colonne:
					a=i.x-(i.largeur//2)
					b=i.y-(i.longueur//2)
					while a<i.x+(i.largeur//2) and not trouv:
						while b<i.y+(i.longueur//2)and not trouv:
							if self.matrice[b,a]!=0:
								trouv=True
							b=b+1
						a=a+1
						b=i.y-(i.longueur//2)
					#on rempli la matrice
					a=i.x-(i.largeur//2)
					b=i.y-(i.longueur//2)
					while a<i.x+(i.largeur//2)and not trouv:
						while b<i.y+(i.longueur//2)and not trouv:
							self.matrice[b,a]=1
							b=b+1
						a=a+1
						b=i.y-(i.longueur//2)
						
				
#on rentre des coordonnee ca nous renvoie le chiffre contenu dans la case de la matrice
	def get_object(self,x,y):
		return int(self.matrice[x,y])
		#0:vide, 1:obstacle, 2:robot

			 
	
"""#jeu de test:
p=Obstacle(6,6,1)
#m=Obstacle(6,15,1)

b=Robot(14,17,m.pi/4)
b.largeur=5
b.longueur=5
a=Arene(22,18,[p],[b])
print (a.matrice)
#print a.matrice[-1,-1]
#a.matrice[0,0]=1
#print a.matrice
#print a.get_object(0,0)"""

