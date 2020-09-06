import numpy as np

# General
def epsilonMaquina(tipoDato):
    """ Funcion que trata de calcular el epsilon 
    de la maquina mediante el algoritmo antes pre_
    sentado. 
    Input:
        tipoDato := esta pensado para ser uno de 
            los tipos proporcionados por la li_
            breria numpy.
    Output:
        Regresa el epsilon de la maquina calcula_
            do con el tipo de dato especificado.
    """
    epsilon = tipoDato(1.0)
    unidad = tipoDato(1.0)
    valor = unidad + epsilon
    
    while valor > unidad:
        epsilon = epsilon/tipoDato(2.0)
        valor = unidad + epsilon
        
    return epsilon*2


def epsilonFloat():
    """ Calculamos el epsilon de la maquina con 
    precision de 32bits
    """
    return epsilonMaquina(np.float32)

def epsilonDouble():
    """ Calculamos el epsilon de la maquina con
    precision de 64 bits
        A pesar de que el flotante de python ya
    tiene esta precision, creo que es convenien_
    te especificarlo.
    """
    return epsilonMaquina(np.float64)

# Segunda parte
def respuesta(res):
    """ Funcion para formatear la respuesta. """
    return "iguales" if res else "diferentes"

def comparacion(epsilon):
    """ Esta funcion resivira el epsilon a eva_
    luar y el tipo de dato al que este correspon_
    de para hacer las comparaciones solicitadas
    en el ejercicio.
    Input:
        En caso de que 
    Output:
        Las respuestas son procesadas por la
        funcion respuesta para obtener el for_
        mato solicitado
            True implica que son iguales
            False implica que son diferentes
    """
    tD = type(epsilon) # Para escribir menos
    print(f'Con {epsilon=} y tipo de dato = {str(tD)} se da que')
    
    # Comprobaciones
    print(f'{respuesta( tD(1 + epsilon )   == 1 )  =}')
    print(f'{respuesta( tD( epsilon/2 )    == 0 )  =}')
    print(f'{respuesta( tD(1 + epsilon/2 ) == 1 )  =}')
    print(f'{respuesta( tD(1 - epsilon/2 ) == 1 )  =}')
    print(f'{respuesta( tD(1 - epsilon/4 ) == 1 )  =}')
    print(f'{respuesta( tD( epsilon**2 )   == 0 )  =}')
    print(f'{respuesta(epsilon + tD(epsilon**2) == epsilon) =}')
    print(f'{respuesta(epsilon - tD(epsilon**2) == epsilon) =}')
    
    print('...\n')


if __name__ == '__main__':
    # Epsilons calculados
    eF = np.float32(epsilonFloat())
    eD = np.float64(epsilonDouble())

    # Imprimir en pantalla
    print(f'Se calculalron los epsilons \n\teF={eF} y \n\teF={eD} \n para 32 y 64 bits correspondientemente.\n')

    # Hacemos la comparacion para 32bits
    comparacion(eF)
    # y para 64
    comparacion(eD)

