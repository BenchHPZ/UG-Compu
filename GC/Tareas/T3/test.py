
import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from dibujar import *
from iluminacion import *
from manejoMatrices import *


def nueva_pantalla(limpiar=True):
    # Buffer posterior
    glDrawBuffer(GL_BACK)

    glMatrixMode(GL_MODELVIEW)
    # Limpiar pantalla
    if limpiar:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()


def main():
    # Init de pygame para ventanas, botones y UI
    pg.init()
    # Init glut para figuras sin apuntadores
    glutInit(sys.argv)

    # Crear pantalla
    sz_display = (800, 650)
    window = pg.display.set_mode(sz_display, DOUBLEBUF | OPENGL)

    dim = Dimensiones()
    iluminacion()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()


        nueva_pantalla(limpiar=True)
        dibujar_ejes()
        pos = Posicion()
        # print(pos.pos_mundo())
        marioneta(pos)

        pg.display.flip()
        pg.time.wait(10)


if __name__ == '__main__':
    main()


