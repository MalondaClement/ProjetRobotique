import numpy as np
import math as m
import random
from tkinter import *
import tkinter
nb_ligne = 500
nb_collone = 500



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


	def changer_angle(self, delta):
	    self.angle+=delta
	    while self.angle> (m.pi)*2:
		    self.angle-= (m.pi)*2
	    while self.angle<0:
		    self.angle+=(m.pi)*2

	def avancer (self, distance):
	    self.x+=m.cos(self.angle)*distance
	    self.x=int(round(self.x,1))
	    self.y-=m.sin(self.angle)*distance
	    self.y=int(round(self.y,1))
#-------------------------------------------------------------------------------------------------------------
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
#-------------------------------------------------------------------------------------------------------------------
class Arene(object):
#initialise la matrice avec des zero partout
    def __init__(self,nb_ligne, nb_colonne,list_obs,list_rob): 
        self.nb_ligne=nb_ligne
        self.nb_colonne=nb_colonne
        self.matrice=np.zeros((nb_ligne,nb_colonne))
        self.list_rob=list_rob
        self.list_obs=list_obs
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
                    if (i.angle<=m.pi/4 or i.angle>=(7*m.pi)/4):
                        tmp=i.largeur
                        i.largeur=i.longueur
                        i.longueur=tmp
                    elif (i.angle>=(3*m.pi)/4 and i.angle<=(5*m.pi)/4):
                        tmp=i.largeur
                        i.largeur=i.longueur
                        i.longueur=tmp
                    a=i.x-(i.largeur/2)
                    b=i.y-(i.longueur/2)
                    while a<i.x+(i.largeur/2) and not trouv:
                        while b<i.y+(i.longueur/2)and not trouv:
                            if self.matrice[int(b),int(a)]!=0: 
                                trouv=True
                            b=b+1
                        a=a+1
                        b=i.y-(i.longueur/2)
					#on rempli la matrice
                    a=i.x-(i.largeur/2)
                    b=i.y-(i.longueur/2)
                    while a<i.x+(i.largeur/2)and not trouv:
                        while b<i.y+(i.longueur/2)and not trouv:
                            self.matrice[int(b),int(a)]=2
                            b=b+1
                        a=a+1
                        b=i.y-(i.longueur/2)

		#parcoure la liste des obstacles meme principe que pour le robot
        for i in list_obs:
            trouv=False
			#verifie si les coordonnees du centre du caree rentre dans la matrice
            if i.x<nb_colonne and i.x>0 and i.y<nb_ligne  and i.y>0:
				#verifie si le caree rentre dans la matrice
                if i.y-(i.longueur/2)>0 and i.x-(i.largeur/2)>0 and i.y+(i.longueur/2)<nb_ligne and i.x+(i.largeur/2)<nb_colonne:
                    a=i.x-(i.largeur/2)
                    b=i.y-(i.longueur/2)
                    while a<i.x+(i.largeur/2) and not trouv:
                        while b<i.y+(i.longueur/2)and not trouv:
                            if self.matrice[int(b),int(a)]!=0:
                                trouv=True
                            b=b+1
                        a=a+1
                        b=i.y-(i.longueur/2)
					#on rempli la matrice
                    a=i.x-(i.largeur/2)
                    b=i.y-(i.longueur/2)
                    while a<i.x+(i.largeur/2)and not trouv:
                        while b<i.y+(i.longueur/2)and not trouv:
                            self.matrice[int(b),int(a)]=1
                            b=b+1
                        a=a+1
                        b=i.y-(i.longueur/2)
                        
    def placer_robot(self,x,y):
        largeur = 20
        longueur = 50
        presence_obstacle = False
        robot = Robot(x,y,m.pi/2)
        if x > (largeur/2) + m.sqrt(((largeur/2)**2)+((longueur/2)**2)) and x < nb_collone - ((largeur/2) + m.sqrt(((largeur/2)**2)+((longueur/2)**2))) and y > (longueur/2) + m.sqrt(((largeur/2)**2)+((longueur/2)**2)) and y < nb_ligne - ((longueur/2) + m.sqrt(((largeur/2)**2)+((longueur/2)**2))):
            for e in range(int(x - m.sqrt(((20/2)**2)+((50/2)**2))) , int(x + m.sqrt(((20/2)**2)+((50/2)**2)))):
                for f in range(int(y - m.sqrt(((20/2)**2)+((50/2)**2))) , int(y + m.sqrt(((20/2)**2)+((50/2)**2)))):
                    if self.matrice[int(e),int(f)] == 1:
                        presence_obstacle = True
                
                        
            if presence_obstacle == False:
                for g in range(int(x - m.sqrt((((20/2)**2)+((50/2)**2)))) , int(x - m.sqrt((((20/2)**2)+((50/2)**2))))):
                    for h in range(int(y - m.sqrt((((20/2)**2)+((50/2)**2)))) , int(y - m.sqrt((((20/2)**2)+((50/2)**2))))):
                        self.matrice[int(g),int(h)] = 2
                
                            
        else :
            self.placer_robot(random.randint(int((20/2)+(((20/2)**2)+((50/2)**2))),int(nb_collone - (20/2)-(((20/2)**2)+((50/2)**2)))),random.randint((50/2)+(((20/2)**2)+((50/2)**2)),nb_ligne - (50/2)-(((20/2)**2)+((50/2)**2))))
        
    def placer_obstacle(self,x,y,forme):
        largeur = 10
        longueur = 10
        obs = Obstacle(x,y,1)
        if x > largeur/2 and x < nb_collone - largeur/2 and y > longueur/2 and y < nb_ligne - longueur/2:
            for i in range (int(x - largeur/2), int(x + largeur/2)):
                for j in range(int(y-longueur/2), int(y+longueur/2)):
                    self.matrice[i,j] = 1
            self.list_obs.append(obs)
        else:
            print(" Erreur insertion obstacle")
        

        
