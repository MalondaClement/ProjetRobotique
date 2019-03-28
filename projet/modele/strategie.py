
class StratLigne(object):
    def __init__(self,distance,vitesse,robot):
        self.distance=distance
        self.vitesse=vitesse
        self.robot=robot
        self.ralenti=False

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
        if self.parcouru >= self.distance*(3/4) and self.ralenti==False :
            self.ralenti=True
            self.vitesse=self.vitesse/2

    def stop(self):
        if self.parcouru>self.distance :
            self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT, self.robot.get_motor_position()[0])
            self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT, self.robot.get_motor_position()[1])
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
        return self.parcouru>self.distance


class StratAngleDroit(object):
    def __init__(self,robot):
        self.robot=robot
        self.angle=-90
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
        self.tourner(self.angle)
        x,y=self.robot.get_motor_position()
        self.parcouru=x
        if self.parcouru >= self.distance*(3/4) :
            self.angle = self.angle/5

    def stop(self):
        return self.parcouru>=self.distance

class StratCarre(object):
    def __init__(self,robot,vitesse,longueurCarre):
        self.robot=robot
        self.vitesse=vitesse
        self.longueurCarre=longueurCarre
        s0=StratLigne(self.longueurCarre,self.vitesse,self.robot)
        s1=StratAngleDroit(self.robot)
        s2=StratLigne(self.longueurCarre,self.vitesse,self.robot)
        s3=StratAngleDroit(self.robot)
        s4=StratLigne(self.longueurCarre,self.vitesse,self.robot)
        s5=StratAngleDroit(self.robot)
        s6=StratLigne(self.longueurCarre,self.vitesse,self.robot)

        self.strats = [s0, s1, s2, s3, s4, s5, s6]
        self.cur =-1

    def get_distance(self) :
        return self.robot.get_distance()

    def step(self):
        if self.stop() :return
        if self.cur < 0 or self.strats[self.cur].stop():
            self.cur+=1
            self.strats[self.cur].start()
        self.strats[self.cur].step()

    def stop(self) :
        return self.cur==len(self.strats)-1 and self.strats[self.cur].stop()

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
        #print("Début start StratMur")

    def step(self):
        if self.stop():
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
        else :
            self.avancer(self.vitesse)
            #print("getdistance")
            #print(self.robot.get_distance())


    def stop(self):
        distance_mur = self.robot.get_distance()
        if distance_mur<=50 or distance_mur == 8190:
            self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT, self.robot.get_motor_position()[0])
            self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT, self.robot.get_motor_position()[1])
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
            return True
        else:
            return False

