from .strategie import StratLigne,StratAngle,StratPolygone
from threading import Thread
class ControleurRobotReelPolygone(Thread):
    def __init__(self,robot):
        super(ControleurRobotReelPolygone,self).__init__()
        self.robot=robot
        self.Strat = StratPolygone(self.robot, 600, 8) # on demande 8 ou 20 dans la question
        self.sp=False

    def init(self):
        self.start()

    def get_distance(self) :
        return self.robot.get_distance()

    def update(self):
        if not self.Strat.stop():
            self.Strat.step()
        else:
            self.sp=True
            return self.stop

    def stop(self):
        return self.sp