#------------------------------------------------------------------------------------------------------------------
class Affichage(object):
	def __init__(self,arene):	
		fenetre =Tk()#creer une fenetre
		fenetre.title('Arene')#donner un nom  la fenetre
		fenetre.geometry("500x500")#donner la taille de la fenetre
		#on definit la zone ou on dessine(fenetre,y,x,couleur d'arrier plan)
		#les *5 sont la car la matrice est trop petite sur l'affichage donc chaque case de la matrice correspond a un carree de cote 5 sur l'affichage
		zone_dessin =Canvas(fenetre, width=5*arene.nb_ligne, height=5*arene.nb_colonne,background='white')
		zone_dessin.pack()
		#on parcoure tous les elements de la matrice et on les colorie selon leur valeur
		i=0
		j=0
		while j<arene.nb_colonne:
			i=0
			while i<arene.nb_ligne:
				if arene.matrice[i,j]==1:
					zone_dessin.create_rectangle(i*5,j*5,(i+1)*5,(j+1)*5,fill='black')
                
				if arene.matrice[i,j]==2:
					zone_dessin.create_rectangle(j*5,i*5,(j+1)*5,(i+1 )*5,fill='red')
				i=i+1
			j=j+1
		#for a in arene.list_rob:
			#zone_dessin.create_line(a.x*5,a.y*5,round(100*m.cos(a.angle),1)+a.x*5,a.y*5+round(100*m.sin(-a.angle),1),arrow='last',fill='yellow')
		fenetre.mainloop()
#-----------------------------------------------------------------------------------------------------------------	
liste_obstacle = []
liste_robot = []


robot = Robot(250,250,m.pi/2)
liste_robot.append(robot)


Arene = Arene(500,500,liste_obstacle,liste_robot)
cpt = 0
cpt2 = 0
for i in range(0, nb_ligne):
    for j in range(0,nb_collone):
        if Arene.matrice[i,j] == 2:
            cpt = cpt + 1
        if Arene.matrice[i,j] == 1:
            cpt2 = cpt2 + 1
print(cpt)
print(cpt2)
cpt2=0

Arene.placer_obstacle(10,10,1)
for i in range(0, nb_ligne):
    for j in range(0,nb_collone):
        if Arene.matrice[i,j] == 1:
            cpt2 = cpt2 + 1
Arene.placer_robot(250,250)
print(cpt2)
print(Arene.list_obs)
print(Arene.list_rob)

Affichage(Arene)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    