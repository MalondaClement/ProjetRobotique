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
rob=RobotReel(70,400,m.pi/2,ar)
aff = Affichage(win,ar,rob)
aff.start()
pyglet.clock.schedule_interval(aff.update, 0.1)
pyglet.app.run()
