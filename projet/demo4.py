import time
from modele.controleur_robotreel import ControleurRobotReel

try:
    print("try")
    from robot2I013 import Robot2I013 as Robot
    robot = Robot()
    print("try ok")
except ImportError:
    print("execpt")
    from interface.fenetre import Fenetre
    from modele.robotreel import RobotReel as Robot
    from modele.controleur_robotreel import ControleurRobotReel
    f=Fenetre()
    f.creer()

ctrl=ControleurRobotReel(robot)
def main(ctrl):
    while not ctrl.stop():
        ctrl.update()
        time.sleep(0.01)
robot.offset_motor_encoder(robot.MOTOR_LEFT, robot.get_motor_position()[0])
robot.offset_motor_encoder(robot.MOTOR_RIGHT, robot.get_motor_position()[1])
#robot.set_motor_dps(robot.MOTOR_LEFT+robot.MOTOR_RIGHT,0)
main(ctrl)
