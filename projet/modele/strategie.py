'''
class Traducteur:
	def __init__(self, robot) :
		self.robot = robot


	def avancer (self, vitesse) :
		# attention : vitesse en mm/s
		self.robot.set_motor_dps(3, ((vitesse*360)/self.robot.WHEEL_BASE_CIRCUMFERENCE))

	def tourner (self, angle) :
		#attention: angle est une vitesse angulaire en degré par seconde, un angle positif fait tourner dans le sens trigonométrique
		self.robot.set_motor_dps(1, -((self.robot.WHEEL_BASE_CIRCUMFERENCE)*(angle/360)*360)/self.robot.WHEEL_CIRCUMFERENCE)
		self.robot.set_motor_dps(2, ((self.robot.WHEEL_BASE_CIRCUMFERENCE)*(angle/360)*360)/self.robot.WHEEL_CIRCUMFERENCE)'''

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
        self.tourner(-45)

    def stop(self):
        return self.parcouru>=self.distance

class StratCarre(object):
    def __init__(self,robot,vitesse,longueurCarre):
        stratTourner = StratAngleDroit(robot)
        stratAvancer = StratLigne(longueurCarre,vitesse,robot)
        self.strategies = [stratAvancer,stratTourner,stratAvancer,stratTourner,stratAvancer,stratTourner,stratAvancer]


    def start(self):
        self.cur = 0

    def step(self):
        if self.stop():
            return
        if self.cur < 0 or self.strategies[self.cur].stop():
            self.cur+=1
            self.strategies[self.cur].start()
            self.strategies[self.cur].step()

    def stop (self):
        return self.cur == len(self.strategies)-1 and self.strategies[self.cur].stop()
