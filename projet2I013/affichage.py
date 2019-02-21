from tkinter import *
import window.fenetre
# from tkinter import *
# from arene import Arene
# from arene import calcul_hypo
# from arene import calcul_angle
# from robot import Robot
# from obstacle import Obstacle
# import math as m
# from tkinter.filedialog import *

class Affichage(object):
    """La classe arène permet de faire le lien entre notre modèle et notre interface graphique.
        Elle utilise notre matrice pour en faire un représentation concrète dans la fenètre graphique.
        :param arene: l'arène dont on souhaite avoir la représentation en graphique
    """
    def __init__(self,arene,fenetre):
        self.arene=arene
        self.vitesse=10
        self.fenetre=fenetre

    def afficher(self):
        print (self.arene.matrice)
        for i in range(0,self.arene.nb_colonne):
            for j in range(0,self.arene.nb_ligne):
                if self.arene.matrice[j,i]==1:
                    zone_dessin.create_rectangle(i,j,i+1,j+1,fill='black')
    def afficher_robot(self):
        global r
        r=zone_dessin.create_polygon(p.x+t*m.cos(p.angle+angle),p.y-t*m.sin(p.angle+angle),p.x+t*m.cos(p.angle-angle),p.y-t*m.sin(p.angle-angle),p.x+t*m.cos(p.angle+angle+m.pi),p.y-t*m.sin(p.angle+angle+m.pi),p.x+t*m.cos(p.angle-angle+m.pi),p.y-t*m.sin(p.angle-angle+m.pi),fill='red',outline='red')
        global f
        f=zone_dessin.create_line(p.x,p.y,round(50*m.cos(p.angle),1)+p.x,p.y+round(50*m.sin(-p.angle),1),arrow='last',fill='yellow')

    def zone(self):
        global zone_dessin
        zone_dessin =Canvas(fenetre, width=self.arene.nb_colonne,height=self.arene.nb_ligne,background='white')
        zone_dessin.focus_set()
        zone_dessin.bind('<Key>',clavier)
        zone_dessin.pack()

def dessiner():
    """Cette fonction permet de bouger l'image du robot et de sa fleche selon les coordonnée du robot
    """
    zone_dessin.coords(r,p.x+t*m.cos(p.angle+angle),p.y-t*m.sin(p.angle+angle),p.x+t*m.cos(p.angle-angle),p.y-t*m.sin(p.angle-angle),p.x+t*m.cos(p.angle+angle+m.pi),p.y-t*m.sin(p.angle+angle+m.pi),p.x+t*m.cos(p.angle-angle+m.pi),p.y-t*m.sin(p.angle-angle+m.pi))
    zone_dessin.coords(f,p.x,p.y,round(50*m.cos(p.angle),1)+p.x,p.y+round(50*m.sin(-p.angle),1))
