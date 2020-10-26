""" Modulo para manejo de matrices de transformadas. """

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from functools import wraps


# Decorador para mantener orden en matriz
def matriz_propia(fun):
    """ Funcion para manejar espacios de matriz de OpenGL.

    La funcion que sea recibida por el decorador
    espera manejar matrices de traslacion, rota_
    cion o escalamiento de OpenGl. De manera que
    este decorador agregara la matriz al inicio
    con PushMatrix, haga lo que deba hacer para
    despues quitarala al final de las operaciones
    con PopMatrix.
    """

    @wraps(fun)
    def ret_fun(*args, **kwargs):
        glPushMatrix()
        fun(*args, **kwargs)
        glPopMatrix()

    return ret_fun

#######################################
# Clases para manejo de matrices #####
#####################################


class Jerarquia:
    """ Clase para manejar Jerarquia como contexto.

    Esta clase ayudara a manejar los niveles de Jerarquia y
    sus transformaciones como cotexto. Esto ayuda a mejorar
    la legibilidad del codigo y a reducir los errores.

    Al entrar a un nuevo nivel agregamos una matriz a la pila
    de transformaciones.
    Con el objeto obtenido podemos agregar transformaciones
    directas a esta pila como tranladra, rotar y zoom.
    Al salir del contexto quitamos la matriz correspondiente.
    """

    def __init__(self) -> None:
        self.rotacion = []
        self.traslacion = []
        self.escalado = []
        glPushMatrix()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        glPopMatrix()

    def escalar(self, x, y, z):
        self.escalado.append((x, y, z))
        glScalef(x, y, z)

    def rotar(self, angulo, x, y ,z):
        self.rotacion.append((angulo, x, y, z))
        glRotatef(angulo, x, y, z)

    def trasladar(self, x, y, z):
        self.traslacion.append((x, y, z))
        glTranslatef(x, y, z)
