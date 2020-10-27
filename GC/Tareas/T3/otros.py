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


class PosStack:
    """ Pila de posiciones.

    Dado que debemos poder hacer undo y redo sobre las tranformaciones
    de la figura, usare una especia de pila (Stack), de tamanio fijo.

    Cuando hagamos undo se mantendran todos los elementos hasta que se
    realice otra transformacion. En este caso se ignroara all que este
    despues del nodo actual. Si se trata de actualizar una matriz igual
    a la ultima agregada sera ignorada la operacion.
    """

    def __init__(self, max_lon=10):
        self._data = [None for _ in range(max_lon)]
        self._act = -1
        self._max_lon = max_lon

    def push(self, data):
        """ Agregamos un nuevo elemento. """
        if self._act >= self._max_lon-1:
            # Eliminamos el primero y recorremos
            self._data[:-1] = self._data[1:]
            self._act -= 1

        self._act += 1
        self._data[self._act] = data
        # Nuleamos lo que este despues de nosotros.
        for i in range(self._act+1, self._max_lon):
            self._data[i] = None

    def undo(self):
        """ Regresamos el indice en uno (si se puede) """
        if self._act > 0:
            self._act -= 1
            return True
        return False

    def redo(self):
        """ Avanzamos el indice en uno (si se puede) """
        if self._act < self._max_lon-1 and\
                self._data[self._act+1] is not None:
            self._act += 1
            return True
        return False

    def read(self):
        """ Regresamos la informacion considerada actual. """
        return self._data[self._act]
