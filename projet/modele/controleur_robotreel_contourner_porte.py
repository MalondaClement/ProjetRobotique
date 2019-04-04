from .strategie import StratContournerPorte
from threading import Thread
class ControleurRobotReelContournerPorte(Thread):
    def __init__(self,robot):
        super(ControleurRobotReelContournerPorte,self).__init__()
        self.robot=robot
        self.StratContournerPorte = StratContournerPorte(self.robot, 500)
        self.sp=False

    def init(self):
        self.start()

    def get_distance(self) :
        return self.robot.get_distance()

    def update(self):
        if self.StratContournerPorte.step():
            self.sp=True
            return self.stop

    def stop(self):
        return self.sp
