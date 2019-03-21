
class StratLigne(object):
    def __init__(self,distance,vitesse,robot):
        self.distance=distance
        self.vitesse=vitesse
        self.robot=robot

    def avancer (self, vitesse):
        self.robot.set_motor_dps(3, ((vitesse*360)/self.robot.WHEEL_BASE_CIRCUMFERENCE))

    def start(self):
        self.parcouru=0

    def step(self):
        x,y=self.robot.get_motor_position()
        print(x,y)
        self.parcouru=(x*self.robot.WHEEL_CIRCUMFERENCE)/360
        if self.stop():
            self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT, self.robot.get_motor_position()[0])
            self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT, self.robot.get_motor_position()[1])
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
            return False
        self.avancer(self.vitesse)

    def stop(self):
        return self.parcouru>self.distance

class StratAngleDroit(object):
    def __init__(self,robot):
        self.robot=robot
        self.distance=self.robot.WHEEL_BASE_CIRCUMFERENCE/4*360/self.robot.WHEEL_CIRCUMFERENCE
        print(self.distance)

    def tourner (self, angle):
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT, -((self.robot.WHEEL_BASE_CIRCUMFERENCE)*(angle/360)*360)/self.robot.WHEEL_CIRCUMFERENCE)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, ((self.robot.WHEEL_BASE_CIRCUMFERENCE)*(angle/360)*360)/self.robot.WHEEL_CIRCUMFERENCE)

    def start(self):
        self.parcouru=0

    def step(self):
        x,y=self.robot.get_motor_position()
        self.parcouru=x
        if self.stop():
            self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT, self.robot.get_motor_position()[0])
            self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT, self.robot.get_motor_position()[1])
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
            print(self.parcouru)
            return False
        self.tourner(-90)

    def stop(self):
        return self.parcouru>=self.distance

class StratCarre(object):
    def __init__(self,robot,vitesse,longueurCarre):
        self.robot=robot
        self.vitesse=vitesse
        self.longueurCarre=longueurCarre
        self.StratLigne=StratLigne(self.longueurCarre,self.vitesse,self.robot)
        self.StratAngleDroit=StratAngleDroit(self.robot)
        self.StratLigne.start()
        self.StratAngleDroit.start()
        self.sp=False
        self.ava=True
        self.tour=False
        self.cpt=0

    def get_distance(self) :
        return self.robot.get_distance()

    def step(self):
        if self.cpt==4:
            self.sp=True
            return self.stop()

        elif self.ava:
            if self.StratLigne.step()==False:
                self.ava=False
                self.tour=True

        elif self.tour:
            print('oui')
            if self.StratAngleDroit.step()==False:
                self.ava=True
                self.tour=False
                self.cpt+=1

    def stop(self):
        return self.sp
