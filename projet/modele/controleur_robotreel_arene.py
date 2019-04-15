from .strategie import StratArene
from threading import Thread
class ControleurRobotReelArene(Thread):
    def __init__(self,robot):
        super(ControleurRobotReelArene,self).__init__()
        self.robot=robot
        self.strategie = StratArene(self.robot, 500, 50)
        self.sp=False

    def init(self):
        self.start()

    def get_distance(self) :
        return self.robot.get_distance()

    def update(self):
        if not self.strategie.stop():
            self.strategie.step()
        else:
            self.sp=True
            return self.stop

    def stop(self):
        return self.sp
