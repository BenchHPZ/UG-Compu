""" Modulo de utilidad para clase Metodos Numericos

Este mpdulo fue creado con funciones que encontre utiles,
que programe muchas veces o que me parecieron interesantes
durante el curso de metodos numericos que tome durante el
semestre ago-dic 20 en el CIMAT.

Algunas de las funciones aqui presentes pueden tener
mejores implementaciones en otro lado. No te recomiendo
usarlo. Y POR SUPUESTO que NO viene con garantia alguna.

Si te es util de alguna forma te agradeceria que me lo 
hicieras saber =)
Tambien invito a que se quejen de cualquier erro que 
encuentren en mi codigo

Autor: bechhpz
Fuente: https://github.com/BenchHPZ
Contacto: jijiji
"""


#################
# importaciones ##
###################

import numpy as np
import matplotlib.pyplot as plt





"""
//////////////////////////////////////////////
|||             Prints bonitos              ||
//////////////////////////////////////////////
"""
def show1D(vec,/, max_sz=8, show=False):
    """ Implementacion para pprint vector 1D.
    
    Funcion para generar string para poder imporimir un
    vector de manera reducida, dando un maximo de elementos 
    a imprimir. Lo puede imprimir directamente si se quiere
    
    Input:
        vec := vector de informacion a imprimir.
        [opcionales]
        max_sz := Maximo de elementos a imprimir.
        show := Imprimir vector
        
    _Doctest:
        >>> show1D([1,2,3,4], show=False)
        '1, 2, 3, 4'
        
        >>> show1D([1,2,3,4,5,6,7,8,9], show=False)
        '1, 2, 3, 4, ..., 6, 7, 8, 9'
    """
    n=0
    # En caso de que venga de instancia de np.data
    try:
        shape = vec.shape
        if len(shape) < 2:
            raise Exception('Array 1D')
        else:
            if shape[0] == 1:
                get = lambda i: vec[0,i]
                n = shape[1]
            elif shape[1] == 1:
                get = lambda i: vec[i,0]
                n = shape[0]
            else:
                raise Exception('No arreglo 1D')
    
    except AttributeError:
        get = lambda i: vec[i]
        n = len(vec)
    except Exception as e:
        if e == 'No arreglo 1D':
            print("Error con las dimensiones del array")
    
    ret = '  '
    if n <= max_sz:
        for i in range(n): ret += str(get(i))+', '
    else:
        for i in range(4): ret += str(get(i))+', '
        ret += '..., '
        for i in range(4): ret += str(get(-(4-i)))+', '
    
    ret = ret[2:-2]
    if show: print(ret)
    return ret       


"""
//////////////////////////////////////////////
|||          Creacion de funciones          ||
//////////////////////////////////////////////
"""
def f_polinomio(coef):
    """ Funcion que genera una funcion polinomial de una 
    variable dados sus coeficientes
    
    _Doctest
        >>> (f_polinomio([1,0,0]))(2)
        4
        
        >>> (f_polinomio([1,0]))(123)
        123
    """
    coef = np.ravel(coef)
    grado = len(coef)-1
    
    return lambda x: sum([coef[n]*x**(grado-n) for n in range(grado+1)])



"""
//////////////////////////////////////////////
|||           Manejo de archivos            ||
//////////////////////////////////////////////
"""

def get2Dvec(path,/, dtype=np.float64, info=False):
    """ Funcion para cargar vector 2D.
    
    Esta funcion tratara de cargar un vector 2D de unarchivo
    de texto que tenga dos columnas (correspondientes a dos
    vectores y separada por un espacio) con k filas (donde k
    es el tamanio de los vectores que estan separados por \n)
    
    Los datos los guardaremos en una instancia de np.matrix
    
    Input:
        path := direccion del archivo para cargar los
            vectores
            
        dtype := tipo de dato para usar
        info := Indica si queremos extraer la informacion
    Output:
        (ret, info)
        ret := np.matrix de (2,k)
        info := Para evitar tener que hacer otro recorrido
            sobre el arreglo se puede extraer informacion
            en este recorrido
            minx := El minimo valor de x
            maxx := El maximo valor de x
    """
    
    try:
        if info: #Declarar info
            ret_info = {'minx':  np.Inf,
                        'maxx': -np.Inf}
        
        with open(path, 'r') as file:
            
            ret = [[],[]]
            for line in file:
                line = list(map(lambda x:dtype(x), 
                                line.split(' ')))
                ret[0].append( line[0] )
                ret[1].append( line[1] )
                
                # Extrar info
                if info:
                    # min
                    ret_info['minx'] = min(ret_info['minx'], line[0])
                    # max
                    ret_info['maxx'] = max(ret_info['maxx'], line[0])
        
        if info:
            return np.matrix(ret, dtype=dtype), ret_info
        else:
            return np.matrix(Ret, dtype=dtype)
    except:
        raise Exception("Error al cargar el archivo")

def write2Dvec(path, x, y):
	""" Funcion para escribir 2D vector en un archivo.

	Esta funcion tratara de escribir dos vecrores de 
	dimension 1xn en un archivo. Estos vectores seran
	escritos como columnas y los elementos de cada vector
	estarn separados por espacio. Cada linea estara 
	separada por /n.

	Input:
		path := Direccion al archivo
		x := Primer vector a escribir en archivo
		y := segundo vector a escribir en archivo
	"""
	try:
		with open(path, 'w') as file:
			for i in range(len(x)):
				file.write(f"{x[i]} {y[i]}\n")

	except Exception as e:
		print(e)



"""
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
|||     Basura y prueba de funciones        ||
//////////////////////////////////////////////
"""
def _bch_test_lib_fun():
	print("La nueva libreria esta bien configurada")


def __bch__main():
	_test_lib_fun()



if __name__ == '__main__':

    import doctest
    doctest.testmod()