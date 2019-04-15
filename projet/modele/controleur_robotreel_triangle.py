from .strategie import StratLigne,StratAngle,StratCarre,StratTriangle
from threading import Thread
class ControleurRobotReelTriangle(Thread):
    def __init__(self,robot):
        super(ControleurRobotReelTriangle,self).__init__()
        self.robot=robot
        self.StratTriangle=StratTriangle(self.robot,250,1000)
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
