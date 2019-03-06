from .strategie import StratLigne,StratAngleDroit

class ControleurRobotReel(object):
    def __init__(self,robot):
        self.robot=robot
        self.StratLigne=StratLigne(1000,1000,self.robot)
        self.StratAngleDroit=StratAngleDroit(self.robot)
        self.StratLigne.start()
        self.StratAngleDroit.start()
        self.sp=False
        self.ava=True
        self.tour=False
        self.cpt=0
        
    def update(self):
        print(self.cpt)
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
        
                
            
        
    def stop(self):
        return self.sp
