import pyglet
import pyglet.gl as pgl
from pyglet.window import key
import OpenGL.GL as ogl
from .affichage3d import *
from modele.robotreel import *
from modele.arene import *
import math as m

WINDOW = 400
INCREMENT = 5

class Window(pyglet.window.Window) :

    # Rotation au lancement
    xRotation = yRotation = 30
    far = 100
    def __init__(self, width, height, title = '') :
        super(Window, self).__init__( width, height, title)
        pgl.glClearColor(0, 0, 0, 1)
        pgl.glEnable(pgl.GL_DEPTH_TEST)


win = Window(WINDOW, WINDOW, 'Cube')
aff = Affichage(win)
aff.on_resize(WINDOW,WINDOW)
aff.on_draw()


pyglet.app.run()