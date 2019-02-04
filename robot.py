class Robot(object):
	def __init__(self,x,y,angle):
		self.x=x
		self.y=y
		self.angle=angle
		self.couleur=0 #noir en binaire
		self.largeur=20
		self.longueur=50

	def get_position(self):
		return self.x, self.y


def changement_angle(robot, angle):
    if angle > 0:
        angle = angle%360
    else :
        angle = angle%(-360)
        
    robot.angle += angle


