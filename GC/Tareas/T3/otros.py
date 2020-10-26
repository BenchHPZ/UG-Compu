""" otros.py """

import warnings


class Inmutable(object):
    """ Clase para definir una calse con atributos inmutables.

    Usamos warnings con las evasiones para no interrumpir
    el programa. Se debe tener cuidado con esto para no
    creer que si se estan cambiando los valores de las
    variables.
    """

    def __setattr__(self, key, value):
        """ Reescribimos el setter normal.

        Hacemos que el setter normal no se pueda usar para
        cambiar los valores de las variables usadas. Aunque
        si para crearlas.
        """
        if key in self.__dict__:
            warnings.warn(f"La propiedad ({key}) de ({type(self)}) no se puede modificar. ")
        else:
            self.__dict__[key] = value

    def force_set(self, key, value):
        """ Creamos un metodo que imite al setter tradicional.

        Esta funcion esta pensada para tener la flexibilidad
        de modificar los parametros, aunque esta pensada paa
        no usarse.
        """
        warnings.warn(f"({type(self)}) esta pensado para tener atributos inmutables. Sigue bajo tu propio riesgo.")
        self.__dict__[key] = value


class Prb(Inmutable):
    """ Para demostrar el funcionamiento de Inmutable """

    def __init__(self):
        self.num = 10
        self.string = 'comida'
        self.flotante = 1.2

    num2 = 11


if __name__ == '__main__':
    prb = Prb()
    print(prb.__dict__)
    print()
    print(prb.num)
    print()
    prb.num = 123
    print(prb.num)