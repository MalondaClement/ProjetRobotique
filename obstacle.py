class Obstacle(object):
#""" Obstacle est une classe qui permet de créer des objets dans notre arène
#    :param x: position en x dans la matrice du centre de l'obstacle
#    :param y: position en y dans la matrice du centre de l'obstacle
#    :param forme: permet la gestion de la forme, 1 pour carré, 2 rond, 3 triangle
#    ...
#"""
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
        if para1!=0 and para2!=0:
            self.largeur = self. longueur = 30
            print ("paramètres incorrects :création d'un carré par défaut")
        else:
            if para1!=0 :
                self.longueur = self.largeur= para1
            else :
                self.longueur = self.largeur= para2
                
    def creer_rond (self,para1,para2):
            if para1!=0 and para2!=0:
                self.rayon = 10
                print ("paramètres incorrects :création d'un rond par défaut")
            else:
                if para1!=0 :
                    self.rayon= para1
                else :
                     self.rayon= para2
                     
    def creer_triangle (self,para1,para2):
            if para1==0 or para2==0:
                self.base = self.hauteur = 10
                print ("paramètres incorrects :création d'un triangle par défaut")
            else :
                self.base=para1
                self.hauteur=para2
                
    def creer_rectangle(self,para1,para2):
            if para1==0 or para2==0:
                self.longueur=10
                self.largeur=20
                print ("paramètres incorrects :création d'un rectangle par défaut")
            else:
                self.longueur=para1
                self.largeur=para2

    def get_position(self):
    #"""Récupération de la position du centre
    #    :returns: position du centre tuplet
    #"""
        return self.x, self.y

    def get_forme(self):
    #"""Récupération de la forme
    #    :returns: position du centre
    #"""
        return self.forme


"""#jeu de test

carre = Obstacle(10, 10, 1)
rond = Obstacle(20, 20, 2)
triangle = Obstacle(30, 30, 3)
inconnu = Obstacle(40, 40, 5)

print(carre.get_position())
print(rond.get_position())
print(triangle.get_position())
print(inconnu.get_position())

if carre.get_forme() == 1 :
    print("C'est un carre")
else :
    print("Il y a une erreur")

if rond.get_forme() == 2 :
    print("C'est un rond")
else :
    print("Il y a une erreur")

if triangle.get_forme() == 3 :
    print("C'est un triangle")
else :
    print("Il y a une erreur")

if inconnu.get_forme() == 1 :
    print("C'est un carre par defaut")
else :
    print("Il y a une erreur")"""

