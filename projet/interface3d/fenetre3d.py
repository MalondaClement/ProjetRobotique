import pyglet
import pyglet.gl as pgl
from pyglet.window import key
import OpenGL.GL as ogl
from .affichage3d import *
import math as m

WINDOW = 600
INCREMENT = 5

class Window(pyglet.window.Window) :

    # Rotation au lancement
    xRotation = yRotation = 0
    far = 200
    def __init__(self, width, height, title = '') :
        super(Window, self).__init__( width, height, title)
        pgl.glClearColor(0, 0, 0, 1)
        pgl.glEnable(pgl.GL_DEPTH_TEST)


win = Window(WINDOW, WINDOW, 'Cube')
aff = Affichage(win)
aff.on_resize(WINDOW,WINDOW)
aff.mur()


pyglet.app.run()
