from .strategie import StratLigne,StratAngle,StratCarre,StratTriangle
from threading import Thread
class ControleurRobotReelTriangle(Thread):
    def __init__(self,robot):
        super(ControleurRobotReelTriangle,self).__init__()
        self.robot=robot
        self.StratTriangle=StratTriangle(self.robot,250,1000) #ici on ne verra pas le triangle quasiment si on met 100mm car notre arene fait 5m par 5m si on veut voir il faut mettre 1000
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
