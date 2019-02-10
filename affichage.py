from tkinter import * 
from arene import Arene
from arene import calcul_hypo
from arene import calcul_angle
from robot import Robot
from Obstacle import Obstacle
import math as m
from tkinter.filedialog import *

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

arret=False	
#petit main ou le robot effectue un parcour simple
def main():
	global arret
	if arret==False:
		"""if p.x==900 and p.y==200:
			p.changer_angle(m.pi/2)
				#.after permet d'attendre un temps donne puis d'effectuer une fonction ensuite
			fenetre.after(50,main)
		if p.x==900 and p.y==100:
			p.changer_angle(m.pi/2)
			fenetre.after(50,main)
		p.avancer(10)
			#je dessine la fleche et le robot dans la fenetre .coords permet de donner de nouvelle coordonnée au objet de la fenetre
			#objet fenetre != objet affichage, l'objet de la fenetre est a déclaré avec la fenetre"""
		#tester le changement d'angle
		p.changer_angle(m.pi/10)
		zone_dessin.coords(r,p.x+t*m.cos(p.angle+angle),p.y-t*m.sin(p.angle+angle),p.x+t*m.cos(p.angle-angle),p.y-t*m.sin(p.angle-angle),p.x+t*m.cos(p.angle+angle+m.pi),p.y-t*m.sin(p.angle+angle+m.pi),p.x+t*m.cos(p.angle-angle+m.pi),p.y-t*m.sin(p.angle-angle+m.pi))
		zone_dessin.coords(f,p.x,p.y,round(50*m.cos(p.angle),1)+p.x,p.y+round(50*m.sin(-p.angle),1))
		fenetre.after(50,main)

def Demarrer():
	global arret
	if arret==True:
		arret=False
	main()

def import_file():
	filepath = askopenfilename(title="Ouvrir un fichier",filetypes=[('txt files','.txt'),('all files','.*')])
	fichier = open(filepath,'r')
	content = fichier.read()
			
	fichier.close()

def export_file():
	f=open('Scenario.txt','w')
	for i in b.list_obj:
		f.write('Obstacle(')
		f.write(str(i.x)+',')
		f.write(str(i.y)+',')
		f.write(str(i.forme)+')\n')

	for i in b.list_rob:
		f.write("Robot(")
		f.write(str(i.x)+',')
		f.write(str(i.y)+',')
		f.write(str(i.angle)+')\n')
	f.write("Arene(")
	f.write(str(b.nb_ligne)+',')
	f.write(str(b.nb_colonne)+')\n')

	f.write("Affichage()")

def arreter():
	global arret
	arret=True
	
arret=False	
o=Obstacle(70,10,1)
p=Robot(70,200,0)
b=Arene(500,1000,[o],[p])
z=Affichage(b)


#declarer la fenetre en dernier
fenetre = Tk()#creer une fenetre
fenetre.title('Arene')#donner un nom  la fenetre
fenetre.geometry("1200x600")#donner la taille de la fenetre
		#on definit la zone ou on dessine(fenetre,y,x,couleur d'arrier plan)
BoutonImporter = Button(fenetre, text ='Importer', command = import_file)
BoutonImporter.pack(side = LEFT, padx = 10, pady = 10)

BoutonExporter = Button(fenetre, text ='Exporter', command = export_file)
BoutonExporter.pack(side = LEFT, padx = 10, pady = 10)

BoutonArreter = Button(fenetre, text ='Arreter', command = arreter)
BoutonArreter.pack(side = LEFT, padx = 10, pady = 10)
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
angle=calcul_angle(p.largeur/2,p.longueur/2)
t=calcul_hypo(p.largeur/2,p.longueur/2)
#r=zone_dessin.create_rectangle(p.x-p.largeur/2,p.y-p.longueur/2,p.x+p.largeur/2,p.y+p.longueur/2,fill='green',outline='green')
"""j=p.x+t*m.cos(p.angle+angle)
y=p.y-t*m.sin(p.angle+angle)
g=zone_dessin.create_line(j,y,j+150*m.cos(p.angle),y-150*m.sin(p.angle))

j1=p.x+t*m.cos(p.angle-angle)
y1=p.y-t*m.sin(p.angle-angle)
c=zone_dessin.create_line(j1,y1,j1+150*m.cos(p.angle),y1-150*m.sin(p.angle))"""

r=zone_dessin.create_polygon(p.x+t*m.cos(p.angle+angle),p.y-t*m.sin(p.angle+angle),p.x+t*m.cos(p.angle-angle),p.y-t*m.sin(p.angle-angle),p.x+t*m.cos(p.angle+angle+m.pi),p.y-t*m.sin(p.angle+angle+m.pi),p.x+t*m.cos(p.angle-angle+m.pi),p.y-t*m.sin(p.angle-angle+m.pi),fill='red',outline='red')
#le fleche
f=zone_dessin.create_line(p.x,p.y,round(50*m.cos(p.angle),1)+p.x,p.y+round(50*m.sin(-p.angle),1),arrow='last',fill='yellow')

zone_dessin.pack()
fenetre.mainloop()



