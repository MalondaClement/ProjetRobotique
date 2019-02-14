class Obstacle(object):
#""" Obstacle est une classe qui permet de créer des objets dans notre arène
#    :param x: position en x dans la matrice du centre de l'obstacle
#    :param y: position en y dans la matrice du centre de l'obstacle
#    :param forme: permet la gestion de la forme, 1 pour carré, 2 rond, 3 triangle
#    ...
#"""
    def __init__(self, x, y, forme):
        self.x = x
        self.y = y
        self.forme = forme
        if self.forme == 1 : #carre
            self.largeur = self. longueur = 30
        elif self.forme == 2 : #rond
            self.rayon = 10
        elif self.forme == 3 : #triangle
            self.base = self.hauteur = 10
        else :
            self.forme = 1
            self.largeur = self. longueur = 10

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

