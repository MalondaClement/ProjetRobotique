import math as m
class Robot(object):
	def __init__(self,x,y,angle):
		self.x=x
		self.y=y
		self.angle=angle
		self.couleur=0 #noir en binaire
		self.largeur=20
		self.longueur=50

	def get_position(self):
		return self.x, self.y
	
	def obstacle (self, originex, originey, arene, pas):
	"""Cette fonction permet la détection des obstacles se trouvant sur une demi devant le robot
		:param originex: x de l'origine de la demi-droite
		:param origeney: y de l'origine de la demi-droite
		:param arene: arene (matrice) dans lequel se trouve le robot
		:param pas: pas entre chaque avancer sur la demi-droite de détection
		:returns : position x, y de l'obstacle qui permetra le calcul de la distance avec celui-ci
	"""
       		recherche_x= originex
        	recherche_y= originey
        	while True:
            		recherche_x+=m.cos(self.angle)*pas
            		recherche_y-=m.sin(self.angle)*pas
            		recherche_x=round(recherche_x,0)
            		recherche_y=round(recherche_y,0)
			if recherche_x<0 or recherche_y<0 or recherche_x>arene.nb_colonne or recherche_y>arene.nb_ligne:
                		return recherche_x, recherche_y
            		if arene.matrice[recherche_x, recherche_y]==1:
                		return recherche_x, recherche_y

	def changer_angle(self, delta):
	    self.angle+=delta
	    while self.angle>(m.pi)*2:
		self.angle-=(m.pi)*2
	    while self.angle<0 :
		self.angle+=(m.pi)*2

	def avancer (self, distance):
	    self.x+=m.cos(self.angle)*distance
	    self.x=int(round(self.x,1))
	    self.y-=m.sin(self.angle)*distance
	    self.y=int(round(self.y,1))

'''#jeu de test:
a=Robot(0,0, m.pi/2)
print (a.get_position()==(0,0))
a.x,a.y=a.x+1,a.y+1
print (a.get_position()==(1,1))
print (a.angle==m.pi/2)

#--------------------------------------------------
#jeu de test (fct changement angle):
changer_angle(a, m.pi/6)#ajout de (m.pi/6)
print(a.angle==(m.pi/2))#False verifie si modification resultat correct
print(a.angle==(2*m.pi)/3)#True verifie si resultat correct

changer_angle(a, -(m.pi/6))#-(m.pi/6)
print(a.angle==(m.pi/2))#True resultat correct
changer_angle(a,(13*(m.pi))/6)#+13(m.pi)/6 => +(m.pi/6)
print(a.angle==(2*m.pi)/3)#True resultat correct
changer_angle(a, -13*(m.pi)/6)#-13(m.pi)/6=> -(m.pi/6)
print(a.angle==(m.pi/2))#True resultat correct
changer_angle(a, 0)#angle nul
print(a.angle==(m.pi/2))#True resultat correct


#jeu de test avancer
b=Robot(0,0,0)
avancer(b,5)
print ((b.x)==5)
changer_angle(b,-m.pi/2)
avancer (b,5)
print ((b.x==5) and (b.y==5))'''
