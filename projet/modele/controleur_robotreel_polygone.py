from .strategie import StratLigne,StratAngle,StratTriangle,StratPolygone
from threading import Thread
import time
class ControleurRobotReelPolygone(Thread):
    def __init__(self,robot):
        super(ControleurRobotReelPolygone,self).__init__()
        self.robot=robot
        self.StratLigne=StratLigne(self.robot, 600, 500)
        self.StratPolygone=StratPolygone(self.robot,250,500,8)
        #self.StratPolygone=StratPolygone(self.robot,250,500,20)
        self.sp=False

    def init(self):
        self.start()

    def get_distance(self) :
        return self.robot.get_distance()

    def update(self):
        if not self.StratPolygone.stop():
            self.StratPolygone.step()
        else:
            self.sp=True
            return self.stop

    def stop(self):
        return self.sp
    def run(self):
        while not self.ctrl.stop():
              self.ctrl.update()
              time.sleep(1./20)
