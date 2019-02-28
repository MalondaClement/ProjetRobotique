import numpy as np
from robot import Robot
from obstacle import Obstacle
from math import pow,atan,sqrt

#j'ai juste fait le cas ou la forme est un caree
class Arene(object):

    """La classe arene permet la représentation des éléments dans l'arène pour faire nos calculs comme la détection d'obtacle.
    Elle gère une matrice dans laquelle chaque élément correpond à un "object" à cette position dans l'arene.
    La matrice est initialement vide (valeurs à 0).
    Si 0 il n'y a rien, si 1 on a un obstacle, si 2 on a le robot.
        :param nb_ligne: nb de lignes de la matrice correpond au pixels
        :param nb_colonne: nb de colonnes de la matrice correpond au pixels
        :param list_obj: liste d'élément de type obstacle à placer dans la matrice
        :param list_rob: liste d'élément de type robotà mettre dans la matrice, dans un premier temps 1 seul
    """
    def __init__(self,nb_ligne, nb_colonne):
        self.nb_ligne=nb_ligne
        self.nb_colonne=nb_colonne
        self.matrice=np.zeros((nb_ligne,nb_colonne))
        self.list_rob=[]
        self.list_obj=[]
        #cree les mur

    def cree_mur(self):
        """Cette fonction permet de mettre les valeurs des bords à 1 afin de les murs.
        """
        for i in range(0,self.nb_ligne):
            for j in range(0,self.nb_colonne):
                if (i == 0) or (j==0) or (i==self.nb_ligne-1) or (j==self.nb_colonne-1):
                    self.matrice[i,j] =1

    def est_dans_matrice(self,o):
        """Cette fonction permet de vérifier si un intertion est bien dans la matrice
            :returns : True si on incère dans la matrice False sinon
        """
        if o.x-o.largeur//2>0 and o.x+o.largeur//2<self.nb_colonne and o.y-o.longueur//2>0 and o.y+o.longueur//2<self.nb_ligne:
            return True

    def est_vide(self,o):
        """
        """
        for p in range(i.y - i.longueur//2,i.y + i.longueur//2):
            for q in range(i.x - i.largeur//2,i.x + i.largeur//2):
                if self.matrice[p,q]!=0:
                    return False
        return True

    def remplir_matrice(self,i,val):
        for p in range(i.y - i.longueur//2,i.y + i.longueur//2):
            for q in range(i.x - i.largeur//2,i.x + i.largeur//2):
                    self.matrice[p,q]=val

    def inserer_robot(self,r):
        """Cette fonction permet d'inserer un robot dans l'arène
            :param r: on passe en paramètre le robot à placer dans la matrice qui représente l'arène
            La fonction fait appel aux fonctions est_dans_matrice et est_vide.
        """
        if self.est_dans_matrice(r) and self.est_vide:
            self.matrice[r.y,r.x]=2
            self.list_rob.append(r)

    def inserer_obs(self,o):
        """Cette fonction permet d'inserer un obstacle dans l'arène
            :param o: on passe en paramètre l'obstacle à placer dans la matrice qui représente l'arène
            La fonction fait appel aux fonctions est_dans_matrice et est_vide.
        """
        if self.est_dans_matrice(o) and self.est_vide:
            self.remplir_matrice(o,1)
            self.list_obj.append(o)


    def get_object(self,x,y):
        """Cette fonction permet de savoir si on a un objet est présente dans la case de la matrice.
            :param x,y: coordonnées de la case que l'on souhaite regarder
            :returns : 0 si vide, 1 si obstacle, 2 si robot
        """
        return int(self.matrice[x,y])

def calcul_angle(p):
    a=atan(p.largeur/p.longueur)
    return a

def calcul_hypo(p):
    a=pow(p.largeur/2,2)+pow(p.longueur/2,2)
    return sqrt(a)

