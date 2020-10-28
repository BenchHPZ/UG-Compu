import pygame as pg

from dibujar import marioneta
from pantalla import nueva_pantalla, manejar_eventos


def main_b():
    screen, pos = nueva_pantalla(limpiar=True, init=True, ejes=False, sz_display=(800, 700))

    while True:
        nueva_pantalla(limpiar=True, ejes=True)
        pos.delta_aleatorio(paso=10)
        marioneta(pos)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        pg.display.flip()
        pg.time.wait(100)


def main_e():
    screen, pos = nueva_pantalla(limpiar=True, init=True, ejes=True, sz_display=(800, 700))

    while True:
        tupla, chng = manejar_eventos(pg.event.get())
        if chng == 'set':
            pos.set_tupla(*tupla)
        elif chng == 'delta':
            pos.set_delta_tupla(*tupla)
        elif chng == 'posicion':
            temp = pos.pos_mundo
            pos.pos_mundo = [temp[0] + tupla[0][0],
                             temp[1] + tupla[0][1],
                             temp[2] + tupla[0][2]]
        elif chng == 'aleat':
            pos.delta_aleatorio()
        elif chng == 'undo':
            pass
        elif chng == 'redo':
            pass

        nueva_pantalla(limpiar=True, ejes=True)
        marioneta(pos)

        pg.display.flip()
        pg.time.wait(100)


if __name__ == '__main__':
    # op = input('Opcion de ejecucion: (e := Experimental, b := Estable)\n')

    if True:
        main_e()
    # elif op.startswith('b'):
    #    main_b()
