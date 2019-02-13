import math as m
class Robot(object):
"""La classe robot permet de créer les robots mais également de gérer ses déplacement (avancer, reculer et rotation).
La gestion de la détection d'obstacle se fait également dans cette classe.
	:param x: position en x du centre du robot
	:param y: position en y du centre du robot
	:param angle: angle de départ du robot en radian
"""
	def __init__(self,x,y,angle):
		self.x=x
		self.y=y
		self.angle=angle
		self.couleur=0 #noir en binaire
		self.largeur=20
		self.longueur=50

	def get_position(self):
		return self.x, self.y


	def changer_angle(self, delta):
	""" On peut changer l'angle du robot a chaque instant
		:param delta: correction d'angle en radian à ajouter à l'angle du robot
		:returns : rien, changement inplace
	"""
	    self.angle+=delta
	    while self.angle>(m.pi)*2:
			self.angle-=(m.pi)*2 #ici y a pas un problème d'indentation ? 
	    while self.angle<0 :
			self.angle+=(m.pi)*2 #ici y a pas un problème d'indentation ? 

	def avancer (self, distance):
	""" On peut faire avancer (et reculer) le robot dans l'arène
		:param distance: distance que doit parcourir le robot dans la modélisation de l'arène
			si distance est négatif on avance, sinon on recule
		:returns : rien, changement inplace
	"""
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
