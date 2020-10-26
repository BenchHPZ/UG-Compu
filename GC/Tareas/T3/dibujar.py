""" Modulo para funciones y clases de dibujo. """

from OpenGL.GL import *
from OpenGL.GLUT import *

from otros import Inmutable
from manejoMatrices import Jerarquia, matriz_propia


#####################################################
# Clases para guardar parametros y configuraciones #
###################################################

class Dimensiones(Inmutable):
    """ Clase para guardar las dimensioens del munieco"""

    def __init__(self):
        """ Constructor vacio porque solo se usa para no
        tener varaibles globales declaradas por ahi y
        aumentar la posible portabilidad de los datos y
        no generar problemas cuando se importe de alguna
        manera irresponsable el modulo.
        """
        self.ESCALA = 0.2
        # Tamanio de cabeza
        self.CABEZA_ALTO = 0.6
        self.CABEZA_RADIO = 0.6
        # Tamanio de cuello
        self.CUELLO_ALTO = 0.4
        self.CUELLO_RADIO = 0.2
        # Tamanio de torzo
        self.TORSO_ALTO = 2
        self.TORSO_RADIO = 1.2
        # Tamanio de hombros
        self.HOMBROS_ALTO = 1.2
        self.HOMBROS_RADIO = 0.5
        # Tamanios de brazos
        self.BRAZO_SUP_ALTO = 1.1
        self.BRAZO_SUP_RADIO = 0.3
        self.BRAZO_INF_ALTO = 1
        self.BRAZO_INF_RADIO = 0.2
        # Tamanio de mano
        self.MANO_ALTO = 0.4
        self.MANO_RADIO = 0.4
        # Tamanios de cadera
        self.CADERA_ALTO = 0.9
        self.CADERA_RADIO = 0.5
        # Tamanios de piernas
        self.PIERNA_SUP_ALTO = 1.1
        self.PIERNA_SUP_RADIO = 0.4
        self.PIERNA_INF_ALTO = 1
        self.PIERNA_INF_RADIO = 0.3
        # Tamanio de pies
        self.PIE_ALTO = 0.5
        self.PIE_RADIO = 0.35


class Parametros(Inmutable):
    """ Clase para guardar parametros. """

    def __init__(self):
        """ Constructor vacio porque solo se usa para no
        tener varaibles globales declaradas por ahi y
        aumentar la posible portabilidad de los datos y
        no generar problemas cuando se importe de alguna
        manera irresponsable el modulo.
        """
        self.SLICES = 10
        self.STACKS = 10
        self.RADIO = 0.5
        self.DELTA_Y_TETERA = 0.38


class Limites(Inmutable):
    """ Clase para limites de posiciones. """

    pass

class Posicion:
    """ Clase para guardar estado de posiciones. """

    def __init__(self):
        """ Constructor vacio porque solo se usa para no
        tener varaibles globales declaradas por ahi y
        aumentar la posible portabilidad de los datos y
        no generar problemas cuando se importe de alguna
        manera irresponsable el modulo.
        """
        self._pos_mundo = (0, 0, 0)
        self._cuello = 0

    @property
    def pos_mundo(self):
        return self._pos_mundo

    @pos_mundo.setter
    def pos_mundo(self, value):
        if -10 < value < 10:
            self._pos_mundo = value


####################################
# Clases del modulo para dibujos ##
##################################

class Figura:
    """ Clase para dibujar una figura general.

    Esta clase no esta pensada para usarse, solo para hacer
    poco codigo con las otras figuras
    """

    def __init__(self, i_x, i_y, i_z):
        """ Constructor de metodo.

        Inicialmente cargamos las dimensiones en
        x,y,z para deseamos para la figura.
        """
        self.tamanio = i_x, i_y, i_z
        self.traslacion = None
        self.rotacion = None

    def trasladar(self, t_x, t_y, t_z):
        """ Funcion de traslacion.

        Funcion para cargar las traslaciones a
        aplicar sobre la figura. Las traslaciones
        seran consideradas como una misma y no son
        aplicadas aqui.
        """
        if self.traslacion is None:
            self.traslacion = (t_x, t_y, t_z)
        else:
            self.traslacion = (self.traslacion[0] + t_x,
                               self.traslacion[1] + t_y,
                               self.traslacion[2] + t_z)

    def rotar(self, angulo, u_x, u_y, u_z):
        """ Funcion de rotacion.

         Funcion para rotar la figura en su propio
         eje, las rotaciones seran aplicadas en el
         orden que sean cargadas sobre la figura y
         siempre despues del escalado pero antes de
         la rotacion.
         """
        if self.rotacion is None:
            self.rotacion = []
        self.rotacion.append((angulo, u_x, u_y, u_z))

    def aplicar_transformadas(self):
        """ Funcion para aplicar transformadas.

        Esta funcion aplicara las transformadas
        necesarias para dar el objeto deseado,
        estas deben ser cargadas antes. Escalamos,
        rotamos y trasladamos.
        """

        pos = self.traslacion
        rotaciones = self.rotacion
        # Escalamos dimensiones a constructor.
        glScalef(self.tamanio[0],
                 self.tamanio[1],
                 self.tamanio[2])
        # Rotamos lo agregado
        if rotaciones is not None:
            for rot in rotaciones:
                glRotatef(rot[0], rot[1], rot[2], rot[3])
        # Trasladamos una sola vez todas las proporcionadas.
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

    @matriz_propia
    def dibujar(self, base2origen=False) -> None:
        """ Funcion especifica para dibujar una esfera.

        Input:
            base2origen := (default: False) Valor boleano que
                indica si la base del objeto se debe poner en
                el origen. Este movimiento implicara mover la
                mitad de la longitud del objeto en el eje y.
                Esto sera agregado a las demas trasnformaciones
                que se hayan aplicado sobre el objeto.
        """
        param = Parametros()
        if base2origen:
            self.trasladar(0, param.RADIO, 0)
        self.aplicar_transformadas()
        glutSolidSphere(param.RADIO, param.SLICES, param.STACKS)


