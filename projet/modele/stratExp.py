class StratExperimentale(object):
    def __init__(self,distance,vitesse,robot):
        self.distance = distance
        self.vitesse = vitesse
        self.robot = robot

    def tournerUneRoue(self, angle, roue):
        if roue == 1:
            self.robot.set_motor_dps(1, ((self.robot.WHEEL_BASE_CIRCUMFERENCE)*(angle/360)*360)/self.self.robot.WHEEL_CIRCUMFERENCE)
            self.robot.set_motor_dps(2, 0)
        elif roue == 2:
            self.robot.set_motor_dps(1, 0)
            self.robot.set_motor_dps(2, ((self.robot.WHEEL_BASE_CIRCUMFERENCE)*(angle/360)*360)/self.robot.WHEEL_CIRCUMFERENCE)

    def avancerVitesseDif(self, vitesse, facteur):
        v = ((vitesse*360)/self.robot.WHEEL_BASE_CIRCUMFERENCE)
        self.robot.set_motor_dps(1,v)
        self.robot.set_motor_dps(2,v/facteur)
