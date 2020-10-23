#!/usr/bin/env python
# coding: utf-8

# # Tarea 3
# 
# _Tarea 3_ de _Benjamín Rivera_ para el curso de __Métodos Numéricos__ impartido por _Joaquín Peña Acevedo_. Fecha limite de entrega __20 de Septiembre de 2020__.

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
# <a href="https://colab.research.google.com/gist/BenchHPZ/...">
#     <img src="../../../assets/colab-badge.svg" 
#          alt="Open In Colab"/>
# </a>
# 
# En caso de que todo salga mal, tratare de dejar una copia disponible en __GoogleColab__ que se pueda ejecutar con la versión de __Python__ de _GoogleColab_

# In[9]:


# Init cell
import sys
import numpy as np
import matplotlib.pyplot as plt

notebook = False

if notebook:
    print("Todo bien con la importacion xD")


# ## Ejercicio 1

# ### .
# 
# Muestre que la inversa de $L_k$ es $L^{-1}_k = I + l_ke_k^T$. Asi, la inversa de una matriz triangular inferior elemental es otra matriz triangular inferior elemental. 

# Sabemos que, si la matriz es invertible, entonces $L_kL_k^{-1} = I$. 
# 
# Procedemos por contradiccion. Supongamos que $L^{-1}_k \neq I + l_ke_k^T$, de manera que $L_k(I + l_ke_k^T) \neq I$; si desarrolamos lo anterior resulta que
# 
# \begin{eqnarray*}
#     L_k(I + l_ke_k^T) &\neq& I \\
#     (I - l_ke_k^T)(I + l_ke_k^T) &\neq& I \\
#     I^2 - (l_ke_k^T)^2 &\neq& I \\
#     I - (l_ke_k^T)^2 &\neq& I \\ 
# \end{eqnarray*}
# 
# lo cual es cierto siempre que $(l_ke_k^T)^2 \neq \bar{0}$. Sin embargo, por la manera en que estan definidas $l_ke_k^T$, $(l_ke_k^T)^2 = 0$. Por lo que llegamos auna contradicion y $L^{-1}_k = I + l_ke_k^T$.
# 

# ### .
# 
# Muestre que $L^{-1}_{k-1}L^{-1}_k = I + l_{k-1}e^T_k + l_ke^t_k$ y con esto demostrar que 
# 
# \begin{equation*} L = L^{-1}_1 L^{-1}_2 \dots L^{-1}_{n-1} = I + \sum_{k=1}^{n-1}l_ke_k^T
# \end{equation*}
# 
# por lo que $L$ es una matriz triangular inferior con 1's en la diagonal
# 

# \textbf{Parte 1} Por definicion y el punto anterior
# 
# \begin{eqnarray*}
#     L_{k-1}^{-1}L_{k}^{-1} &=& (I + l_{k-1}e_{k-1}^T)(I + l_ke_k^T) \\
#         &=& I^2 + l_{k-1}e_{k-1}^T(l_ke_k^T) + l_{k-1}e_{k-1}^T + l_ke_k^T \\
#         &&\text{y como sabemos que la multiplicacion de las submatrices $l,e$ es 0} \\
#         &=& I + \bar{0} + l_{k-1}e_{k-1}^T + l_ke_k^T \\
#         &=& I + l_{k-1}e_{k-1}^T + l_ke_k^T 
# \end{eqnarray*}
# 
# \textbf{Parte 2} ...

# ## Ejercicio 2

# In[2]:


def show1D( x,sz,/, max_sz=8, prnt=True):
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
            >>> show1D([1,2,3,8,5,6,7,8,9,0], 10, prnt=False)
            '1, 2, 3, 8, ... , 7, 8, 9, 0'
            
            >>> show1D([1,2,3,8], 4, prnt=False)
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
    
    if prnt: print(ret)
    return ret       


# In[3]:


def forwardSubstitution( L, n, b, t,/,dtype=np.float64):
    """ Funcion que implementa el metodo desustitucion pa_
    ra adelante dada una matriz triangular inferior.
        Input:
            L := apuntador a la matriz L
            n := tamanio de la matriz L
            b := apuntador al vector b
            t := tolerancia de 0's
        Otput:
            ret := vector x de respuestas si se encontro, o
                None en caso de que hay habido algun error
                
        _Doctest:
            >>> forwardSubstitution(np.matrix([[1,0],[0,1]]), 1, np.matrix([[3,4]]), 0.1)
            matrix([[3.],
                    [4.]])
    """

    if len(L) == b.size:
        n = len(L)
        # verificamos que la matriz tenga solucion
        for i in range(n):
            if abs(L[i,i]) <= t:
                print("Err: 0 o casi cero en diagonal")
                return None
        
        x = np.zeros((n), dtype=dtype)
        for i in range(n):
            x[i] = (b[0,i] - np.sum([L[i,j]*x[j] for j in range(i)],
                                    dtype=dtype)
                   )/L[i,i]

        return np.asmatrix(x, dtype=dtype).transpose()
    
    else:
        print("Err: dimensiones")
        return None


