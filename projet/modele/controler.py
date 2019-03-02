from interface.fenetre import*
import math as m

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
        f.z.vitesse=f.z.vitesse+1
    if touche =='Down':
        f.z.vitesse=f.z.vitesse-1
    if touche =='Left':
        f.p.changer_angle(m.pi/10)
        f.z.dessiner()
    if touche =='Right':
        f.p.changer_angle(-m.pi/10)
        f.z.dessiner()