class Tetera(Figura):
    """ Clase para dibujar una tetera.

    Usando las primitivas de GLUT tratamos de poner una
    tetera en el centro del plano, esto nos permite poder
    trabajar con ella de una manera mas intuitiva.
    """

    @matriz_propia
    def dibujar(self, base2origen=False) -> None:
        """ Funcion especifica para dibujar una tetera.

        Input:
            base2origen := (default: False) Valor boleano que
                indica si la base del objeto se debe poner en
                el origen. Este movimiento implicara mover la
                mitad de la longitud del objeto en el eje y.
                Esto sera agregado a las demas trasnformaciones
                que se hayan aplicado sobre el objeto.
        """
        param = Parametros()
        if base2origen:
            self.trasladar(0, param.DELTA_Y_TETERA, 0)
        self.aplicar_transformadas()
        glutSolidTeapot(param.RADIO)


####################################
#    Funciones independientes    ##
##################################


def dibujar_ejes():
    """ Funcion para dibujar los ejes.

    Se debe correr antes de realizar cualquier otra
    transformacion para que los ejes queden en el
    lugar correcto.
    """
    unidad = 1
    glBegin(GL_LINES)
    # eje X
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-unidad, 0.0, 0.0)
    glVertex3f(unidad, 0.0, 0.0)
    # eje Y
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(0.0, -unidad, 0.0)
    glVertex3f(0.0, unidad, 0.0)
    # eje Z
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(0.0, 0.0, -unidad)
    glVertex3f(0.0, 0.0, unidad)

    glEnd()


###################################
# Partes del cuerpo para dibujar #
#################################
# Variable local para acceder a dimensiones
__dim = Dimensiones()


def torso():
    """ Funcion para dibujar el torso.

    El torso, al coincidir con la jerarquia global,
    no se le debe agregar ninguna transformada.
    """
    Esfera(__dim.TORSO_RADIO,
           __dim.TORSO_ALTO,
           __dim.TORSO_RADIO).dibujar()


###################
# ##  Cabeza  ## #
#################
def cuello():
    """ Funcion para dibujar el cuello. """
    Esfera(__dim.CUELLO_RADIO,
           __dim.CUELLO_ALTO,
           __dim.CUELLO_RADIO
           ).dibujar(base2origen=True)


def cabeza():
    obj = Tetera(__dim.CABEZA_RADIO,
                 __dim.CABEZA_ALTO,
                 __dim.CABEZA_RADIO)
    # Empezamos con la cabeza de frente
    obj.rotar(90, 0, 1, 0)
    obj.dibujar(base2origen=True)


###################
# parte superior #
#################
def hombros():
    """ Funcion para dibujar los hombros. """
    Esfera(__dim.HOMBROS_ALTO,
           __dim.HOMBROS_RADIO,
           __dim.HOMBROS_RADIO).dibujar()


def brazo_superior():
    """ Funcion para dibujar antebrazo. """
    Esfera(__dim.BRAZO_SUP_RADIO,
           __dim.BRAZO_SUP_ALTO,
           __dim.BRAZO_SUP_RADIO
           ).dibujar(base2origen=True)


def brazo_inferior():
    """ Funcion para dibujar brazo. """
    Esfera(__dim.BRAZO_INF_RADIO,
           __dim.BRAZO_INF_ALTO,
           __dim.BRAZO_INF_RADIO
           ).dibujar(base2origen=True)


