""" pantalla.py
autor: bench
fecha: 26/10/20
Archivo del proyecto T3
"""

import pygame as pg
from pygame.locals import *
from functools import wraps

from OpenGL.GL import *
from OpenGL.GLUT import *

from iluminacion import iluminacion
from dibujar import dibujar_ejes, Posicion, marioneta
from otros import PosStack


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

    pos = Posicion()
    glLoadIdentity()
    return ret, pos


def manejar_eventos():
    eventos = {}
    for events in pg.event.get():
        if events.type == pg.QUIT:
            pg.quit()
            quit()

        if events.type == pg.KEYDOWN:
            if events.key == pg.K_DOWN:
                eventos['down'] = True
            if events.key == pg.K_UP:
                eventos['up'] = True
            if events.key == pg.K_LEFT:
                eventos['left'] = True
            if events.key == pg.K_RIGHT:
                eventos['right'] = True

            if events.key == pg.K_b:
                eventos['b'] = True
            elif events.key == pg.K_o:
                eventos['o'] = True
            elif events.key == pg.K_s:
                eventos['set'] = [
                    float(input()),
                    float(input()),
                    float(input()),
                    float(input()),
                    float(input()),
                    float(input()),
                    float(input()),
                    float(input()),
                    float(input()),
                    float(input()),
                    float(input()),
                    float(input()),
                    float(input()),
                    float(input()),
                    float(input()),
                ]
                print('Espere...')

            if events.key == pg.K_u:
                eventos['undo'] = True
            elif events.key == pg.K_r:
                eventos['redo'] = True

    return eventos


def fin_bucle(espera=10):
    pg.display.flip()
    pg.time.wait(espera)


def bucle_aplicacion(pos: Posicion, pila: PosStack):




    marioneta(pos)
    fin_bucle(espera=500)
