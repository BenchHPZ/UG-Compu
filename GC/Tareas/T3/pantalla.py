""" pantalla.py
autor: bench
fecha: 26/10/20
Archivo del proyecto T3
"""

import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLUT import *

from iluminacion import iluminacion
from dibujar import dibujar_ejes


def nueva_pantalla(limpiar=True, init=False, sz_display=(800, 700), ejes=False, td=True):
    ret = None
    if init:
        pg.init()
        glutInit(sys.argv)
        iluminacion()
        ret = pg.display.set_mode(sz_display, DOUBLEBUF|OPENGL)

    # Buffer posterior
    glDrawBuffer(GL_BACK)
    glMatrixMode(GL_MODELVIEW)
    # Limpiar pantalla
    if limpiar:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    if td:
        iluminacion()
    if ejes:
        dibujar_ejes()

    glLoadIdentity()
    return ret
