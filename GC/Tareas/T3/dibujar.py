""" Modulo para funciones y clases de dibujo. """

from OpenGL.GL import *
from OpenGL.GLUT import *

import hashlib
import random

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


# Variable local para acceder a dimensiones
__dim = Dimensiones()


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

    def __init__(self):
        # Posicion global
        self.global_max = 10
        self.global_min = -self.global_max
        # Central
        self.central_ang_max = 20
        self.central_ang_min = -self.central_ang_max
        # Cuello
        self.cuello_ang_max = 30
        self.cuello_ang_min = -self.cuello_ang_max
        # Cabeza
        self.cabeza_ang_rot_max = 100
        self.cabeza_ang_rot_min = -self.cabeza_ang_rot_max
        self.cabeza_ang_si_max = 30
        self.cabeza_ang_si_min = -self.cabeza_ang_si_max
        # Brazos
        self.brazo_sup_max = 180
        self.brazo_sup_min = -90
        self.brazo_inf_max = 160
        self.brazo_inf_min = -self.brazo_inf_max
        self.mano_max = 90
        self.mano_min = -self.mano_max
        # Piernas
        self.pierna_sup_max = 90
        self.pierna_sup_min = -10
        self.pierna_inf_max = 10
        self.pierna_inf_min = -110
        self.pie_max = 75
        self.pie_min = -self.pie_max


