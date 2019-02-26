import math as m
from fenetre import* 


def main(o,z,p,fenetre):
    if p.distancemax(z.arene):
        p.changer_angle(m.pi/7)
    p.avancer(z.vitesse)
    z.dessiner()
    #fenetre.after(50,main(o,z,p,fenetre))
