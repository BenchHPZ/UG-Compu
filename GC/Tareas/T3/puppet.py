import pygame as pg

from dibujar import marioneta, Posicion
from pantalla import bucle_aplicacion, nueva_pantalla, manejar_eventos
from otros import PosStack


def main():

    screen, pos = nueva_pantalla(limpiar=True, init=True, ejes=True, sz_display=(800, 700))

    while True:
        nueva_pantalla(limpiar=True, ejes=True)
        pos.delta_aleatorio(paso=10)
        marioneta((pos))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        pg.display.flip()
        pg.time.wait(100)


if __name__ == '__main__':
    main()
