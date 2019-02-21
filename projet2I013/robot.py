import math as m

class Robot(object):
    """La classe robot permet de construire un robot avec sa position et son angle.
        :param x,y: position x,y du robot
        :param angle: angle d'oriantation du robot en RADIAN
    """
    def __init__(self,x,y,angle):
        self.x=x
        self.y=y
        self.angle=angle
        self.largeur=20
        self.longueur=50

    def get_position(self):
        return self.x, self.y

    def obstacle (self, originex, originey, arene, pas):
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
                    recherche_x+=m.cos(self.angle)*pas
                    recherche_y-=m.sin(self.angle)*pas
                    recherche_x=int(round(recherche_x,0))
                    recherche_y=int(round(recherche_y,0))
                    if recherche_x<0 or recherche_y<0 or recherche_x>arene.nb_colonne or recherche_y>arene.nb_ligne:
                        return recherche_x, recherche_y
                    if arene.matrice[recherche_y, recherche_x]==1:
                        return recherche_x, recherche_y

    def changer_angle(self, delta):
        """Cette fonction permet de changer l'oriantation de notre robot.
            :param delta: le fragment d'angle que l'on souhaite ajouter en RADIAN
            Si ramène la valeur entre 0 et 2pi si besoin
        """
        self.angle+=delta
        while self.angle>(m.pi)*2:
            self.angle-=(m.pi)*2
        while self.angle<0:
            self.angle+=(m.pi)*2

    def avancer (self, distance):
        """Cette fonction permet de faire avancer notre robot de la distance donnée
            :param distance: distance à déplacer du robot
        """
        self.x+=m.cos(self.angle)*distance
        self.x=int(round(self.x,1))
        self.y-=m.sin(self.angle)*distance
        self.y=int(round(self.y,1))

    def calcul_angle(self):
        """Cette fonction permet de faire le calcul de l'angle de la demi droite de recherche d'obstacle
            :returns : Angle de la demi-droite
        """
        a=m.atan(self.largeur/self.longueur)
        return a

    def calcul_hypo(self):
        """
        """
        a=m.pow(self.largeur/2,2)+m.pow(self.longueur/2,2)
        return m.sqrt(a)


    def distancemax(self,arene):
        MAX=50
        angle=self.calcul_angle()
        t=self.calcul_hypo()
        a,b=self.obstacle(self.x,self.y-t*m.sin(self.angle),arene,1)
        if m.sqrt(pow(a-self.x, 2) + pow(b-self.y, 2)) < MAX:
            return True
        a,b=self.obstacle(self.x+t*m.cos(self.angle+angle),self.y-t*m.sin(self.angle+angle),arene,1)
        if m.sqrt(pow(a-self.x, 2) + pow(b-self.y, 2)) < MAX:
            return True
        a,b=self.obstacle(self.x+t*m.cos(self.angle-angle),self.y-t*m.sin(self.angle-angle),arene,1)
        if m.sqrt(pow(a-self.x, 2) + pow(b-self.y, 2)) < MAX:
            return True
        return False
