import time
from modele.controleur_robotreel_cercle import ControleurRobotReelCercle

try:
    from robot2I013 import Robot2I013 as Robot
    robot = Robot()
    ctrl=ControleurRobotReelCercle(robot, 100, 5, 0, 50)
    def main(ctrl):
        while not ctrl.stop():
            ctrl.update()
            time.sleep(0.01)
    robot.offset_motor_encoder(robot.MOTOR_LEFT, robot.get_motor_position()[0])
    robot.offset_motor_encoder(robot.MOTOR_RIGHT, robot.get_motor_position()[1])
    #robot.set_motor_dps(robot.MOTOR_LEFT+robot.MOTOR_RIGHT,0)
    main(ctrl)

except ImportError:
    menu = 0
    print("Cette demo peut se lancer dans le simulateur 2D et 3D")
    print("Pour la lancer en 2D saisir 2D pour la lancer en 3D saisir 3D")
    menu = input()
    from modele.robotreel import RobotReel as Robot
    if menu == "2D" or menu == "2":
        from interface.fenetre import Fenetre
        f=Fenetre(2)
        f.creer()
    elif menu == "3D" or menu == "3":
        from interface3d.affichage3d import *
        from interface3d.fenetre3d import *
        from modele.arene import Arene
        from modele.obstacle import Obstacle
        import math as m
        import pyglet
        WINDOW = 600
        win = Window(WINDOW, WINDOW, 'Cube')
        ar=Arene(500,500)
        ob=ObstacleRectangle(70,50,10,10)
        ob1=ObstacleRectangle(100,100,40,50)
        ar.inserer_obs(ob)
        ar.inserer_obs(ob1)
        rob=RobotReel(70,400,m.pi/2,ar)
        aff = Affichage(win,ar,rob,0)
        aff.start()
        aff.on_resize(600,600)
        aff.on_draw()
        aff.recherche_balise()
        pyglet.clock.schedule_interval(aff.update, 0.1)
        pyglet.app.run()
    else :
        print("Erreur pas d'entrée dans le menu")

