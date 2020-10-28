""" pantalla.py
autor: bench
fecha: 26/10/20
Archivo del proyecto T3
"""

import pygame as pg
import random

from pygame.locals import *
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
        ret = pg.display.set_mode(sz_display, DOUBLEBUF | OPENGL)

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


def manejar_eventos(estados):
    paso = 0.5
    estado = None
    delta = [None for _ in range(20)]

    for events in estados:
        if events.type == pg.QUIT:
            pg.quit()
            quit()

        if events.type == pg.KEYDOWN:
            if events.key == pg.K_DOWN:
                delta[0] = [0, -paso, 0]
                estado = 'posicion'
            elif events.key == pg.K_UP:
                delta[0] = [0, paso, 0]
                estado = 'posicion'
            elif events.key == pg.K_LEFT:
                delta[0] = [-paso, 0, 0]
                estado = 'posicion'
            elif events.key == pg.K_RIGHT:
                delta[0] = [paso, 0, 0]
                estado = 'posicion'

            elif events.key == pg.K_a:
                estado = 'aleat'
            elif events.key == pg.K_o:
                delta = [0 for _ in range(20)]
                estado = 'set'
            elif events.key == pg.K_s:
                conf = input('Ingrese los parametros: (separdos por espacios)\n')
                try:
                    conf = conf.split()
                    delta = [0 for _ in range(20)]
                    delta[:len(conf)] = conf
                    delta = [int(ele) if ele is not None else 0 for ele in delta]
                    estado = 'delta'
                except:
                    print('Algo salio mal =(')

            elif events.key == pg.K_u:
                estado = 'undo'
            elif events.key == pg.K_r:
                estado = 'redo'

    return delta, estado


def fin_bucle(espera=10):
    pg.display.flip()
    pg.time.wait(espera)


def bucle_aplicacion(pos: Posicion, pila: PosStack):
    marioneta(pos)
    fin_bucle(espera=500)
