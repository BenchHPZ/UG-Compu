""" Modulo para clases utiles del programa. """

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


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
