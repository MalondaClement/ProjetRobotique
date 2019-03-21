
class StratLigne(object):
    def __init__(self,distance,vitesse,robot):
        self.distance=distance
        self.vitesse=vitesse
        self.robot=robot

    def avancer (self, vitesse):
        self.robot.set_motor_dps(3, ((vitesse*360)/self.robot.WHEEL_BASE_CIRCUMFERENCE))

    def start(self):
        self.parcouru=0
        self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT, self.robot.get_motor_position()[0])
        self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT, self.robot.get_motor_position()[1])
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)


    def step(self):
        x,y=self.robot.get_motor_position()
        self.avancer(self.vitesse)
        self.parcouru=(x*self.robot.WHEEL_CIRCUMFERENCE)/360

    def stop(self):
        if self.parcouru>self.distance :
            self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT, self.robot.get_motor_position()[0])
            self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT, self.robot.get_motor_position()[1])
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
        return self.parcouru>self.distance
        

class StratAngleDroit(object):
    def __init__(self,robot):
        self.robot=robot
        self.distance=self.robot.WHEEL_BASE_CIRCUMFERENCE/4*360/self.robot.WHEEL_CIRCUMFERENCE

    def tourner (self, angle):
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT, -((self.robot.WHEEL_BASE_CIRCUMFERENCE)*(angle/360)*360)/self.robot.WHEEL_CIRCUMFERENCE)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, ((self.robot.WHEEL_BASE_CIRCUMFERENCE)*(angle/360)*360)/self.robot.WHEEL_CIRCUMFERENCE)

    def start(self):
        self.parcouru=0
        self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT, self.robot.get_motor_position()[0])
        self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT, self.robot.get_motor_position()[1])
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)

    def step(self):
        self.tourner(-90)
        x,y=self.robot.get_motor_position()
        self.parcouru=x

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
        self.cpt=0

    def get_distance(self) :
        return self.robot.get_distance()

    def step(self):
        if self.cpt>=4:
            self.sp=True
            return self.stop()

        elif self.ava:
            if not self.StratLigne.stop():
                self.StratLigne.step()
            else:
                self.ava=False
                self.StratAngleDroit.start()

        elif not self.ava:
            if not self.StratAngleDroit.stop():
                self.StratAngleDroit.step()
            else:
                self.ava=True
                self.cpt+=1
                self.StratLigne.start()

    def stop(self):
        return self.sp

class StratMur(object):
    #la distance entre la position initiale du robot et du mur ne depasse pas 8,000 millimetre
    def __init__(self,vitesse,robot):
        self.vitesse=vitesse
        self.robot=robot

    def avancer (self, vitesse):
        self.robot.set_motor_dps(3, ((vitesse*360)/self.robot.WHEEL_BASE_CIRCUMFERENCE))

    def start(self):
        self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT, self.robot.get_motor_position()[0])
        self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT, self.robot.get_motor_position()[1])
        print("Début start StratMur")

    def step(self):
        self.avancer(self.vitesse)
        print("getdistance")
        print(self.robot.get_distance())
        if self.stop():
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)

    def stop(self):
        return self.robot.get_distance()==8190

