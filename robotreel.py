from math import pi,atan,cos,sin,pow,sqrt

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
        self.largeur=20
        self.longueur=50
        self.arene= arene
        self.MOTOR_LEFT_DPS=0
        self.MOTOR_RIGHT_DPS=0
        self.MOTOR_LEFT_ROTATION =0
        self.MOTOR_RIGHT_ROTATION = 0


    def set_motor_dps(self, port,dps):
        """ Fixe la vitesse du robot
            - port=1 pour la roue gauche, 2 pour la roue droite, 3 pour les 2 roues
            - dps est une vitesse angulaire en degré par seconde
        """
        if port == MOTOR_LEFT :
            self.MOTOR_LEFT = dps
        elif port == MOTOR_RIGHT :
            self.MOTOR_RIGHT_DPS = dps
        elif port ==MOTOR_LEFT+MOTOR_RIGHT :
            self.MOTOR_RIGHT_DPS = self.MOTOR_LEFT_DPS = dps

    def get_motor_position (self) :
        return MOTOR_LEFT_ROTATION, MOTOR_RIGHT_ROTATION

    def offset_motor_encoder (self, port, offset) :
        #port=1 pour la roue gauche, 2 pour la roue droite, 3 pour les 2 roues
        if port == MOTOR_LEFT :
            self.MOTOR_LEFT_ROTATION = offset
        elif port == MOTOR_RIGHT :
            self.MOTOR_RIGHT_ROTATION = offset
        elif port ==MOTOR_LEFT+MOTOR_RIGHT :
            self.MOTOR_RIGHT_ROTATION = self.MOTOR_LEFT_ROTATION = offset

    def get_distance (self) :
        """Rcupération de la distance qui sépare de l'obstacle
            :returns: la distance au plus proche obstacle
        #je n'ai pas compris les valeurs de l'intervalle de détection du robot -> fonction à préciser
        """
        recherche_x= self.x +(self.longueur/2)*cos(angle)
        recherche_y= self.y -(self.longueur/2)*sin(angle)
        test=0
        while test==0:
            recherche_x+=cos(self.angle)*2
            recherche_y-=sin(self.angle)*2
            recherche_x=int(round(recherche_x,0))
            recherche_y=int(round(recherche_y,0))
            if recherche_x<0 or recherche_y<0 or recherche_x>self.arene.nb_colonne or recherche_y>self.arene.nb_ligne:
                test=1
            if self.arene.matrice[recherche_y, recherche_x]==1:
                test=1
        return sqrt(pow(recherche_x-self.x, 2) + pow(recherche_y-self.y, 2))


    def stop (self) :
        """Arrete le robot
        """
        self.MOTOR_LEFT_DPS == MOTOR_RIGHT_DPS = 0 #c'est pas un self.MOTOR_RIGHT_DPS ?

    def actualiser(self) :
        """ Réalise une actualisation de la position, ou de l'angle du robot
        """
        if MOTOR_RIGHT_DPS = MOTOR_LEFT_DPS :
            x+= cos(angle)* (((MOTOR_LEFT_DPS/20) * WHEEL_DIAMETER )/ 360 ) /10 #conversion en cm
            y-= sin(angle)* (((MOTOR_LEFT_DPS/20) * WHEEL_DIAMETER )/ 360 ) /10

        elif MOTOR_RIGHT_DPS == -MOTOR_LEFT_DPS :
            angle+= (MOTOR_RIGHT_DPS*WHEEL_CIRCUMFERENCE/WHEEL_BASE_CIRCUMFERENCE) * (pi/180)