def mano():
    """ Funcion para dibujar mano. """
    obj = Tetera(__dim.MANO_RADIO,
                 __dim.MANO_ALTO,
                 __dim.MANO_RADIO)
    obj.rotar(90, 0, 1, 0)
    obj.dibujar(base2origen=True)


@matriz_propia
def brazo(derecho: bool, pos: Posicion):
    """ Funcion para dibujar un brazo.
    Si el brazo no es derecho, entonces es izquierdo.
    """

    init_ang = 90
    rot = init_ang if derecho else -init_ang
    # Rotacion general
    glRotatef(rot, 0, 1, 0)

    # Union de hombro
    # glRotatef() # Rotacion hombro
    brazo_superior()

    # Union de codo
    # glRotatef() # Rotacion de codo
    glTranslatef(0, __dim.BRAZO_SUP_ALTO, 0)
    brazo_inferior()

    # Union de mano
    # glRotatef() # Rotacion en munieca
    glTranslatef(0, __dim.BRAZO_INF_ALTO, 0)
    mano()


###################
# parte inferior #
#################
def cadera():
    """ Funcion para dibujar la cadera. """
    Esfera(__dim.CADERA_ALTO,
           __dim.CADERA_RADIO,
           __dim.CADERA_RADIO).dibujar()


def pierna_superior():
    """ Funcion para dibujar antebrazo. """
    Esfera(__dim.PIERNA_SUP_RADIO,
           __dim.PIERNA_SUP_ALTO,
           __dim.PIERNA_SUP_RADIO
           ).dibujar(base2origen=True)


def pierna_inferior():
    """ Funcion para dibujar brazo. """
    Esfera(__dim.PIERNA_INF_RADIO,
           __dim.PIERNA_INF_ALTO,
           __dim.PIERNA_INF_RADIO
           ).dibujar(base2origen=True)


def pie():
    """ Funcion para dibujar mano. """
    obj = Tetera(__dim.PIE_RADIO,
                 __dim.PIE_RADIO,
                 __dim.PIE_ALTO)
    obj.rotar(90, 0, 1, 0)
    obj.trasladar(__dim.PIE_RADIO/3, 0, 0)
    obj.dibujar(base2origen=True)


@matriz_propia
def pierna(derecho: bool, pos: Posicion):
    """ Funcion para dibujar una pierna.
    Si la pierna no es derecho, entonces es izquierdo.
    """
    init_ang = 90
    rot = init_ang if derecho else -init_ang
    # Rotacion general
    glRotatef(rot, 0, 1, 0)

    # Union de hombro
    # glRotatef() # Rotacion nalga
    pierna_superior()

    # Union de codo
    # glRotatef() # Rotacion de rodilla
    glTranslatef(0, __dim.PIERNA_SUP_ALTO, 0)
    pierna_inferior()

    # Union de mano
    # glRotatef() # Rotacion en tobillo
    glTranslatef(0, __dim.PIERNA_INF_ALTO, 0)
    pie()


############################
#        Muniequo        ##
##########################

def marioneta(pos):
    """ Funcion para dibujar marioneta dadas  posiciones. """

    dim = __dim

    with Jerarquia() as origen:
        origen.escalar(dim.ESCALA,
                       dim.ESCALA,
                       dim.ESCALA)

        with Jerarquia() as _cuello:
            _cuello.trasladar(0, dim.TORSO_ALTO / 2, 0)
            cuello()
            with Jerarquia() as _cabeza:
                _cabeza.trasladar(0, dim.CUELLO_ALTO, 0)
                # Rotacioens
                cabeza()

        with Jerarquia() as _hombros:
            _hombros.trasladar(0, dim.TORSO_ALTO / 2, 0)
            hombros()
            with Jerarquia() as brazo_der:
                brazo_der.trasladar(-dim.HOMBROS_ALTO / 2, 0, 0)
                brazo_der.rotar(170, 0, 0, 1)
                brazo(derecho=True, pos=pos)
            with Jerarquia() as brazo_izq:
                brazo_izq.trasladar(dim.HOMBROS_ALTO / 2, 0, 0)
                brazo_izq.rotar(-170, 0, 0, 1)
                brazo(derecho=False, pos=pos)

        with Jerarquia() as _cadera:
            _cadera.trasladar(0, -dim.TORSO_ALTO / 2, 0)
            cadera()
            _cadera.rotar(180, 0, 0, 1)
            with Jerarquia() as pierna_der:
                pierna_der.trasladar(-dim.CADERA_ALTO / 2, 0, 0)
                # pierna_der.rotar(0, 0, 0, 0)
                pierna(derecho=True, pos=pos)
            with Jerarquia() as pierna_izq:
                pierna_izq.trasladar(dim.CADERA_ALTO / 2, 0, 0)
                pierna(derecho=False, pos=pos)

        # Queremos que el torso este al frente
        torso()