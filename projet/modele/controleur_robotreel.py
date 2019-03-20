from .strategie import StratLigne,StratAngleDroit, StratCarre

class ControleurRobotReel(object):
    def __init__(self,robot):
        self.robot=robot
        self.StratCarre=StratCarre(self.robot,1000,1000)
        self.sp=False

    def get_distance(self) :
        return self.robot.get_distance()

    def update(self):
        if self.StratCarre.step():
            self.sp=True
            return self.stop

    def stop(self):
        return self.sp
