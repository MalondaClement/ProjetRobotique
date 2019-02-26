from tkinter import *
from tkinter.filedialog import *
from arene import*
import math as m
from controler import*

class Affichage(object):
    """La classe arène permet de faire le lien entre notre modèle et notre interface graphique.
        Elle utilise notre matrice pour en faire un représentation concrète dans la fenètre graphique.
        :param arene: l'arène dont on souhaite avoir la représentation en graphique
    """
    def __init__(self,arene,fenetre,robot):
        self.arene=arene
        self.vitesse=10
        self.fenetre=fenetre
        self.p=robot
        self.a=calcul_angle(self.p)
        self.t=calcul_hypo(self.p)


    def afficher(self):
        for i in range(0,self.arene.nb_colonne):
            for j in range(0,self.arene.nb_ligne):
                if self.arene.matrice[j,i]==1:
                    self.zone_dessin.create_rectangle(i,j,i+1,j+1,fill='black')
    def afficher_robot(self):
        p=self.p
        t=self.t
        angle=self.a
        self.r=self.zone_dessin.create_polygon(p.x+t*m.cos(p.angle+angle),p.y-t*m.sin(p.angle+angle),p.x+t*m.cos(p.angle-angle),p.y-t*m.sin(p.angle-angle),p.x+t*m.cos(p.angle+angle+m.pi),p.y-t*m.sin(p.angle+angle+m.pi),p.x+t*m.cos(p.angle-angle+m.pi),p.y-t*m.sin(p.angle-angle+m.pi),fill='red',outline='red')
        self.f=self.zone_dessin.create_line(p.x,p.y,round(50*m.cos(p.angle),1)+p.x,p.y+round(50*m.sin(-p.angle),1),arrow='last',fill='yellow')

    def zone(self):
        self.zone_dessin =Canvas(self.fenetre, width=self.arene.nb_colonne,height=self.arene.nb_ligne,background='white')
        self.zone_dessin.focus_set()
        self.zone_dessin.bind('<Key>',clavier)
        self.zone_dessin.pack()

    def dessiner(self):
        """Cette fonction permet de bouger l'image du robot et de sa fleche selon les coordonnée du robot
        """
        p=self.p
        t=self.t
        angle=self.a
        self.zone_dessin.coords(self.r,p.x+t*m.cos(p.angle+angle),p.y-t*m.sin(p.angle+angle),p.x+t*m.cos(p.angle-angle),p.y-t*m.sin(p.angle-angle),p.x+t*m.cos(p.angle+angle+m.pi),p.y-t*m.sin(p.angle+angle+m.pi),p.x+t*m.cos(p.angle-angle+m.pi),p.y-t*m.sin(p.angle-angle+m.pi))
        self.zone_dessin.coords(self.f,p.x,p.y,round(50*m.cos(p.angle),1)+p.x,p.y+round(50*m.sin(-p.angle),1))
