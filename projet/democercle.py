import time
from modele.controleur_robotreel_cercle import ControleurRobotReelCercle

try:
    from robot2I013 import Robot2I013 as Robot
    robot = Robot()
except ImportError:
    from interface.fenetre import Fenetre
    from modele.robotreel import RobotReel as Robot
    f=Fenetre(0)
    f.creer()

ctrl=ControleurRobotReelCercle(robot, 500, 5, 0, 75)
def main(ctrl):
    while not ctrl.stop(): 
        ctrl.update()
        time.sleep(0.01)
robot.offset_motor_encoder(robot.MOTOR_LEFT, robot.get_motor_position()[0])
robot.offset_motor_encoder(robot.MOTOR_RIGHT, robot.get_motor_position()[1])
#robot.set_motor_dps(robot.MOTOR_LEFT+robot.MOTOR_RIGHT,0)
main(ctrl)
