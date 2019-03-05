
class ControleurRobotReel (object) :
	def __init__(self, robot) :
		self.robot = robot


	def avancer (self, vitesse) :
		# attention : vitesse en mm/s
		self.robot.set_motor_dps(3, ((vitesse*360)/self.robot.WHEEL_BASE_CIRCUMFERENCE))

	def tourner (self, angle) :
		#attention: angle est une vitesse angulaire en degré par seconde, un angle positif fait tourner dans le sens trigonométrique
		self.robot.set_motor_dps(1, -((self.robot.WHEEL_BASE_CIRCUMFERENCE)*(angle/360)*360)/self.robot.WHEEL_CIRCUMFERENCE)
		self.robot.set_motor_dps(2, ((self.robot.WHEEL_BASE_CIRCUMFERENCE)*(angle/360)*360)/self.robot.WHEEL_CIRCUMFERENCE)
		
	def get_distance(self):
		return self.robot.get_distance()
	
