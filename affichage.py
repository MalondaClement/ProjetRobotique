from tkinter import * 
from arene import Arene
from robot import Robot
from Obstacle import Obstacle
import math as m

class Affichage(object):
	def __init__(self,arene):
		self.arene=arene	

	def afficher(self):
		#on parcoure tous les elements de la matrice et on les colorie selon leur valeur
		i=0
		j=0
		while j<self.arene.nb_colonne:
			i=0
			while i<self.arene.nb_ligne:
				if self.arene.matrice[i,j]==1:
					zone_dessin.create_rectangle(j,i,(j+1),(i+1 ),fill='black')
				
				i=i+1
			j=j+1
		
#petit main ou le robot effectue un parcour simple
def main():
	if p.x==900 and p.y==200:
		p.changer_angle(m.pi/2)
		#.after permet d'attendre un temps donne puis d'effectuer une fonction ensuite
		fenetre.after(50,main)
	if p.x==900 and p.y==100:
		p.changer_angle(m.pi/2)
		fenetre.after(50,main)
	p.avancer(10)
	#je dessine la fleche et le robot dans la fenetre .coords permet de donner de nouvelle coordonnée au objet de la fenetre
	#objet fenetre != objet affichage, l'objet de la fenetre est a déclaré avec la fenetre
	zone_dessin.coords(r,p.x-p.largeur/2,p.y-p.longueur/2,p.x+p.largeur/2,p.y+p.longueur/2)
	zone_dessin.coords(f,p.x,p.y,round(50*m.cos(p.angle),1)+p.x,p.y+round(50*m.sin(-p.angle),1))
	fenetre.after(50,main)

def Demarrer():
	main()

o=Obstacle(50,10,1)
p=Robot(50,200,0)
b=Arene(500,1000,[o],[p])
z=Affichage(b)
#declarer la fenetre en dernier
fenetre = Tk()#creer une fenetre
fenetre.title('Arene')#donner un nom  la fenetre
fenetre.geometry("1200x600")#donner la taille de la fenetre
		#on definit la zone ou on dessine(fenetre,y,x,couleur d'arrier plan)

#bouton demarer 
BoutonGo = Button(fenetre, text ='Démarrer', command = Demarrer)
BoutonGo.pack(side = LEFT, padx = 10, pady = 10)
#bouton quitter
BoutonQuitter = Button(fenetre, text ='Quitter', command = fenetre.destroy)
BoutonQuitter.pack(side = LEFT, padx = 5, pady = 5)
#crée la zone de dessin
zone_dessin =Canvas(fenetre, width=z.arene.nb_colonne,height=z.arene.nb_ligne,background='white')
#j'affiche l'arene de base avant de demarer la demo
z.afficher()
#le robot
r=zone_dessin.create_rectangle(p.x-p.largeur/2,p.y-p.longueur/2,p.x+p.largeur/2,p.y+p.longueur/2,fill='red')
#le fleche
f=zone_dessin.create_line(p.x,p.y,round(50*m.cos(p.angle),1)+p.x,p.y+round(50*m.sin(-p.angle),1),arrow='last',fill='yellow')

zone_dessin.pack()
fenetre.mainloop()


"""p.avancer(20)
b=Arene(200,110,[o],[p])
a=Affichage(b)
p.avancer(20)
b=Arene(200,110,[o],[p])
a=Affichage(b)
p.avancer(10)
b=Arene(200,110,[o],[p])
a=Affichage(b)
#a=Affichage(b)"""

