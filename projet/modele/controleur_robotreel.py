from .strategie import StratLigne,StratAngleDroit, StratCarre
from threading import Thread
class ControleurRobotReel(Thread):
    def __init__(self,robot):
        super(ControleurRobotReel,self).__init__()
        self.robot=robot
        self.StratLigne=StratLigne(1000,1000,self.robot)
        self.StratAngleDroit=StratAngleDroit(self.robot)
        self.StratLigne.start()
        self.StratAngleDroit.start()
        self.sp=False
        self.ava=True
        self.tour=False
        self.cpt=0

    def init(self):
        self.start()

    def run(self):
        while not self.stop():
            self.update()
            time.sleep(1./50)
        print("stop")

    def get_distance(self) :
        return self.robot.get_distance()

    def update(self):
        '''if StratCarre(self.robot, 1000, 1000):
            self.sp = True
            return self.stop()'''
        if self.cpt==4:
            self.sp=True
            return self.stop()

        elif self.ava:
            if self.StratLigne.step()==False:
                self.ava=False
                self.tour=True

        elif self.tour:
            if self.StratAngleDroit.step()==False:
                self.ava=True
                self.tour=False
                self.cpt+=1
        '''if self.StratAngleDroit.step()==False:
            self.sp=True
            return self.stop()'''




    def stop(self):
        return self.sp
