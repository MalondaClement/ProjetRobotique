
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





def clavier(event):
    """Cette fonction reçoit les touches appuyé par l'utilisateur et effectue des actions pour certaines d'entre elles.
        :param event: flèche recu
            -Touche Up permet d'augmenter la vitesse
            -Touche Down permet baisser la vitesse
            -Touche Right permet de faire tourner le robot a droite
            -Touche Left permet de faire tourner le robot a gauche
    """
	#touche=event.keysym
    return

    #j'ai repris le fonction clavier de controler sans modifier son architecture


