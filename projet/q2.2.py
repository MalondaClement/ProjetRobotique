#script qui est utiliser pour faire le polygone de la question 2.2
#modification également dans stratégie  avec la nouvelle class StratPolygone et ajout d'un fichier controleur_robotreel_polygone.py
import time
from modele.controleur_robotreel_polygone import ControleurRobotReelPolygone

try:
    from robot2I013 import Robot2I013 as Robot
    robot = Robot()
    ctrl=ControleurRobotReelPolygone(robot)
    def main(ctrl):
        while not ctrl.stop():
            print(robot.get_distance())
            ctrl.update()
            time.sleep(0.01)
    robot.offset_motor_encoder(robot.MOTOR_LEFT, robot.get_motor_position()[0])
    robot.offset_motor_encoder(robot.MOTOR_RIGHT, robot.get_motor_position()[1])
    main(ctrl)

except ImportError:
    from interface.fenetre import Fenetre
    from modele.robotreel import RobotReel as Robot
    f=Fenetre(5)
    f.creer()
