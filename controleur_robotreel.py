class ControleurRobotReel (object) :
	def __init__(self, robot) :
		self.robot = robot


	def avancer (self, vitesse) :
		# attention : vitesse en mm/s
		robot.set_motor_dps(3, ((vitesse*360)/robot.WHEEL_CIRCUMFERENCE))

	def tourner (self, angle) :
		#attention: angle est une vitesse angulaire en degré par seconde, un angle positif fait tourner dans le sens trigonométrique
		robot.set_motor_dps(1, -((robot.WHEEL_BASE_CIRCUMFERENCE)/(360/angle)*360)/robot.WHEEL_CIRCUMFERENCE)
		robot.set_motor_dps(2, ((robot.WHEEL_BASE_CIRCUMFERENCE)/(360/angle)*360)/robot.WHEEL_CIRCUMFERENCE)





def clavier(event):
    """Cette fonction reçoit les touches appuyé par l'utilisateur et effectue des actions pour certaines d'entre elles.
        :param event: flèche recu
            -Touche Up permet d'augmenter la vitesse
            -Touche Down permet baisser la vitesse
            -Touche Right permet de faire tourner le robot a droite
            -Touche Left permet de faire tourner le robot a gauche
    """
	touche=event.keysym
	print(touche)
	if touche =='Up':
	    avancer(10)
	if touche =='Down':
    	avancer(-10)
	if touche =='Left':
    	tourner(90)
    	dessiner()
	if touche =='Right':
    	tourner(-90)
        	dessiner()

    #j'ai repris le fonction clavier de controler sans modifier son architecture


