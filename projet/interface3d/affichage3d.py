import pyglet
import pyglet.gl as pgl
from pyglet.window import key
import OpenGL.GL as ogl
from .affichage3d import *
from modele.obstacle import*
import math as m


class Affichage(object):

    def __init__(self, fenetre3d):
        self.fenetre3d = fenetre3d
        pgl.glClearColor(0, 0, 0, 1)
        pgl.glEnable(pgl.GL_DEPTH_TEST)
        self.r=ObstacleRectangle(0,0,50,10)

    def on_draw(self) :
        z=m.sqrt(self.r.largeur**2+self.r.longueur**2)

        # Effacer la fenetre
        self.fenetre3d.clear()

        # Creation d'une matrice
        pgl.glPushMatrix()

        # Definit la rotation autour de l'axe choisi par la suite 
        pgl.glRotatef(self.fenetre3d.xRotation, 0, 1, 0)
        pgl.glRotatef(self.fenetre3d.yRotation, 0, 1, 1)

        # Debut du dessin
        pgl.glBegin(ogl.GL_QUADS)

        # Premier carre rouge
        pgl.glColor3ub(255, 0, 0)
        pgl.glVertex3f(0, 0, 0)
        pgl.glVertex3f(0, self.r.largeur, 0)
        pgl.glVertex3f(self.r.longueur, self.r.largeur, 0)
        pgl.glVertex3f(self.r.longueur, 0, 0)

        # Second carre bleu
        pgl.glColor3ub(0, 0, 255)
        pgl.glVertex3f(0, 0, 0)
        pgl.glVertex3f(0, self.r.longueur, 0)
        pgl.glVertex3f(0, self.r.longueur, z)
        pgl.glVertex3f(0, 0, z)

        # Troisieme carre vert
        pgl.glColor3ub(0, 255, 0)
        pgl.glVertex3f(0, self.r.largeur, 0)
        pgl.glVertex3f(0, self.r.largeur, z)
        pgl.glVertex3f(self.r.longueur, self.r.largeur, z)
        pgl.glVertex3f(self.r.longueur, self.r.largeur, 0)

        # Quatrieme carre rose
        pgl.glColor3ub(255, 0, 255)
        pgl.glVertex3f(self.r.longueur, 0, 0)
        pgl.glVertex3f(self.r.longueur, self.r.largeur, 0)
        pgl.glVertex3f(self.r.longueur, self.r.largeur, z)
        pgl.glVertex3f(self.r.longueur, 0, z)

        # Cinquieme carre gris fclair
        pgl.glColor3ub(122, 122, 122)
        pgl.glVertex3f(0, 0, 0)
        pgl.glVertex3f(self.r.longueur, 0, 0)
        pgl.glVertex3f(self.r.longueur, 0, z)
        pgl.glVertex3f(0, 0, self.r.largeur)

        # Sixieme face fonce
        pgl.glColor3ub(40, 40, 40)
        pgl.glVertex3f(0, 0, self.r.largeur)
        pgl.glVertex3f(self.r.longueur, 0, z)
        pgl.glVertex3f(self.r.longueur, self.r.largeur, z)
        pgl.glVertex3f(0, self.r.largeur, z)

        # Fin du dessin
        pgl.glEnd()

        # Effacer la matrice
        pgl.glPopMatrix()

    def on_resize(self, width, height):

        # Definir le repere (la zone de la fenetre utilisee)
        pgl.glViewport(0, 0, width, height)

        # Utiliser une projection
        pgl.glMatrixMode(ogl.GL_PROJECTION)
        pgl.glLoadIdentity()

        Ratio = width/height
        pgl.gluPerspective(35, Ratio, 1, 1000)
        pgl.gluLookAt(0, 0, self.fenetre3d.far, 0, 0, 0, 0, 1, 0)

        pgl.glMatrixMode(ogl.GL_MODELVIEW)

        pgl.glTranslatef(0, 0, -400)




    def on_text_motion(self,motion):
        if motion == key.UP :
            self.fenetre3d.xRotation -= INCREMENT 
        elif motion == key.DOWN :
            self.fenetre3d.xRotation += INCREMENT
        elif motion == key.LEFT :
            self.fenetre3d.yRotation -= INCREMENT
        elif motion == key.RIGHT :
            self.fenetre3d.yRotation += INCREMENT

