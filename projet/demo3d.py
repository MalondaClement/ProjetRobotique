from interface3d.affichage3d import *
from interface3d.fenetre3d import *
from modele.arene import Arene
from modele.robotreel import RobotReel
from modele.controleur_robotreel_carre import ControleurRobotReelCarre
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
aff = Affichage(win,ar,rob)
aff.start()
aff.on_resize(600,600)
#aff.draw()
aff.on_draw()
pyglet.clock.schedule_interval(aff.update, 0.1)
pyglet.app.run()
