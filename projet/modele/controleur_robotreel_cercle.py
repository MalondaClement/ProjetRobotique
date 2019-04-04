from .strategie import StratCercle
from threading import Thread
class ControleurRobotReelCercle(object):
    def __init__(self,robot, rayon,temps, direction, cercle):
        super(ControleurRobotReelCercle,self).__init__()
        self.StratCercle=StratCercle(robot,rayon,temps,direction,cercle)
        self.sp = False

    def start(self):
        self.StratCercle.start()

    def update(self) :
        if not self.StratCercle.stop():
            self.StratCercle.step()
        else:
            self.sp=True
            return self.stop

    def stop(self):
        return self.sp


