import pyglet
import pyglet.gl as pgl
from PIL.Image import*
from pyglet.window import key
import OpenGL.GL as ogl
from modele.obstacle import*
import math as m
import time
from modele.controleur_robotreel_carre import ControleurRobotReelCarre
from modele.controleur_robotreel_mur import ControleurRobotReelMur
from threading import Thread 



class Affichage(Thread):

    def __init__(self, fenetre3d,arene,robot):
        super(Affichage,self).__init__()
        self.fenetre3d = fenetre3d
        pgl.glClearColor(0, 0, 0, 1)
        pgl.glEnable(pgl.GL_DEPTH_TEST)
        self.r=ObstacleRectangle(0,0,10,50)
        self.robot=robot
        self.arene=arene
        self.x=200
        #self.ctrl=ControleurRobotReelMur(self.robot)
        self.ctrl=ControleurRobotReelCarre(self.robot)
        self.rouge=(255,0,0,255)
        self.jaune=(255,255,0,255)
        self.bleu=(0,0,255,255)
        self.vert=(0,255,0,255)
        self.tableau=[self.jaune,self.rouge,self.bleu,self.vert]
        self.tmp=list(self.tableau)
        self.centre=(0,0)

    def draw(self) :
        for i in self.arene.list_obj:
            i.hauteur=50
            # Effacer la fenetre
            #self.fenetre3d.clear()

            # Creation d'une matrice
            #pgl.glPushMatrix()

            # Debut du dessin
            #pgl.glBegin(ogl.GL_QUADS)
            x=i.x-i.largeur//2
            y=i.y-i.longueur//2

            # Premier carre rouge de derrier
            pgl.glColor3ub(255, 0, 0)
            pgl.glVertex3f(x, 0, y)
            pgl.glVertex3f(x, i.hauteur, y)
            pgl.glVertex3f(x+i.largeur, i.hauteur, y)
            pgl.glVertex3f(x+i.largeur, 0, y)

            # Second carre bleu de gauche
            pgl.glColor3ub(0, 0, 255)
            pgl.glVertex3f(x, 0, y)
            pgl.glVertex3f(x, i.hauteur, y)
            pgl.glVertex3f(x, i.hauteur, y+i.longueur)
            pgl.glVertex3f(x, 0, y+i.longueur)

            # Troisieme carre vert du dessous
            pgl.glColor3ub(0, 255, 0)
            pgl.glVertex3f(x, 0, y)
            pgl.glVertex3f(x+i.largeur, 0, y)
            pgl.glVertex3f(x+i.largeur, 0, y+i.longueur)
            pgl.glVertex3f(x, 0, y+i.longueur)

            # Quatrieme carre rose de droite
            pgl.glColor3ub(255, 0, 255)
            pgl.glVertex3f(x+i.largeur, 0, y)
            pgl.glVertex3f(x+i.largeur, i.hauteur, y)
            pgl.glVertex3f(x+i.largeur, i.hauteur, y+i.longueur)
            pgl.glVertex3f(x+i.largeur, 0, y+i.longueur)

            # Cinquieme carre gris fclair du haut
            pgl.glColor3ub(122, 122, 122)
            pgl.glVertex3f(x, i.hauteur, y)
            pgl.glVertex3f(x+i.largeur, i.hauteur, y)
            pgl.glVertex3f(x+i.largeur, i.hauteur, y+i.longueur)
            pgl.glVertex3f(x, i.hauteur, y+i.longueur)

            # Sixieme face fonce
            pgl.glColor3ub(40, 40, 40)
            pgl.glVertex3f(x, 0, y+i.longueur)
            pgl.glVertex3f(x, i.hauteur, y+i.longueur)
            pgl.glVertex3f(x+i.largeur, i.hauteur, y+i.longueur)
            pgl.glVertex3f(x+i.largeur, 0, y+i.longueur)
            # Fin du dessin
            #pgl.glEnd()

            # Effacer la matrice
            #pgl.glPopMatrix()
            #pgl.glFlush()
    def on_draw(self):
        self.fenetre3d.clear()
        #pgl.glPushMatrix()
        #pgl.glRotatef(self.fenetre3d.xRotation, 0, 1, 0)
        #pgl.glRotatef(0, 0, 1, 1)
        pgl.glBegin(ogl.GL_QUADS)
        #bleu
        pgl.glColor3ub(0, 0, 255)
        pgl.glVertex3f(0, 0, 0)
        pgl.glVertex3f(0,10, 0)
        pgl.glVertex3f(self.arene.nb_colonne, 10, 0)
        pgl.glVertex3f(self.arene.nb_colonne, 0, 0)
        #rouge
        pgl.glColor3ub(255, 0, 0)
        pgl.glVertex3f(self.arene.nb_colonne, 0, 0)
        pgl.glVertex3f(self.arene.nb_colonne,10, 0)
        pgl.glVertex3f(self.arene.nb_colonne, 10, self.arene.nb_ligne)
        pgl.glVertex3f(self.arene.nb_colonne, 0, self.arene.nb_ligne)
        
        #vert
        pgl.glColor3ub(0, 255, 0)
        pgl.glVertex3f(0, 0, self.arene.nb_ligne)
        pgl.glVertex3f(0,10, self.arene.nb_ligne)
        pgl.glVertex3f(self.arene.nb_colonne, 10, self.arene.nb_ligne)
        pgl.glVertex3f(self.arene.nb_colonne, 0, self.arene.nb_ligne)
        
        #jaune
        pgl.glColor3ub(255, 255, 0)
        pgl.glVertex3f(00, 0, 00)
        pgl.glVertex3f(00,10, 00)
        pgl.glVertex3f(00, 10, self.arene.nb_ligne)
        pgl.glVertex3f(00, 0, self.arene.nb_ligne)
        
        #blanc
        pgl.glColor3ub(255, 255, 255)
        pgl.glVertex3f(00, 0, self.arene.nb_ligne)
        pgl.glVertex3f(00,0, 0)
        pgl.glVertex3f(self.arene.nb_colonne, 0, 0)
        pgl.glVertex3f(self.arene.nb_colonne, 0, self.arene.nb_ligne)
        
        self.draw()
        pgl.glEnd()
        kitten = pyglet.image.load('balise2.png')
        sprite = pyglet.sprite.Sprite(kitten)
        sprite.set_position(00,80)
        sprite.draw()
        pyglet.image.get_buffer_manager().get_color_buffer().save('screenshot.png')
        pgl.glFlush()
        
    def couleur(self,i,x,y):       
        for p in self.tmp:
          if i.getpixel((x,y))==p:  
            return True,p
        return False,p

    def recherche_balise(self):
        i=open('screenshot.png')
        (largeur, hauteur)= i.size
        for k in range(hauteur):
          for j in range(largeur):
              d,e=self.couleur(i,j,k)
              if d:
                a=self.balise(i,j,k,e)
                j=a[1][0]
                k=a[1][1]
                if len(self.tmp)==1:
                    print(self.centre)
                    print("fini")
                    return True
        print("perdu")
                 
    def balise(self,i,x,y,c):
        self.tmp.remove(c)
        if len(self.tmp)==3:
            for x in range(x,i.size[0]):
                if i.getpixel((x,y))!=c and (self.couleur(i,x,y)[0]):
                  return True,(x,y)
            self.tmp=list(self.tableau)
            return False,(x,y)
        elif len(self.tmp)==2:
            for y in range(y,i.size[1]):
                if i.getpixel((x,y))!=c and (self.couleur(i,x,y)[0]):
                  print(x,y)
                  self.centre=(x,y)
                  return True,(x,y)
            self.tmp=list(self.tableau)
            return False,(x,y)
        elif len(self.tmp)==1:
            for x in range(0,x):
                if i.getpixel((x,y))!=c and (self.couleur(i,x,y)[0]):
                  return True,(x,y)
            self.tmp=list(self.tableau)
            self.centre=(0,0)
            return False,(x,y)
        
    def obstacle (self, robot,originex, originey, arene, pas):
        """Cette fonction permet la détection des obstacles se trouvant sur une demi devant le robot ?
            :param originex: x de l'origine de la demi-droite
            :param origeney: y de l'origine de la demi-droite
            :param arene: arene (matrice) dans lequel se trouve le robot
            :param pas: pas entre chaque avancer sur la demi-droite de détection
            :returns : position x, y de l'obstacle qui permetra le calcul de la distance avec celui-ci
        """
        recherche_x= originex
        recherche_y= originey
        while True:
                    recherche_x+=m.cos(robot.angle)*pas
                    recherche_y-=m.sin(robot.angle)*pas
                    #recherche_x=int(round(recherche_x,0))
                    #recherche_y=int(round(recherche_y,0))
                    if recherche_x<0 or recherche_y<0 or recherche_x>arene.nb_colonne or recherche_y>arene.nb_ligne:
                        return recherche_x, recherche_y
                    if arene.matrice[int(recherche_y), int(recherche_x)]==1:
                        return recherche_x, recherche_y

    def on_resize(self, width, height):

        # Definir le repere (la zone de la fenetre utilisee)
        #pgl.glViewport(0, 0, width, height)

        # Utiliser une projection
        pgl.glMatrixMode(ogl.GL_PROJECTION)
        pgl.glLoadIdentity()
        #self.x-=1
        Ratio = width/height
        pgl.gluPerspective(35, Ratio, 1, 1000)
        x=self.robot.x+m.cos(self.robot.angle)*(self.robot.largeur//2)
        y=self.robot.y-m.sin(self.robot.angle)*(self.robot.longueur//2)
        a,b=self.obstacle(self.robot,self.robot.x,self.robot.y,self.arene,1)
        #print(x,y)
        pgl.gluLookAt(x, 10, y, a, 0, b, 0, 1, 0)
        pgl.glMatrixMode(ogl.GL_MODELVIEW)

        #pgl.glTranslatef(0, 0, -400)

    def update(self,dt):
        pass
        #self.recherche_balise()
        """if not self.ctrl.stop():
            self.ctrl.update()
            self.on_resize(600,600)
            self.on_draw()"""
            


