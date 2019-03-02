class Controleur(object):
    """docstring for Controleur"""
    def __init__(self):
        pass

def clavier(event):
    """Cette fonction reçoit les touches appuyé par l'utilisateur et effectue des actions pour certaines d'entre elles.
        :param event: flèche recu
            -Touche Up permet d'augmenter la vitesse
            -Touche Down permet baisser la vitesse
            -Touche Right permet de faire tourner le robot a droite
            -Touche Left permet de faire tourner le robot a gauche
    """
    touche=event.keysym
    print(touche)
    if touche =='Up':
        z.vitesse=z.vitesse+1
    if touche =='Down':
        z.vitesse=z.vitesse-1
    if touche =='Left':
        p.changer_angle(m.pi/10)
        dessiner()
    if touche =='Right':
        p.changer_angle(-m.pi/10)
        dessiner()