class Posicion:
    """ Clase para guardar estado de posiciones. """
    __lim = Limites()

    def __init__(self):
        """ Constructor vacio porque solo se usa para no
        tener varaibles globales declaradas por ahi y
        aumentar la posible portabilidad de los datos y
        no generar problemas cuando se importe de alguna
        manera irresponsable el modulo.
        """
        # Posicion global
        self._pos_mundo = [0, 0, 0]

        # Angulos centrales
        self._ang_hombros = 0
        self._ang_cadera = 0

        # Angulos cabeza
        self._ang_cuello = 0
        self._ang_cabeza_rot = 0
        self._ang_cabeza_si = 0

        # brazos
        self._ang_hombro_der = 0
        self._ang_codo_der = 0
        self._ang_mano_der = 0
        self._ang_hombro_izq = 0
        self._ang_codo_izq = 0
        self._ang_mano_izq = 0

        # piernas
        self._ang_gluteo_der = 0
        self._ang_rodilla_der = 0
        self._ang_pie_der = 0
        self._ang_gluteo_izq = 0
        self._ang_rodilla_izq = 0
        self._ang_pie_izq = 0

    def __hash__(self):
        ret = hashlib.md5()
        ret.update("".join([f'{val}' for val in self.__dict__.values()]).encode('utf-8'))
        return hash(ret.hexdigest())

    # Propiedades, setters y getters con los limites de las variables.
    # Pierna derecho
    @property
    def ang_gluteo_der(self):
        return self._ang_gluteo_der

    @ang_gluteo_der.setter
    def ang_gluteo_der(self, value):
        if self.__lim.pierna_sup_min < value < self.__lim.pierna_sup_max:
            self._ang_gluteo_der = value

    @property
    def ang_rodilla_der(self):
        return self._ang_rodilla_der

    @ang_rodilla_der.setter
    def ang_rodilla_der(self, value):
        if self.__lim.pierna_inf_min < value < self.__lim.pierna_inf_max:
            self._ang_rodilla_der = value

    @property
    def ang_pie_der(self):
        return self._ang_pie_der

    @ang_pie_der.setter
    def ang_pie_der(self, value):
        if self.__lim.pie_min < value < self.__lim.pie_max:
            self._ang_pie_der = value

    # Pierna izquierdo
    @property
    def ang_gluteo_izq(self):
        return self._ang_gluteo_izq

    @ang_gluteo_izq.setter
    def ang_gluteo_izq(self, value):
        if self.__lim.pierna_sup_min < value < self.__lim.pierna_sup_max:
            self._ang_gluteo_izq = value

    @property
    def ang_rodilla_izq(self):
        return self._ang_rodilla_izq

    @ang_rodilla_izq.setter
    def ang_rodilla_izq(self, value):
        if self.__lim.pierna_inf_min < value < self.__lim.pierna_inf_max:
            self._ang_rodilla_izq = value

    @property
    def ang_pie_izq(self):
        return self._ang_pie_izq

    @ang_pie_izq.setter
    def ang_pie_izq(self, value):
        if self.__lim.pie_min < value < self.__lim.pie_max:
            self._ang_pie_izq = value

    # Brazo izquierdo
    @property
    def ang_hombro_izq(self):
        return self._ang_hombro_izq

    @ang_hombro_izq.setter
    def ang_hombro_izq(self, value):
        if self.__lim.brazo_sup_min < value < self.__lim.brazo_sup_max:
            self._ang_hombro_izq = value

    @property
    def ang_codo_izq(self):
        return self._ang_codo_izq

    @ang_codo_izq.setter
    def ang_codo_izq(self, value):
        if self.__lim.brazo_inf_min < value < self.__lim.brazo_inf_max:
            self._ang_codo_izq = value

    @property
    def ang_mano_izq(self):
        return self._ang_mano_izq

    @ang_mano_izq.setter
    def ang_mano_izq(self, value):
        if self.__lim.mano_min < value < self.__lim.mano_max:
            self._ang_mano_izq = value

    # Brazo derecho
    @property
    def ang_hombro_der(self):
        return self._ang_hombro_der

    @ang_hombro_der.setter
    def ang_hombro_der(self, value):
        if self.__lim.brazo_sup_min < value < self.__lim.brazo_sup_max:
            self._ang_hombro_der = value

    @property
    def ang_codo_der(self):
        return self._ang_codo_der

    @ang_codo_der.setter
    def ang_codo_der(self, value):
        if self.__lim.brazo_inf_min < value < self.__lim.brazo_inf_max:
            self._ang_codo_der = value

    @property
    def ang_mano_der(self):
        return self._ang_mano_der

    @ang_mano_der.setter
    def ang_mano_der(self, value):
        if self.__lim.mano_min < value < self.__lim.mano_max:
            self._ang_mano_der = value

    # Cabeza
    @property
    def ang_cabeza_rot(self):
        return self._ang_cabeza_rot

    @ang_cabeza_rot.setter
    def ang_cabeza_rot(self, value):
        if self.__lim.cabeza_ang_si_min < value < self.__lim.cabeza_ang_si_max:
            self._ang_cabeza_rot = value

    @property
    def ang_cabeza_si(self):
        return self._ang_cabeza_si

    @ang_cabeza_si.setter
    def ang_cabeza_si(self, value):
        if self.__lim.cabeza_ang_si_min < value < self.__lim.cabeza_ang_si_max:
            self._ang_cabeza_si = value

    @property
    def ang_cuello(self):
        return self._ang_cuello

    @ang_cuello.setter
    def ang_cuello(self, value):
        if self.__lim.cuello_ang_min < value < self.__lim.cuello_ang_max:
            self._ang_cuello = value

    # Objetos centrales
    @property
    def ang_cadera(self):
        return self._ang_cadera

    @ang_cadera.setter
    def ang_cadera(self, value):
        if self.__lim.central_ang_min < value < self.__lim.central_ang_max:
            self._ang_cadera = value

    @property
    def ang_hombros(self):
        return self._ang_hombros

    @ang_hombros.setter
    def ang_hombros(self, value):
        if self.__lim.central_ang_min < value < self.__lim.central_ang_max:
            self._ang_hombros = value

    # Posicion absoluta
    @property
    def pos_mundo(self):
        return self._pos_mundo

    @pos_mundo.setter
    def pos_mundo(self, value):
        if self.__lim.global_min < value[0] < self.__lim.global_max \
                and self.__lim.global_min < value[1] < self.__lim.global_max \
                and self.__lim.global_min < value[2] < self.__lim.global_max:
            self._pos_mundo = value

    def get_all(self):
        """ Return values of all atributes. """
        return [
            self.pos_mundo,
            # Lado derecho
            self.ang_hombro_der,
            self.ang_codo_der,
            self.ang_mano_der,
            self.ang_gluteo_der,
            self.ang_rodilla_der,
            self.ang_pie_der,
            # Lado izquierdo
            self.ang_hombro_izq,
            self.ang_codo_izq,
            self.ang_mano_izq,
            self.ang_gluteo_izq,
            self.ang_rodilla_izq,
            self.ang_pie_izq,
            # Angulos cabeza
            self.ang_cuello,
            self.ang_cabeza_rot,
            self.ang_cabeza_si,
            # Extras
            self.ang_hombros,
            self.ang_cadera,
        ]

    def get_setters(self):
        """ Return all name functions to set atributes. """
        return [
            'pos_mundo',
            # Lado derecho
            'ang_hombro_der',
            'ang_codo_der',
            'ang_mano_der',
            'ang_gluteo_der',
            'ang_rodilla_der',
            'ang_pie_der',
            # Lado izquierdo
            'ang_hombro_izq',
            'ang_codo_izq',
            'ang_mano_izq',
            'ang_gluteo_izq',
            'ang_rodilla_izq',
            'ang_pie_izq',
            # Angulos cabeza
            'ang_cuello',
            'ang_cabeza_rot',
            'ang_cabeza_si',
            # Extras
            'ang_hombros',
            'ang_cadera',
        ]

    def _charge_tuple(self, args):
        PARAMETROS = 20 - 2
        flag = True

        total = [None for _ in range(PARAMETROS)]
        lon = len(args)
        if lon == 12:
            total[1:1 + lon] = args
        elif lon == 15:
            total[1:1 + lon] = args
        elif lon == 17:
            total[1:1 + lon] = args
        elif lon == 20:
            total[1:] = args[:-3]
            total[0] = (args[-3], args[-2], args[-1])
        else:
            flag = False
        return total, flag

    def set_tupla(self, *args):
        """ Se reciben tuplas para establecer como valores de los angulos
        del modelo. Todos los valroes que se reciban aqui pasaran por los
        setters para mantener

        Si se reciben 12 elementos, se aplicara sobre las extremidades, de
        izquierda a derecha (primero cada lado), de el hombro al pie.
        Si se reciben 15 elemetos, se aplican a los anteriores mas los tres
        puntos de la cara.
        Si se reciben 17 se tambien se aplicara a cadera y hombros.
        Y si se reciben 20, tambien se trasladara.
        """
        total, flag = self._charge_tuple(args)
        if flag:
            params = self.get_setters()
            if len(params) == len(total):
                for i in range(len(total)):
                    if total[i] is not None:
                        setattr(self, params[i], total[i])
            else:
                raise Exception('Error de tamanios')
            return True
        return False

    def set_delta_tupla(self, *args):
        total, flag = self._charge_tuple(args)
        if flag:
            params = self.get_setters()
            if len(params) == len(total):
                for i in range(1, len(total)):
                    if total[i] is not None:
                        setattr(self, params[i], getattr(self, params[i]) + total[i])
            else:
                raise Exception('Error de tamanios')
            return self.get_all()
        return False

    def delta_aleatorio(self, paso=5):
        PARAMETROS = 20
        tupla = [random.choice([-1, 0, 1]) * paso for _ in range(PARAMETROS)]
        return self.set_delta_tupla(*tupla)


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
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -unidad)
    glVertex3f(0.0, 0.0, unidad)

    glEnd()


