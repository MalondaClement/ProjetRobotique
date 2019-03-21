from .strategie import StratLigne,StratAngleDroit, StratCarre,StratMur
from threading import Thread
class ControleurRobotReel(Thread):

    def __init__(self,robot):
        super(ControleurRobotReel,self).__init__()
        self.robot=robot
        self.StratMur=StratMur(1000,self.robot)
        self.sp=False
        self.start()

    def start(self):
        self.StratMur.start()

    def get_distance(self) :
        return self.robot.get_distance()

    def update(self):
        if not self.StratMur.stop():
            self.StratMur.step()
        else:
            self.sp=True
            return self.stop

    def stop(self):
        return self.sp
