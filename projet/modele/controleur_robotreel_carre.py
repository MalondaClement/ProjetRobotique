from .strategie import StratLigne,StratAngleDroit, StratCarre
from threading import Thread
class ControleurRobotReelCarre(Thread):
    def __init__(self,robot):
        super(ControleurRobotReelCarre,self).__init__()
        self.robot=robot
        self.StratLigne=StratLigne(500, 600, self.robot)
        self.StratCarre=StratCarre(self.robot,250,500)
        self.sp=False

    def init(self):
        self.start()

    def get_distance(self) :
        return self.robot.get_distance()

    def update(self):
        if self.StratCarre.step():
            self.sp=True
            return self.stop

    def stop(self):
        return self.sp