###################################
# Partes del cuerpo para dibujar #
#################################


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
    ang = 90
    rot = ang if derecho else -ang
    glRotatef(rot, 0, 1, 0)
    glRotatef(-170, 1, 0, 0)
    # Transformadas generales
    # (ARRIBA) NO TOCAR (ARRIBA)

    # Union de hombro
    with Jerarquia() as _hombro:
        # Rotacion hombro
        ang = pos.ang_hombro_der if derecho else pos.ang_hombro_izq
        _hombro.rotar(ang, 1, 0, 0)
        brazo_superior()

        # Union de codo
        with Jerarquia() as _codo:
            # Rotacion de codo
            ang = pos.ang_codo_der if derecho else pos.ang_codo_izq
            _codo.trasladar(0, __dim.BRAZO_SUP_ALTO, 0)
            _codo.rotar(ang, 1, 0, 0)
            brazo_inferior()

            # Union de mano
            with Jerarquia() as _mano:
                # Rotacion en munieca
                ang = pos.ang_mano_der if derecho else pos.ang_mano_izq
                _mano.trasladar(0, __dim.BRAZO_INF_ALTO, 0)
                _mano.rotar(ang, 0, 1, 0)
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
    obj.rotar(180, 0, 0, 1)
    obj.rotar(90, 0, 1, 0)
    obj.trasladar(5 * __dim.PIE_RADIO / 6, 0, 0)
    obj.dibujar(base2origen=True)


