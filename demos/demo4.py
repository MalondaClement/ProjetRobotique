
arret=False
def main():
    global arret
    if arret==False:
        if p.distancemax(z.arene):
            p.changer_angle(m.pi/7)
        p.avancer(z.vitesse)
        dessiner()
        fenetre.after(50,main)
