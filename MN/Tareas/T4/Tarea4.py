#!/usr/bin/env python
# coding: utf-8

# # Tarea 3
# 
# _Tarea 4_ de _Benjamín Rivera_ para el curso de __Métodos Numéricos__ impartido por _Joaquín Peña Acevedo_. Fecha limite de entrega __27 de Septiembre de 2020__.

# ### Como ejecutar

# ##### Requerimientos
# 
# Este programa se ejecuto en mi computadora con la version de __Python 3.8.2__ y con estos
# [requerimientos](https://github.com/BenchHPZ/UG-Compu/blob/master/MN/requerimientos.txt)
# 
# #### Jupyter
# 
# En caso de tener acceso a un _servidor jupyter_ ,con los requerimientos antes mencionados, unicamente basta con ejecutar todas las celdas de este _notebook_. Probablemente no todas las celdas de _markdown_ produzcan el mismo resultado por las 
# [_Nbextensions_](jupyter-contrib-nbextensions.readthedocs.io).
# 
# #### Consola
# 
# Habrá archivos e instrucciones para poder ejecutar cada uno de los ejercicios desde la consola.
# 
# #### Si todo sale mal
# 
# <a href="https://colab.research.google.com/gist/BenchHPZ/813abd96c1dac91b038905ac85cc425c/tarea3.ipynb">
#     <img src="../../../assets/colab-badge.svg" 
#          alt="Open In Colab"/>
# </a>
# 
# En caso de que todo salga mal, tratare de dejar una copia disponible en __GoogleColab__ que se pueda ejecutar con la versión de __Python__ de _GoogleColab_

# In[2]:


usage = """
Programa correspondiente a la Tarea4 de Metodos Numericos. Este
programa espera leer los archivos de tipo npy

Alumno: Benjamin Rivera

Usage:
  Tarea4.py ejercicio1 <matA> <vecB> [--path=<path>]
  Tarea4.py ejercicio2 <matA> <vecB> [--path=<path>]
  Tarea4.py -h | --help

Options:
  -h --help          Show this screen.
  -v --version          Show version.
  --path=<path>   Directorio para buscar archivos [default: data/].
"""

import sys
import scipy
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
from scipy.linalg import solve_triangular

NOTEBOOK = False


# ## Ejercicio 1
# 
# Programar el algoritmo de factorizaci'on $LU$ con pivoteo parcial y probarlo resolviendo un sistema de ecuaciones lineales.
# 

# In[3]:


# Parte 1

def Algoritmo1 (A, n, t,/,dtype=np.float64):
    """ Algoritmo1 de notas de la tarea 
    
    Python dificulta el pase de variables por referencia,
    por lo que regresaremos las matrices L, U y p mediante
    return.
    """
    # Inicializar
    L = np.identity(n, dtype=dtype)
    U = np.copy(A)
    p = [p_i for p_i in range(n)]
    
    for k in range(n):
        # Encuentra pivote
        r = max([r_i for r_i in range(k, n)], 
                key=lambda r_i: abs(U[r_i,k]))
        
        if abs(U[r,k]) < t:
            return 1, None
        
        # Permutacion de matrices
        if r != k:
            # Intercambiar filas k,r
            for j in range(n):                
                U[k,j], U[r,j] = U[r,j], U[k,j]
            
            # Registrar cambio de filas
            p[k], p[r] = p[r], p[k]
            if k > 0:
                # cambio de filas de matriz L
                for j in range(k-1):
                    L[k,j], L[r,j] = L[r,j], L[k,j]
        
        # Reescribir las matrices
        for i in range(k+1, n):
            L[i,k] = U[i,k]/U[k,k]
            for j in range(k, n):
                U[i,j] -= L[i,k]*U[k,j]
                
    return 0, L, U, p

def factLU(A, n, t,/,dtype=np.float64):
    """ Generar factorizacion A=LU con pivoteo parcial
    
    Funcion para hacer la factorizacion LU con pivoteo 
    parcial.
    
    Python dificulta el pase de variables por referencia,
    por lo que regresaremos las matrices L, U y p mediante
    return.
    
        Input:
            A := apuntador a la matriz a factorizar
            n := tamanio n de la matriz
            t := tolerancia de cercania con el 0
            
            dtype := [opcional] Tipo de dato a usar

        Output: ret, L, U, p
            ret := Variable de estado que sera
                0 si se pudo factorizar
                1 si hubo algun problema
            L := Matriz triangular inferior obtenida de
                la descomposicion de A, tamanio nxn
            U := Matriz triangular inferior con tamanio
                nxn de A = LU
            p := vector de permutacion de pivoteo parcial
    """
    sz = A.shape; n = sz[0]
    ret = -1, None, None, None

    # corroboramos las dimensiones
    if sz[0] == sz[1]: #Matriz cuadrada
        ret = 0, None, None, None
    
    # Ejecutamos algoritmo 1
    if ret[0] == 0:
        ret = Algoritmo1(A, n, t, dtype=dtype)
        
    return ret


