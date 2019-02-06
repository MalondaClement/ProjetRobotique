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

#j'ai juste fait le cas ou la forme est un caree
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
	
	def placer_obstacle(self,x,y,forme):
		trouv=False
		#on verifie si x et y sont dans la matrice et si ils sont supérieurs à 0
		if x<=nb_collone and x>=0 and y<=nb_ligne  and i.y>=0: 
			if forme==1:
				#création de l'obstacle i (ici un carré)
				i=Obstacle(x,y,1)
				#on verifie que l'obstacle puisse entrer dans la matrice
				if i.y-(i.largeur/2)>0 and i.x-(i.largeur/2)>0 and i.y+(i.largeur/2)<nb_ligne and i.x+(i.largeur/2)<nb_collone:
					a=i.x-(i.largeur/2)
					b=i.y-(i.largeur/2)
					#on remplie la matrice
					while a<i.x+(i.largeur/2) and not trouv:
						while b<i.y+(i.largeur/2) and not trouv:
							if self.matrice[b,a]==1:
								trouv=True
							b=b+1
						a=a+1
						b=i.y-(i.largeur/2)
					if not trouv:
						obstacle.append(i)	
						
	



#test placer obstacle
#placer_obstacle(6,6,1);
#placer_obstacle(499,450,1);
#placer_obstacle(45,45,2);
#placer_obstacle(89,89,3);
#placer_obstacle(46,46,1);

			 
	
#jeu de test:
#p=Obstacle(4,6,1)
#m=Obstacle(5,15,1)
a=Arene(20,12,[])
a.placer_obstacle(6,6,1)
B=Arene(20,12,obstacle)
print B.matrice
#print a.matrice[-1,-1]
#a.matrice[0,0]=1
#print a.matrice
#print a.get_object(0,0)

