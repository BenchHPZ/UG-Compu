import pygame as pg

from dibujar import marioneta, Posicion
from pantalla import nueva_pantalla
from otros import PosStack


def main2():

    instancia = Posicion()
    print(instancia.ang_rodilla_der)
    instancia.ang_rodilla_der += 9
    print(instancia.ang_rodilla_der)

    print(instancia.get_all())
    instancia.set_tupla(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
    print(instancia.get_all())
    instancia.set_delta_tupla(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    print(instancia.get_all())
    print(instancia.delta_aleatorio())
    print(instancia.delta_aleatorio())
    print(instancia.get_all())


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
