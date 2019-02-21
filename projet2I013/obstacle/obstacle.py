class Obstacle(object):
    """ Obstacle est une classe qui permet de créer des objets dans notre arène
    :param x: position en x dans la matrice du centre de l'obstacle
    :param y: position en y dans la matrice du centre de l'obstacle
    :param forme: permet la gestion de la forme, 1 pour carré, 2 rond, 3 triangle
    ...
"""
    def __init__(self, x, y, forme, para1, para2):
        self.x = x
        self.y = y
        self.forme = forme
        self.para1=para1
        self.para2=para2
        if self.forme == 1 : #carre
            self.creer_carree (para1,para2)
        elif self.forme == 2 : #rond
            self.creer_rond(para1,para2)
        elif self.forme == 3 : #triangle
            self.creer_triangle(para1,para2)
        elif self.forme==4: #rectangle
            self.creer_rectangle(para1,para2)
        else :
            self.creer_carree(para1,para2)

    def creer_carree (self,para1, para2):
        """Fonction permetant la création d'un obstacle carré
            :param para1: valeur de la longueur et de la largeur
            :param para2: si para1 vaut 0 on prend para2 sinon valeur par defaut 30
        """
        if para1!=0 and para2!=0:
            self.largeur = self.longueur = 30
            print ("paramètres incorrects :création d'un carré par défaut")
        else:
            if para1!=0 :
                self.longueur = self.largeur= para1
            else :
                self.longueur = self.largeur= para2

    def creer_rond (self,para1,para2):
            """Fonction permetant la création d'un obstacle rond
                :param para1: valeur du rayon
                :param para2: si para1 vaut 0 on prend para2 sinon valeur par defaut 10
            """
            if para1!=0 and para2!=0:
                self.rayon = 10
                print ("paramètres incorrects :création d'un rond par défaut")
            else:
                if para1!=0 :
                    self.rayon= para1
                else :
                     self.rayon= para2

    def creer_triangle (self,para1,para2):
            """Fonction permetant la création d'un obstacle triangulaire
                :param para1: valeur de la base
                :param para2: valeur de la hauteur
                Si para1 et para2 valent 0, on prend 10 par défaut
            """
            if para1==0 or para2==0:
                self.base = self.hauteur = 10
                print ("paramètres incorrects :création d'un triangle par défaut")
            else :
                self.base=para1
                self.hauteur=para2

    def creer_rectangle(self,para1,para2):
            """Fonction permetant la création d'un obstacle carré
                :param para1: valeur de la longueur et de la largeur
                :param para2: si para1 vaut 0 on prend para2 sinon valeur par defaut 30
            """
            if para1==0 or para2==0:
                self.longueur=10
                self.largeur=20
                print ("paramètres incorrects :création d'un rectangle par défaut")
            else:
                self.longueur=para1
                self.largeur=para2

    def get_position(self):
        """Récupération de la position du centre
        :returns: position du centre tuplet
    """
        return self.x, self.y

    def get_forme(self):
        """Récupération de la forme
        :returns: position du centre
    """
        return self.forme
