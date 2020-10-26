
import pygame as pg

from dibujar import *
from pantalla import nueva_pantalla


def main():

    nueva_pantalla(limpiar=True, init=True, ejes=True, sz_display=(800, 700))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        nueva_pantalla(limpiar=True, ejes=True)
        pos = Posicion()
        marioneta(pos)

        pg.display.flip()
        pg.time.wait(10)


if __name__ == '__main__':
    main()


