import numpy as np

class Obstacle(object):
    def __init__(self, x, y, forme):
        self.x = x
        self.y = y
        self.forme = forme
        if self.forme == 1 : #carre
            self.largeur = self. longueur = 10
        elif self.forme == 2 : #rond
            self.rayon = 10
        elif self.forme == 3 : #triangle
            self.base = self.hauteur = 10
        else :
            self.forme = 1
            self.largeur = self. longueur = 10

    def get_position(self):
        return self.x, self.y

    def get_forme(self):
        return self.forme

#j'ai juste fait le cas ou la forme est un carée
class Arene(object):
#initialise la matrice avec des zero partout
	def __init__(self,nb_ligne, nb_collone,obstacle): 
		self.matrice=np.zeros((nb_ligne,nb_collone))
		#parcoure la liste des obstacles
		for i in obstacle:
			#verifie si les coordonnees du centre du caree rentre dans la matrice
			if i.x<=nb_collone and i.x>=0 or i.y<=nb_ligne  and i.y>=0:
				#verifie si le caree rentre dans la matrice
				if i.y-(i.largeur/2)>=0 and i.x-(i.largeur/2)>=0 and i.y+(i.largeur/2)<=nb_ligne and i.x+(i.largeur/2)<=nb_collone:
					a=i.x-(i.largeur/2)
					b=i.y-(i.largeur/2)
					#on rempli la matrice
					while a<i.x+(i.largeur/2):
						while b<i.y+(i.largeur/2):
							self.matrice[b,a]=1
							b=b+1
						a=a+1
						b=i.y-(i.largeur/2)
						
				
#on rentre des coordonnee ca nous renvoie le chiffre contenu dans la case de la matrice
	def get_object(self,x,y):
		return int(self.matrice[x,y])
		#0:vide, 1:obstacle, 2:robot

			 
	
#jeu de test:
p=Obstacle(5,5,1)
m=Obstacle(5,15,1)
a=Arene(20,12,[p,m])
print a.matrice
#print a.matrice[-1,-1]
#a.matrice[0,0]=1
#print a.matrice
#print a.get_object(0,0)
