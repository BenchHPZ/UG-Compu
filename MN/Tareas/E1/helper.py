""" Modulo para importar y guardar funciones de otras tareas
para usar en el archivo principal del examen del primer 
parcial. """


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns





def metodo_horner(n, a, x0, dtype=np.float64):
    """ Implementacion del metodo de horner, basado
    en el pseudocodigo del documento de la tarea.
    """

    x0 = dtype(x0)
    # Normalizar el tipo de dato
    a = np.array(a, dtype=dtype, copy=True)
    # Reservar memoria
    b = np.array(a, dtype=dtype, copy=True)

    for k in range(1,n):
        b[k] = a[k] - b[k-1]*x0
    return a[-1]-b[-2]*x0, b



def show1D(vec, max_sz=8, show=False):
    """ Implementacion para pprint vector 1D. """
    n=0
    try: # En caso de que venga de instancia de np.data 
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



def get2Dvec(path,/, dtype=np.float64, info=True):
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

def plot_ej1_1(x, y):
    """ Funcion 1 para graficar resultados. 
    
    Esta funcion buscca graficar los datos recibidos para poder
    tomar la mejor decision respecto al grado a utilizar en la
    aproximacion a polinomios.
    
    Input:
        x := Valores de cordenadas x
        y := Valores de cordenadas y
    """
    fig, ax = plt.subplots()
    sns.scatterplot(x, y, ax=ax)
    plt.show()

def plot_ej1_2(x, y, f, rng):
    """ Funcion 2 para graficar resultados
    
    Esta funcion busca graficar los datos recibidos para mostrar
    la posible eproximacion obtenida por el metodo.
    Input:
        x := Valores de cordenadas x
        y := Valores de cordenadas y
        f := Funcion polinomica obtenida
        rng := particion del rango para graficar
    """
    yf = [f(cx) for cx in rng]
    fig, ax = plt.subplots()
    sns.scatterplot(x, y, ax=ax)
    ax.plot(rng, yf, linestyle= "-")
    plt.show()

def error_ej1(p, x, y):
    """ Funcion para calcular error del polinomio. """
    return sum((p(x[i]) - y[i])**2 for i in range(len(x))) 
    