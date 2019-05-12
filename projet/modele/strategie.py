from math import fabs, pi
class StratLigne(object):
    def __init__(self,robot,vitesse,distance):
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

class StratAngle(object):
    def __init__(self,robot, angle=-90):
        self.robot=robot
        self.test=True
        self.v_angu=-90
        self.angle=angle
        self.distance=self.robot.WHEEL_BASE_CIRCUMFERENCE/fabs((360/self.angle))*360/self.robot.WHEEL_CIRCUMFERENCE

    def tourner (self, v_angu):
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT, -((self.robot.WHEEL_BASE_CIRCUMFERENCE)*(v_angu/360)*360)/self.robot.WHEEL_CIRCUMFERENCE)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, ((self.robot.WHEEL_BASE_CIRCUMFERENCE)*(v_angu/360)*360)/self.robot.WHEEL_CIRCUMFERENCE)

    def start(self):
        self.parcouru=0
        self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT, self.robot.get_motor_position()[0])
        self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT, self.robot.get_motor_position()[1])
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)

    def step(self):
        self.tourner(self.v_angu)
        x,y=self.robot.get_motor_position()
        self.parcouru=x
        if self.parcouru >= self.distance*(3/4) and self.test :
            self.v_angu = self.v_angu/5
            self.test=False

    def stop(self):
        if self.parcouru >=self.distance :
            self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT, self.robot.get_motor_position()[0])
            self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT, self.robot.get_motor_position()[1])
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
        return self.parcouru>=self.distance

class StratCarre(object):
    def __init__(self,robot,vitesse,longueurCarre):
        self.robot=robot
        self.vitesse=vitesse
        self.longueurCarre=longueurCarre
        s0=StratLigne(self.robot, self.vitesse, self.longueurCarre)
        s1=StratAngle(self.robot)
        s2=StratLigne(self.robot, self.vitesse, self.longueurCarre)
        s3=StratAngle(self.robot)
        s4=StratLigne(self.robot, self.vitesse, self.longueurCarre)
        s5=StratAngle(self.robot)
        s6=StratLigne(self.robot, self.vitesse, self.longueurCarre)

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
    def __init__(self,robot,vitesse,distance=50):
        self.vitesse=vitesse
        self.robot=robot
        self.distance=distance

    def avancer (self, vitesse):
        self.robot.set_motor_dps(3, ((vitesse*360)/self.robot.WHEEL_BASE_CIRCUMFERENCE))

    def start(self):
        self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT, self.robot.get_motor_position()[0])
        self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT, self.robot.get_motor_position()[1])
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)

    def step(self):
        if self.stop():
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
        else :
            self.avancer(self.vitesse)

    def stop(self):
        distance_mur = self.robot.get_distance()
        print(distance_mur)
        if distance_mur<=self.distance or distance_mur == 8190:
            self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT, self.robot.get_motor_position()[0])
            self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT, self.robot.get_motor_position()[1])
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
            return True
        else:
            return False

class StratCercle(object):
   def __init__(self, robot, rayon, temps, direction, cercle) :
       self.robot=robot
       self.rayon=rayon
       self.temps=temps
       self.direction=direction
       self.cercle=cercle
       self.distance= (2*pi*rayon)*(cercle/100)*(360/self.robot.WHEEL_CIRCUMFERENCE)

   def start(self):
       self.parcouru=0
       self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT, self.robot.get_motor_position()[0])
       self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT, self.robot.get_motor_position()[1])
       self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)

   def step(self):
        #print(self.distance)
        if self.direction=="gauche" :
            self.robot.set_motor_dps(1, ((((2*pi*(self.rayon+self.robot.WHEEL_BASE_WIDTH))/(self.temps*(self.cercle/100)))*360)/self.robot.WHEEL_BASE_CIRCUMFERENCE))
            self.robot.set_motor_dps(2, ((((2*pi*self.rayon/(self.temps*(self.cercle/100)))*360)/self.robot.WHEEL_BASE_CIRCUMFERENCE)))
        elif self.direction=="droite" :
            self.robot.set_motor_dps(2, ((((2*pi*(self.rayon+self.robot.WHEEL_BASE_WIDTH))/(self.temps*(self.cercle/100)))*360)/self.robot.WHEEL_BASE_CIRCUMFERENCE))
            self.robot.set_motor_dps(1, ((((2*pi*self.rayon/(self.temps*(self.cercle/100)))*360)/self.robot.WHEEL_BASE_CIRCUMFERENCE)))


   def stop(self) :
        if self.direction=="gauche" :
            motor_vit=self.robot.get_motor_position()[1]
            if self.distance < self.robot.get_motor_position()[1]:
                self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT, self.robot.get_motor_position()[0])
                self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT, self.robot.get_motor_position()[1])
                self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
                print("strat terminee")
            return self.distance < motor_vit

        else :
            motor_vit=self.robot.get_motor_position()[0]
            if self.distance < self.robot.get_motor_position()[0]:
                self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT, self.robot.get_motor_position()[0])
                self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT, self.robot.get_motor_position()[1])
                self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
                print("strat terminee")
            return self.distance < motor_vit

class StratContournerPorte(object):
    def __init__(self,robot,vitesse):
        self.robot = robot
        self.vitesse = vitesse
        s0 = StratMur(self.robot, self.vitesse, 70)
        s1 = StratDetectePorte(self.robot)
        s2 = StratAngle(self.robot)
        #s2 = StratMur(self.robot, self.vitesse)
        self.strats = [s0, s1, s2]
        self.cur = -1

    def step(self):
        if self.stop() :
            return
        if self.cur < 0 or self.strats[self.cur].stop():
            self.cur+=1
            self.strats[self.cur].start()
        self.strats[self.cur].step()
        print(self.cur)

    def stop(self) :
        return self.cur==len(self.strats)-1 and self.strats[self.cur].stop()

class StratDetectePorte(object):
    def __init__(self, robot):
        self.robot = robot
        self.fin = False

    def start(self):
        self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT, self.robot.get_motor_position()[0])
        self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT, self.robot.get_motor_position()[1])
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)

    def step(self):
        if self.stop():
            return min(d_gauche, d_droite)
        else:
            self.robot.servo_rotate(1)
            d_gauche = self.robot.get_distance()
            print(d_gauche)
            self.robot.servo_rotate(179)
            d_droite = self.robot.get_distance()
            print(d_droite)
            self.robot.servo_rotate(90)
            self.fin = True
            print(self.fin)

    def stop(self):
        return self.fin
    def stop(self):
        return self.fin
