import time

try:
    from robot2I013 import Robot2I013 as Robot
    robot = Robot()
    robot.set_motor_dps(robot.MOTOR_LEFT+robot.MOTOR_RIGHT,0)
    robot.offset_motor_encoder(robot.MOTOR_LEFT, robot.get_motor_position()[0])
    robot.offset_motor_encoder(robot.MOTOR_RIGHT, robot.get_motor_position()[1])
    robot.servo_rotate(30)

except ImportError:
    print("Pas une demo")
