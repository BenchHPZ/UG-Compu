""" Modulo para funciones y clases de dibujo. """

from functools import wraps

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# from clases import matriz_propia

# Variables globales para tamanios y parametros
# Tamanio de cabeza
CABEZA_ALTO = 1
CABEZA_RADIO = 1
# Tamanio de torzo
TORSO_ALTO = 1
TORSO_RADIO = 0.5
# Tamanio de hombros
HOMBROS_ALTO = 1
HOMBROS_RADIO = 0.5
# Tamanios de brazos
BRAZO_SUP_ALTO = 1
BRAZO_SUP_RADIO = 0.5
BRAZO_INF_ALTO = 1
BRAZO_INF_RADIO = 0.5
# Tamanios de cadera
CADERA_ALTO = 1
CADERA_RADIO = 0.5
# Tamanios de piernas
PIERNA_SUP_ALTO = 1
PIERNA_SUP_RADIO = 0.5
PIERNA_INF_ALTO = 1
PIERNA_INF_RADIO = 0.5

SLICES = 10
STACKS = 10


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


####################################
# Clases del modulo para dibujos ##
##################################
class Figura:
    """ Clase para dibujar una figura general.

    Esta clase no esta pensada para usarse, solo para hacer
    poco codigo con las otras figuras
    """

    def __init__(self, i_x, i_y, i_z):
        self.tamanio = i_x,  i_y, i_z
        self.traslacion = None
        self.rotacion = None

    def trasladar(self, t_x, t_y, t_z):
        self.traslacion = (t_x, t_y, t_z)

    def rotar(self, angulo, u_x, u_y, u_z):
        if self.rotacion is None:
            self.rotacion = []
        self.rotacion.append((angulo, u_x, u_y, u_z))

    def aplicar_movimientos(self):
        pos = self.traslacion
        rotaciones = self.rotacion

        if rotaciones is not None:
            for rot in rotaciones:
                glRotatef(rot[0], rot[1], rot[2], rot[3])
        if pos is not None:
            glTranslatef(pos[0], pos[1], pos[2])


class Esfera(Figura):
    """ Clase para dibujar y manejar una esfera.

    Se usan las primitivas de OpenGl GLUT para
    dibujar una esfera con dimensiones x,y,z que
    son pasados como parametros al constructor.
    Esta no sera una esfera para terminos noramles,
    tratamos de elipsar una esfera para terminos
    del ejercicio.
    """

    def dibujar(self):
        glPushMatrix()
        glScalef(self.tamanio[0],
                 self.tamanio[1],
                 self.tamanio[2])
        self.aplicar_movimientos()
        glutSolidSphere(0.5, SLICES, STACKS)
        glPopMatrix()


class Tetera(Figura):
    """ Clase para dibujar una tetera.

    Usando las primitivas de GLUT tratamos de poner una
    tetera en el centro del plano, esto nos permite poder
    trabajar con ella de una manera mas intuitiva.
    """
    def dibujar(self):
        pass
