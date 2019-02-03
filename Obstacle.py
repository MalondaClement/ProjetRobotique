class Obstacle(object):
    def __init__(self, x, y, forme):
        self.x = y
        self.y = y
        self.forme = forme
        if self.forme == 1 : #carre
            self.largeur = self. longueur = 10
        elif self.forme == 2 : #rond
            self.rayon = 10
        elif self.forme == 3 : #triangle
            self.base = self.hauteur = 10
        else :
            self.forme = 1
            self.largeur = self. longueur = 10

    def get_position(self):
        return self.x, self.y

    def get_forme(self):
        return self.forme


#jeu de test

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
    print("C'est un carre par défaut")
else :
    print("Il y a une erreur")

