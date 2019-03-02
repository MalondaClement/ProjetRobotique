import math as m
from interface.fenetre import*
from modele.robotreel import RobotReel
from modele.controleur_robotreel import ControleurRobotReel

avancer =1
tourner =0

def main(o,z,p,fenetre):
    c=ControleurRobotReel(p)
    p.actualiser()
    z.dessiner()
    z.zone_dessin.create_rectangle(p.x,p.y,p.x+1,p.y+1,fill='green')
    if (z.avancer ==1) :
        if (p.MOTOR_LEFT_ROTATION < 5000*360/p.WHEEL_CIRCUMFERENCE) :
            print(p.MOTOR_LEFT_ROTATION)
            c.avancer(1000)

        else :
            p.stop()
            z.avancer =0
            z.tourner =1
            p.offset_motor_encoder(3, 0)
    elif (z.tourner ==1) :
    	if (p.MOTOR_LEFT_ROTATION < p.WHEEL_BASE_CIRCUMFERENCE/4 *360/p.WHEEL_CIRCUMFERENCE ) :
    		c.tourner(-45)
    	else :
    		p.stop()
    		z.avancer =1
    		z.tourner =0
    		p.offset_motor_encoder(3, 0)