@matriz_propia
def pierna(derecho: bool, pos: Posicion):
    """ Funcion para dibujar una pierna.
    Si la pierna no es derecho, entonces es izquierdo.
    """
    ang = 90
    rot = ang if derecho else -ang
    glRotatef(rot, 0, 1, 0)
    # (ARRIBA) Transformadas generales (ARRIBA)
    # (ARRIBA) NO TOCAR (ARRIBA)

    """ Los derecho e izquierdos estan cambiados aqui, pero 
    no encuentro la manera correcta de arreglarlo sin que se
    rompa y ya estoy cansado. ='(
    todo: solucionar esto =)
    """

    # Union de nalga
    with Jerarquia() as _nalga:
        # Rotacion nalga
        ang = pos.ang_gluteo_izq if derecho else pos.ang_gluteo_der
        _nalga.rotar(-ang, 1, 0, 0)
        pierna_superior()

        # Union de rodilla
        with Jerarquia() as _rodilla:
            # Rotacion de rodilla
            ang = pos.ang_rodilla_izq if derecho else pos.ang_rodilla_der
            _rodilla.trasladar(0, __dim.PIERNA_SUP_ALTO, 0)
            _rodilla.rotar(-ang, 1, 0, 0)

            # Union de pie
            with Jerarquia() as _pie:
                # Rotacion en tobillo
                # Si, esta al revez, cometi un error de orientacion
                # en algun lado pero no lo encuentro
                ang = pos.ang_pie_izq if derecho else pos.ang_pie_der
                _pie.trasladar(0, __dim.PIERNA_INF_ALTO, 0)
                _pie.rotar(-ang, 1, 0, 0)

                pie()
            pierna_inferior()


############################
#        Muniequo        ##
##########################

def marioneta(pos: Posicion):
    """ Funcion para dibujar marioneta dadas  posiciones. """

    # Empezamos =D
    with Jerarquia() as origen:
        origen.escalar(__dim.ESCALA,
                       __dim.ESCALA,
                       __dim.ESCALA)
        # ## (ARRIBA) NO TOCAR (ARRIBA) ###
        origen.trasladar(pos.pos_mundo[0],
                         pos.pos_mundo[1],
                         pos.pos_mundo[2])
        origen.rotar(0, 0, 1, 0)

        with Jerarquia() as _cuello:
            _cuello.trasladar(0, __dim.TORSO_ALTO / 2, 0)
            # ## (ARRIBA) NO TOCAR (ARRIBA) ###
            _cuello.rotar(pos.ang_cuello, 0, 0, 1)

            cuello()
            with Jerarquia() as _cabeza:
                _cabeza.trasladar(0, __dim.CUELLO_ALTO, 0)
                # ## (ARRIBA) NO TOCAR (ARRIBA) ###
                # (ABAJO) Rotaciones de cabeza (ABAJO)
                _cabeza.rotar(pos.ang_cabeza_si,
                              1, 0, 0)  # rotacion SI (x)
                _cabeza.rotar(pos.ang_cabeza_rot,
                              0, 1, 0)  # rotacion NO (y)

                cabeza()

        with Jerarquia() as _cadera:
            _cadera.trasladar(0, -__dim.TORSO_ALTO / 2, 0)
            _cadera.rotar(180, 0, 0, 1)
            # ## (ARRIBA) NO TOCAR (ARRIBA) ###
            # (ABAJO) Rotar cadera (ABAJO)
            _cadera.rotar(pos.ang_cadera, 0, 0, 1)

            cadera()
            with Jerarquia() as pierna_der:
                pierna_der.trasladar(-__dim.CADERA_ALTO / 2, 0, 0)
                pierna(derecho=True, pos=pos)
            with Jerarquia() as pierna_izq:
                pierna_izq.trasladar(__dim.CADERA_ALTO / 2, 0, 0)
                pierna(derecho=False, pos=pos)

        torso()
        with Jerarquia() as _hombros:
            _hombros.trasladar(0, __dim.TORSO_ALTO / 2, 0)
            # ## (ARRIBA) NO TOCAR (ARRIBA) ###
            # (ABAJO) Rotar hombros (ABAJO)
            _hombros.rotar(pos.ang_hombros, 0, 0, 1)

            hombros()
            with Jerarquia() as brazo_der:
                brazo_der.trasladar(-__dim.HOMBROS_ALTO / 2, 0, 0)
                brazo(derecho=True, pos=pos)
            with Jerarquia() as brazo_izq:
                brazo_izq.trasladar(__dim.HOMBROS_ALTO / 2, 0, 0)
                brazo(derecho=False, pos=pos)

        None
