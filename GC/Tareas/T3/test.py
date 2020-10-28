import pygame as pg

from dibujar import marioneta, Posicion
from pantalla import bucle_aplicacion, nueva_pantalla, manejar_eventos
from otros import PosStack




def main():
    screen, pos = nueva_pantalla(limpiar=True, init=True, ejes=True, sz_display=(800, 700))
    print(type(pos))
    pila = PosStack(max_lon=15)
    print(type(pila))


    while False:
        eventos = manejar_eventos()
        nueva_pantalla(limpiar=True, ejes=True)



        if 'b' in eventos:  # Movimiento random
            pila.push(pos.delta_aleatorio())
        elif 'o' in eventos:  # Posicion original
            pila.push(data=pos.set_tupla(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))

        paso = 0.5
        if 'down' in eventos:
            temp = pos.pos_mundo
            temp[1] -= paso
            pos.pos_mundo = temp
            pila.push(pos.get_all())
        elif 'up' in eventos:
            temp = pos.pos_mundo
            temp[1] += paso
            pos.pos_mundo = temp
            pila.push(pos.get_all())
        elif 'right' in eventos:
            temp = pos.pos_mundo
            temp[0] += paso
            pos.pos_mundo = temp
            pila.push(pos.get_all())
        elif 'left' in eventos:
            temp = pos.pos_mundo
            temp[0] -= paso
            pos.pos_mundo = temp
            pila.push(pos.get_all())

        if 'undo' in eventos:
            pila.undo()
            pos.set_tupla(pila.read())
        elif 'redo' in eventos:
            pila.redo()
            pos.set_tupla(pila.read())
        bucle_aplicacion(pos, pila)


if __name__ == '__main__':
    main()
