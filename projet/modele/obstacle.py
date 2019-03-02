class Obstacle(object):
    """ Obstacle est une classe qui permet de creer des objets dans notre arène
    :param x: position en x dans la matrice du centre de l'obstacle
    :param y: position en y dans la matrice du centre de l'obstacle
    :param forme: permet la gestion de la forme, 1 pour carré, 2 rond, 3 triangle
    ...
    """
    def __init__(self, x, y,forme):
        self.x = x
        self.y = y
        self.forme = forme
        
                
class ObstacleRectangle(Obstacle):
    """ ObstacleRectagle est une classe fille de Obstacle qui permet de creer des objets rectangulaires (et carrés) dans notre arène
    :param x: position en x dans la matrice du centre de l'obstacle
    :param y: position en y dans la matrice du centre de l'obstacle
    :param largeur: largeur du coté 
    :param longueur: longeur du coté (si largeur == longueur alors on a un carré)
    """
    def __init__(self,x, y, largeur, longueur):
        Obsatacle.__init__(self,x,y,1)
        self.largeur=largeur
        self.longueur=longueur
        
class ObstacleEllipse(Obstacle):
    """ ObstacleEllipse est une classe fille de Obstacle qui permet de creer des objets elliptiques (et circulaires) dans notre arène
    :param x: position en x dans la matrice du centre de l'obstacle
    :param y: position en y dans la matrice du centre de l'obstacle
    :param grand_r: grand rayon 
    :param petit_r: petit rayon (si grand_r == petit_r alors on a un cercle)
    """
    def __init__(self,x, y, grand_r, petit_r):
        Obsatacle.__init__(self,x,y,2)
        self.grand_r=grand_r
        self.petit_r=petit_r

class ObstacleTringle(Obstacle):
    """ ObstacleTringle est une classe fille de Obstacle qui permet de creer des objets triangulaires dans notre arène
    :param x: position en x dans la matrice du centre de l'obstacle
    :param y: position en y dans la matrice du centre de l'obstacle
    :param hauteur: hauteur du triangle 
    :param base: base du triangle
    """
    def __init__(self,x, y, hauteur, base):
        Obsatacle.__init__(self,x,y,3)
        self.hauteur=hauteur
        self.base=base
