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
main(ctrl)