# In[4]:


def readFile(file,/, path='datos/npy/', ext='.npy', dtype=np.float64):
    """ Funcion para cargar los archivos en memoria en el 
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
        
def Ejercicio2(f_L, f_b):
    """ Programa para ejecutar el ejercicio 2. espera el nombre
    de los archivos de la matriz y el vector soluciones para 
    funcionar.
    """
    L = readFile(f_L)
    b = readFile(f_b)
    dtype = np.float64
    t = (2.2e-16)**(2/3) # De la tarea 1 y como estamos usando flaot64
    
    print(len(L), b.size)
    
    x = forwardSubstitution(L, len(L), b, t, dtype=dtype)
    
    if not x is None:
        show1D(x, len(x))
        error = np.linalg.norm(L*x-b.transpose()) #Norma de numpy
        print(f'Error =\n {error}')
    else:
        print("El sistema no tiene solucion.\nY es singular.")


if notebook:    
    for sz in [5, 50, 500]:
        Ejercicio2('matL'+str(sz), 'vecb'+str(sz))
        print('\n')


# #### Como ejecutar
# Para ejecutar en consola se necesita estar en el mismo directorio que la carpeta de la tarea `datos`. Como nombre de los archivos no se espera la direccion completa ni la extension del archivo. Se infiere automatincamente que los datos sera obtenidos del subdirectorio `datos/npy` y con la extension `.npy`. De manera qu la ejecucion debe parecerse a lo siguiente
# ```console
# $ python3 Tarea3.py matL5 vecb5
# ```
# 
# #### Otros
# [Norma de Numpy](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html)

# ## Ejercicio 3

# In[5]:


def backwardSubstitution( U, n, b, t,/,dtype=np.float64):
    """ Funcion que implementa el metodo desustitucion pa_
    ra atras dada una matriz triangular inferior.
        Input:
            U := apuntador a la matriz U
            n := tamanio de la matriz U
            b := apuntador al vector b
            t := tolerancia de 0's
        Otput:
            ret := vector x de respuestas si se encontro, o
                None en caso de que hay habido algun error
                
    """
    
    if len(U) == b.size:
        n = len(U)
        
        # verificamos que la matriz tenga solucion
        for i in range(n):
            if abs(U[i,i]) <= t:
                print("Err: 0 o casi cero en diagonal")
                return None
        
        x = np.zeros((n), dtype=dtype)
        for i in range(n-1, -1, -1):
            x[i] = (b[0,i] - np.sum([U[i,j]*x[j] for j in range(i+1-1, n)],
                                    dtype=dtype)
                   )/U[i,i]

        return np.asmatrix(x, dtype=dtype).transpose()
    
    else:
        print("Err: dimensiones")
        return None


# In[8]:


def Ejercicio3(f_U, f_b):
    """ Programa para ejecutar el ejercicio 3. espera el nombre
    de los archivos de la matriz y el vector soluciones para 
    funcionar.
    """
    U = readFile(f_U)
    b = readFile(f_b)
    dtype = np.float64
    t = (2.2e-16)**(2/3) # De la tarea 1 y como estamos usando flaot64
    
    print(len(U), b.size)
    
    x = backwardSubstitution(U, len(U), b, t, dtype=dtype)
    
    if not x is None:
        show1D(x, len(x))
        error = np.linalg.norm(U*x-b.transpose()) #Norma de numpy
        print(f'Error =\n {error}')
    else:
        print("El sistema no tiene solucion.\nY es singular.")


if notebook:    
    for sz in [5, 50, 500]:
        Ejercicio3('matU'+str(sz), 'vecb'+str(sz))
        print('\n')
        
        
        
if __name__ == "__main__" and not notebook:
    import doctest
    doctest.testmod()
    
    if len(sys.argv) >= 2:
        ejercicio = sys.argv[1].lower()

        if ejercicio == 'ejercicio2':
            Ejercicio2( sys.argv[2], sys.argv[3])
        elif ejercicio == 'ejercicio3':
            Ejercicio3( sys.argv[2], sys.argv[3])
        else:
            print(')= ... =(')