# In[4]:


# Parte 2

# Para mejor rendimiento usare la implementacion de scipy
#solo hay que tener cuidado porque funciona con numpy.float64
backwardSubstitution = lambda U,b: solve_triangular(U, b, lower=False)
forwardSubstitution = lambda L,b: solve_triangular(L, b, lower=True)


def genSolLU(L, U, n, b, p, t,/, dtype=np.float64):
    """ Generar solucion de LUX = pb 
    
    Funcion que trata de resolver el sistema LUx = Pb, 
    donde L es una matriz triangular inferior y U es una 
    matriz triangular superior.
    
    Debe crear un arraglo $\hat{b} = (\hat{b_1}, \dots,
    \hat{b_n})^T $ con los elementos $ b = (b_1, \dots, 
    b_n)^T$ reordenados de acuerdo al vec $p [\hat{b_1}
    = b_{p_i}]$
    
        Input:
            L := Apuntador a matriz L
            U := Apuntador a matriz U
            n := tamanio de la amtriz
            b := el vactor b
            p := el apuntador a un arreglo de enteros de 
                longitud n
            t := tolerancia de cercania con 0

        Output:
            ret := apuntoador a arreglo de soluciones x.
                En caso de que no se encuentre solucion,
                se devuelve NULL
    """
    pb = np.matrix([b[i,0] for i in p]).transpose() # vector \bar{b}
    # Tratar de resolver LUx = pb
    try:
        # Ly=b (forward)
        y = forwardSubstitution(L, pb)
        # Ux=y (backward)
        x = backwardSubstitution(U, y)
        return x
    
    except Exception as e:
        print(f'Err: {e}')
        # Si la matriz es singular
        return None


# In[5]:


# Parte 3

def solFactLU( A, b,/, t=np.finfo(np.float64).eps, dtype=np.float64):
    """ Resuelve el sistema Ax=b
    
    Esta funcion trata de resolver el sistema de ecuaciones 
    Ax=b usando la factorizacion LU. El ejercicio pide
    crear las matrices LU y el arreglo p pero eso se hace
    en `factLU`.
    
        Input:
            A := Matriz para resolver y factorizar
            b := vector de respuestas
        Output:
            ret := se regresa el vector x respuesta, o None
                en caso de que no haya habido respuestas.
    """
    n = len(A)
    ret, L, U, p = factLU(A, n, t, dtype)
    if ret == 0:
        return genSolLU(L, U, n, b, p, t, dtype)
    else:
        return None


# In[6]:


# Parte 4

def show1D( x,sz,/, max_sz=8, show=True):
    """ Funcion que recibe un arreglo 1D y, en caso de
    que no sea muy grande, lo imprime en pantalla. En
    caso de que lo sea, imprime datos representativos.
        Input:
            x := Apuntador al arreglo 1D para imprimir
            sz := Tamanio del arreglo. (para la imple_
                mentacion en python es inecesario, pe_
                ro lo solicita el ejercicio)
            max_sz := Maximo de elementos a imprimir
            prnt := Indica si el string obtenido se 
                debe imprimir en pantalla
        Output:
            Esta funcion regresa
            
        _Doctest:
            >>> show1D([1,2,3,8,5,6,7,8,9,0], 10, show=False)
            '1, 2, 3, 8, ... , 7, 8, 9, 0'
            
            >>> show1D([1,2,3,8], 4, show=False)
            '1, 2, 3, 8'
    """
    ret = '=('
    
    if sz <= max_sz:
        ret = str(x)[1:-1]
    else:
        mid = max_sz//2
        
        ret = str(x[ :mid])[1:-1]
        ret += ', ... , '
        ret += str(x[-mid:])[1:-1]
    
    if show: print(ret)
    return ret 

def readFile(file,/, path='datos/npy/', ext='.npy', dtype=np.float64):
    """ Funcion para cargar archivos en memoria.
    
    Funcion para cargar los archivos en memoria en el 
    formato que se meustra en el punto 4 del ejercicio 2.
    No lleva el path, ni la extension, solo el nombre del
    archivo. Por default trata de leer los archivos npy
        
        Input:
            file := nombre del archivo sin extension
            path := directorio para buscar el archivo
            ext := extension del archivo a buscar
            dtype := tipo de dato para guardar los valores
    """
    try:
        return np.asmatrix(np.load(file= str(path+file+ext), 
                                   allow_pickle=False),
                          dtype=dtype)
    except:
        raise Exception("Error al encontrar el archivo solicitado.")

