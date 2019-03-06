from .strategie import StratLigne

class ControleurRobotReel(object):
    def __init__(self,robot):
        self.robot=robot
        self.sp=False
        self.StratLigne=StratLigne(1000,1000,self.robot)
        self.StratLigne.start()
        
        
    def update(self):
        if self.StratLigne.step()==False:
            self.sp=True
        
    def stop(self):
        return self.sp
