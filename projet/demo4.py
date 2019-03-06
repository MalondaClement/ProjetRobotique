import time
try:
    from robot2I013 import Robot2I013 as Robot
    robot = Robot()
    
except ImportError:
    from interface.fenetre import Fenetre
    from modele.robotreel import RobotReel as Robot
    from modele.controleur_robotreel import ControleurRobotReel
    f=Fenetre()
    f.creer()

ctrl=ControleurRobotReel(robot)
def main(ctrl):
    while not ctrl.stop():
        ctrl.update()
        time.sleep(0.20)
    
"""def main(z,p,f,c):
    p.actualiser()
    z.dessiner()
    if (z.avancer ==1) :
        if (p.MOTOR_LEFT_ROTATION < 5000*360/p.WHEEL_CIRCUMFERENCE) :
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

while not hasattr(f, 'z'):
    pass
c=ControleurRobotReel(f.p)
main(f.z,f.p,f,c) """   		
