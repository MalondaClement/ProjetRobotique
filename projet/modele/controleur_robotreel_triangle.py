from .strategie import StratLigne,StratAngle,StratTriangle
from threading import Thread
import time
class ControleurRobotReelTriangle(Thread):
    def __init__(self,robot):
        super(ControleurRobotReelTriangle,self).__init__()
        self.robot=robot
        self.StratLigne=StratLigne(self.robot, 600, 500)
        self.StratTriangle=StratTriangle(self.robot,250,500)
        self.sp=False

    def init(self):
        self.start()

    def get_distance(self) :
        return self.robot.get_distance()

    def update(self):
        if not self.StratTriangle.stop():
            self.StratTriangle.step()
        else:
            self.sp=True
            return self.stop

    def stop(self):
        return self.sp
    def run(self):
        while not self.ctrl.stop():
              self.ctrl.update()
              time.sleep(1./20)
