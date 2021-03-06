import time

menu_demo = 0
print("Veuillez entrer le type de simulation a lancer \n0 : carre \n1 : arret avant un mur\n2 : cercle\n3 : contourner une porte ")
menu_demo = input()
try:
    from robot2I013 import Robot2I013 as Robot
    robot = Robot()
    if menu_demo=="0" :
        from modele.controleur_robotreel_carre import ControleurRobotReelCarre
        ctrl= ControleurRobotReelCarre(robot)
    elif menu_demo=="1" :
        from modele.controleur_robotreel_mur import ControleurRobotReelMur
        ctrl=ControleurRobotReelMur(robot)
    elif menu_demo=="2" :
        from modele.controleur_robotreel_cercle import ControleurRobotReelCercle
        ctrl=ControleurRobotReelCercle(robot, 200, 5, 0, 100)
    elif menu_demo=="3" :
        from modele.controleur_robotreel_contourner_porte import ControleurRobotReelContournerPorte
        ctrl=ControleurRobotReelContournerPorte(robot)
    #ajouter les nouveaux controleurs si besoin
    else:
        print("Erreur la demo demandee n'existe pas")
        exit(1)
    def main(ctrl):
        while not ctrl.stop():
            ctrl.update()
            time.sleep(0.01)
    robot.offset_motor_encoder(robot.MOTOR_LEFT, robot.get_motor_position()[0])
    robot.offset_motor_encoder(robot.MOTOR_RIGHT, robot.get_motor_position()[1])
    #robot.set_motor_dps(robot.MOTOR_LEFT+robot.MOTOR_RIGHT,0)
    main(ctrl)

except ImportError:
    menu_type = 0
    print ("Veuillez entrer le type de simulation a lancer \n2 : simulation 2D\n3 : simulation 3D")
    menu_type = input()
    from modele.robotreel import RobotReel as Robot
    if menu_type == "2D" or menu_type == "2":
        from interface.fenetre import Fenetre
        f=Fenetre(menu_demo)
        f.creer()
    elif menu_type == "3D" or menu_type == "3":
        from interface3d.affichage3d import *
        from interface3d.fenetre3d import *
        from modele.arene import Arene
        from modele.obstacle import Obstacle
        import math as m
        import pyglet
        WINDOW = 600
        win = Window(WINDOW, WINDOW, 'Cube')
        ar=Arene(500,500)
        ob=ObstacleRectangle(60,125,40,100)
        ob1=ObstacleRectangle(200,100,100,40)
        ar.inserer_obs(ob)
        ar.inserer_obs(ob1)
        rob=RobotReel(150,400,m.pi/2,ar)
        ar.inserer_robot(rob)
        aff = Affichage(win,ar,rob,menu_demo)
        aff.on_resize(600,600)
        aff.on_draw()
        #aff.recherche_balise()
        aff.start()
        pyglet.clock.schedule_interval(aff.update, 0.1)
        pyglet.app.run()
    else :
        print("Erreur : Valeur incorrecte")
