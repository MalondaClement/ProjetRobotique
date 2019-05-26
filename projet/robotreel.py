from math import pi,atan,cos,sin,pow,sqrt,fabs
import time

WHEEL_BASE_WIDTH         = 117  # distance (mm) de la roue gauche a la roue droite.
WHEEL_DIAMETER           = 66.5 #  diametre de la roue (mm)
WHEEL_BASE_CIRCUMFERENCE = WHEEL_BASE_WIDTH * pi # perimetre du cercle de rotation (mm)
WHEEL_CIRCUMFERENCE      = WHEEL_DIAMETER   * pi # perimetre de la roue (mm)
MOTOR_LEFT = 1
MOTOR_RIGHT = 2


class RobotReel(object) :
    """ La classe RobotReel est une classe qui à pour but d'être la plus plroche possible de l'API du robot que
        nous utilisons dans le projet. Pour cela cette classe a été developpées avec uniquent les fonctions de
        l'API, seul le corps est différents, le code n'aura donc pas a être modifié si nous passons de la
        simulation au monde réel.
            :param x: coordonnée x du robot dans l'arène
            :param y: coordonnée y du robot dans l'arène
            :param angle: angle du robot en radian
            :param arene: arène de simulation dans lequel il se trouve (matrice)
    """
    def __init__(self,x,y,angle, arene):
        self.x=x
        self.y=y
        self.angle=angle
        self.angle_tete=90
        self.largeur=20
        self.longueur=50
        self.arene= arene
        self.MOTOR_LEFT_DPS=0
        self.MOTOR_RIGHT_DPS=0
        self.MOTOR_LEFT_ROTATION =0
        self.MOTOR_RIGHT_ROTATION = 0
        self.WHEEL_BASE_WIDTH         = 117 # distance (mm) de la roue gauche a la
        self.WHEEL_DIAMETER           = 66.5 #  diametre de la roue (mm)
        self.WHEEL_BASE_CIRCUMFERENCE = self.WHEEL_BASE_WIDTH * pi
        self.WHEEL_CIRCUMFERENCE      = self.WHEEL_DIAMETER   * pi
        self.MOTOR_LEFT = 1
        self.MOTOR_RIGHT = 2

    def set_motor_dps(self, port,dps):
        """ Fixe la vitesse du robot
            - port=1 pour la roue gauche, 2 pour la roue droite, 3 pour les 2 roues
            - dps est une vitesse angulaire en degré par seconde
        """
        if port == MOTOR_LEFT :
            self.MOTOR_LEFT_DPS = dps
        elif port == MOTOR_RIGHT :
            self.MOTOR_RIGHT_DPS = dps
        elif port ==MOTOR_LEFT+MOTOR_RIGHT :
            self.MOTOR_RIGHT_DPS = self.MOTOR_LEFT_DPS = dps

    def get_motor_position (self) :
        return self.MOTOR_LEFT_ROTATION, self.MOTOR_RIGHT_ROTATION

    def offset_motor_encoder (self, port, offset) :
        #port=1 pour la roue gauche, 2 pour la roue droite, 3 pour les 2 roues
        if port == MOTOR_LEFT :
            self.MOTOR_LEFT_ROTATION -= offset
        elif port == MOTOR_RIGHT :
            self.MOTOR_RIGHT_ROTATION -= offset
        elif port ==MOTOR_LEFT+MOTOR_RIGHT :
            self.MOTOR_RIGHT_ROTATION -= offset
            self.MOTOR_LEFT_ROTATION -= offset

    def get_distance (self) :
        """Rcupération de la distance qui sépare de l'obstacle
            :returns: la distance au plus proche obstacle
        """
        recherche_x= self.x +(self.largeur/2)*cos(self.angle+self.angle_tete-90)
        recherche_y= self.y -(self.longueur/2)*sin(self.angle+self.angle_tete-90)
        #print(recherche_y,recherche_x)
        test=0
        while test==0:
            recherche_x+=cos(self.angle+self.angle_tete-90)*2
            recherche_y-=sin(self.angle+self.angle_tete-90)*2
            recherche_x=int(round(recherche_x,0))
            recherche_y=int(round(recherche_y,0))
            if recherche_x<0 or recherche_y<0 or recherche_x>self.arene.nb_colonne or recherche_y>self.arene.nb_ligne:
                test=1
            else if self.arene.matrice[recherche_y, recherche_x]==1:
                test=1

        distance= sqrt(pow(recherche_x-(self.x+(self.largeur/2)*cos(self.angle)), 2) + pow(recherche_y-(self.y-(self.longueur/2)*sin(self.angle)), 2))
        if distance < 5 or distance > 8000 :
            distance = 8190
        return distance

    def servo_rotate(self,position):
        if position >= 0 and position <= 180:
            self.angle_tete = position

    def stop (self) :
        """Arrete le robot
        """
        self.MOTOR_LEFT_DPS = self.MOTOR_RIGHT_DPS = 0

    def actualiser(self) :
        """ Réalise une actualisation de la position et/ou de l'angle du robot
        """
        self.MOTOR_LEFT_ROTATION+= self.MOTOR_LEFT_DPS /20
        self.MOTOR_RIGHT_ROTATION+= self.MOTOR_RIGHT_DPS /20
        print(self.MOTOR_LEFT_ROTATION, self.MOTOR_RIGHT_ROTATION)

        if self.MOTOR_RIGHT_DPS == self.MOTOR_LEFT_DPS :

            self.x+= cos(self.angle)* (((self.MOTOR_LEFT_DPS/20) * self.WHEEL_DIAMETER )/ 360 ) /10 #conversion en cm
            self.y-= sin(self.angle)* (((self.MOTOR_LEFT_DPS/20) * self.WHEEL_DIAMETER )/ 360 ) /10

        else:
            if self.MOTOR_RIGHT_DPS == -self.MOTOR_LEFT_DPS :
                self.angle+= (((self.MOTOR_RIGHT_DPS/20)*self.WHEEL_CIRCUMFERENCE/self.WHEEL_BASE_CIRCUMFERENCE) * (pi/180))
            else :
                rayon = (self.WHEEL_BASE_WIDTH/2*(self.MOTOR_RIGHT_DPS+self.MOTOR_LEFT_DPS)/(self.MOTOR_RIGHT_DPS-self.MOTOR_LEFT_DPS))/10
                vitesserg=self.MOTOR_LEFT_DPS*WHEEL_DIAMETER/360
                vitesserd=self.MOTOR_RIGHT_DPS*WHEEL_DIAMETER/360
                pourcentage=(2*pi*(rayon+WHEEL_BASE_WIDTH)/ max(vitesserd, vitesserg) /100)/20
                angle_rotation=2*pi*pourcentage
                angle_tournage=(pi/2)-((2*pi- angle_rotation) / 2)
                AB = (cos((2*pi- angle_rotation)/2)*2*rayon)/20
                if self.MOTOR_RIGHT_DPS > self.MOTOR_LEFT_DPS :
                    self.angle -= (angle_tournage*pi/90)
                    self.x -= cos(self.angle) * AB
                    self.y += sin(self.angle) * AB
                    self.angle -= (angle_tournage*pi/90)
                else:
                    self.angle += (angle_tournage*pi/90)
                    self.x += cos(self.angle) * AB
                    self.y -= sin(self.angle) * AB
                    self.angle += (angle_tournage*pi/90)
                #time.sleep(0.5)
                
                #print(self.x , self.y)

    def calcul_angle(self):
        """Cette fonction permet de faire le calcul de l'angle de la demi droite de recherche d'obstacle
            :returns : Angle de la demi-droite
        """
        a=atan(self.largeur/self.longueur)
        return a

    def calcul_hypo(self):
        """
        """
        a=pow(self.largeur/2,2)+pow(self.longueur/2,2)
        return sqrt(a)

               