def Ejercicio1(matA, vecb,/, path='datosLU/npy/', dtype=np.float64):
    
    A = readFile(matA, path=path, dtype=dtype)
    b = readFile(vecb, path=path, dtype=dtype).transpose()
    
    print(f' Size\n A := {A.shape}, b := {b.shape}')
    
    x = solFactLU(A, b)

    if not isinstance(x, np.ndarray):
        print('La matriz es singular')
    else:
        print('x =>')
        show1D(x, len(x))
        error = np.linalg.norm(A*x-b.transpose()) #Norma de numpy
        print(f'Error =\n     {error}')


# In[7]:


# Parte 5

if NOTEBOOK:    
    for sz in [5, 50, 500]:
        Ejercicio1('matrizA'+str(sz), 'vecb'+str(sz))
        print('\n')


# ## Ejercicio 2
# 
# Programar el algoritmo de \textbf{factorizaci\'on de Cholesky} y resuelva un sistema de ecuaciones lineales.
# 

# In[17]:


# Parte 1

def factChol(A, n, t):
    """ Factorizacion de Cholesky
    
    Funcion que busca calcular la matriz $L$ de la 
    factorizacion de Cholesky.
    
        Input:
            A := Apuntador a matriz A
            n := tamanio de la matriz cuadarada n
            t := Tolerancia con cercania a cero 
        Output:
            L := Matriz L, None si algo salio mal
    """
    try:
        L = np.identity(n)

        for j in range(n):
            L[j,j] = np.sqrt(A[j,j] - sum([L[j,k]**2 for k in range(j)]))

            for i in range(j+1, n):
                L[i,j] = (A[i,j] - sum(L[i,k]*L[j,k] for k in range(j))
                         )/L[j,j]
        return L

    except Exception as e:
        print(f'Error: {e}')

    return None


# In[18]:


# Parte 2

def transpose(M, n):
    """ Calculo de la matriz transpuesta 
        
        _Doctest:
            >>> transpose(np.matrix([[1,2],[3,4]]), 2)
            array([[1, 3],
                   [2, 4]])
    """
    ret = np.copy(M)
    
    for i in range(n):
        for j in range(n):
            ret[j,i] = M[i,j]
        
    return ret


# In[19]:


# Parte 3

def solChol( A, n, b,/, t=np.finfo(np.float64).eps, dtype=np.float64):
    """ Funcion para resolver con Cholesky
    
    Esta funcion recibira una funcion A simetrica y
    positiva. Luego con ella se usara alguna implemen_
    tacion de forwardSubstitution para resolver el
    sistema Ax=b => LL^Tx=b
    
        Input:
            A := Apuntador a matriz A del sistema
            n := tamanio n de matriz A
            b := apuntador a vector b del sistema
            t := tolerancia de similaridad a cero
        
        Output:
            ret := None si algo salio mal, en otro
                caso se regresa el apuntador al 
                vector de respuestas
    """
    L = factChol(A, n, t)
    
    if not isinstance(L, np.ndarray):
        return None
    else:
        return genSolLU(L, L.transpose(), n, b, [i for i in range(n)], t)
        


# In[20]:


# Parte 4
def Ejercicio2(matA, vecB,/, path='datosChol/npy/', dtype=np.float64):
    A = readFile(matA, path=path, dtype=dtype)
    b = readFile(vecB, path=path, dtype=dtype).transpose()
    
    print(f' Size\n A := {A.shape}, b := {b.shape}')
    
    x = solChol(A, len(A), b)

    if not isinstance(x, np.ndarray):
        print('La matriz es singular')
    else:
        print('x =>')
        show1D(x, len(x))
        error = np.linalg.norm(A*x-b.transpose()) #Norma de numpy
        print(f'Error =\n     {error}')


# In[21]:


# Parte 5

if NOTEBOOK:    
    for sz in [5, 50, 500]:
        Ejercicio2('matSim'+str(sz), 'vecb'+str(sz))
        print('\n')


if __name__ == "__main__" and not NOTEBOOK:

    import doctest
    from docopt import docopt
    
    doctest.testmod()
    args = docopt(usage, version='Tarea4, prb')
    
    if len(sys.argv) >= 2:
        if   args['ejercicio1']:
            Ejercicio1(args['<matA>'], args['<vecB>'], args['--path'])
        elif args['ejercicio2']:
            Ejercicio2(args['<matA>'], args['<vecB>'], args['--path'])

