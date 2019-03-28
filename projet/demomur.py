import time
from modele.controleur_robotreel_mur import ControleurRobotReelMur

try:
    from robot2I013 import Robot2I013 as Robot
    robot = Robot()
except ImportError:
    from interface.fenetre import Fenetre
    from modele.robotreel import RobotReel as Robot
    f=Fenetre(1)
    f.creer()

ctrl=ControleurRobotReelMur(robot)
def main(ctrl):
    while not ctrl.stop():
        print(robot.get_distance())
        ctrl.update()
        time.sleep(0.01)
robot.offset_motor_encoder(robot.MOTOR_LEFT, robot.get_motor_position()[0])
robot.offset_motor_encoder(robot.MOTOR_RIGHT, robot.get_motor_position()[1])
#robot.set_motor_dps(robot.MOTOR_LEFT+robot.MOTOR_RIGHT,0)
main(ctrl)
# robot.servo_rotate(0)
# robot.servo_rotate(180)
# robot.servo_rotate(90)
