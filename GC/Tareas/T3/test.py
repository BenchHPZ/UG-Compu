import pygame as pg

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from dibujar import *
from clases import *
from iluminacion import *


def nueva_pantalla(limpiar=True):
    # Buffer posterior
    glDrawBuffer(GL_BACK)

    # Limpiar pantalla
    if limpiar:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Mover camara
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    global ang
    # Init glut para figuras sin apuntadores
    glutInit(sys.argv)
    # Init de pygame para ventanas, botones y UI
    pg.init()
    # Crear pantalla
    sz_display = (800, 650)
    window = pg.display.set_mode(sz_display, DOUBLEBUF | OPENGL)

    iluminacion()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        nueva_pantalla(limpiar=True)
        with Jerarquia() as mundo:
            mundo.rotar(ang, 1, 1, 1)
            esfera = Esfera(1, 0.5, 2)
            esfera.dibujar()

            ang += 1

        pg.display.flip()
        pg.time.wait(50)


ang = 0
if __name__ == '__main__':
    main()
