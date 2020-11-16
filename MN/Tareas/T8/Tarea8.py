#!/usr/bin/env python
# coding: utf-8

# # Tarea 8
# 
# _Tarea 8_ de _Benjamín Rivera_ para el curso de __Métodos Numéricos__ impartido por _Joaquín Peña Acevedo_. Fecha limite de entrega __1 de Noviembre de 2020__.

# In[1]:



import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as LA
import scipy as sp
import seaborn as sns

from scipy.linalg import solve_triangular # Para backward y forward substitution
from scipy.linalg import svdvals


NOTEBOOK = True


# ## Ejercicio 1
# 
# Programar y probar el método de descomposición en valores singulares. Anque algoritmo permite factorizar una matriz rectangular, el programa se va a probar con matrices cuadradas para revisar su número de condición y el uso de la factorización para resolver sistemas de ecuaciones.

# ### Implementar Algoritmo 1
# 
# Escriba una función que implemente el Algoritmo 1 para obtener las matrices U, V y el arreglo s de la descomposición en valores singulares de una matriz A.

# In[2]:


def reordenar_matriz(mat, orden):
    if type(mat) == np.matrix:
        return np.concatenate([mat[:, i] for i in orden],
                              axis=1)
    else:
        return [mat[i] for i in orden]
        

def ordenar(M1: np.matrix, M2: np.matrix, v: list) -> tuple:
    """ Funcion para reordenar las columnas de las
    matrices como se pide en Algoritmo 1.
    """
    # Buscamos el orden en funcion de s O(nlog n)
    orden = [i for i in range(len(v))]
    orden.sort(key=lambda i: v[i],
               reverse=True)
    # -------------------------------
    # Reordenamos los recibidos O(3n)
    M1 = reordenar_matriz(M1, orden)
    M2 = reordenar_matriz(M2, orden)
    v = reordenar_matriz(v, orden)
    # --------------------------
    # Regresamos los reordenados
    return M1, M2, v


if NOTEBOOK and True:
    """ Parte para probar el uso de ordenar. """
    n = 3
    U = np.matrix(np.random.rand(n, n), dtype=np.float16)
    V = np.matrix(np.random.rand(n, n), dtype=np.float16)
    s = list(np.random.rand(1, n).flatten())
    print(U, end='\n\n')
    print(V, end='\n\n')
    print(s, end='\n\n')

    print('-'*n*12)
    U, V, s = ordenar(U, V, s)
    print(U, end='\n\n')
    print(V, end='\n\n')
    print(s, end='\n\n')


# In[3]:


def Algoritmo1(A: np.matrix, m: int, n: int, T=None, N=100, dtype=np.float64):
    """ Descomopsocion en valores singulares. 
    
    Input:
        A := Matriz de mxn con columnas $a_i, i\in [0,n]$
    """
    # En caso de no pasar tolerancia lo ponemos al epsilon del tipo de dato
    if T is None:
        T = np.finfo(dtype).eps ** (1 / 2)

    if not isinstance(A, np.matrix):
        try:
            A = np.matrix(A)
        except:
            raise Exception("=( nshe k pz")

    # Inicializar valores
    V = np.matrix(np.identity(n), 
                  dtype=dtype)
    k = 0
    F = 1

    while k < N and F > 0:
        k = k+1
        F = 0
        for i in range(n-1):
            for j in range(i+1, n):
                alpha = dtype(A[:, i].transpose()*A[:, i])
                gamma = dtype(A[:, j].transpose()*A[:, j])
                beta  = dtype(A[:, i].transpose()*A[:, j])

                if alpha*gamma > np.finfo(dtype).eps and abs(beta) > T*alpha*gamma:
                    F = 1
                    if beta != 0:
                        nu = (gamma - alpha)/(2*beta)
                        t = 1/(abs(nu) + np.sqrt(1 + nu**2))
                        if nu < 0:
                            t = -t
                        c = 1/np.sqrt(1 + t**2)
                        s = t*c
                    else:
                        c = 1
                        s = 0
                    
                    # Modificacion de A
                    a = A[:, i]
                    b = A[:, j]
                    
                    A[:, i] = c*a - s*b
                    A[:, j] = s*a + c*b

                    # Modificacion de V
                    a = V[:, i]
                    b = V[:, j]
                    
                    V[:, i] = c*a - s*b
                    V[:, j] = s*a + c*b
    
    s = []
    for j in range(n):
        s.append(LA.norm(A[:, j].flatten()
                         , 2))

    A, V, s = ordenar(A, V, s)
    
    U = np.matrix(np.zeros((m, n)),
                  dtype=dtype)
    for j in range(n):
        U[:, j] = A[:, j]/s[j]

    return U, V, s


# ### Funcion de solucion
# 
# Escriba una función que calcule una aproximación de la solución del sistema $Ax = b$ usando la descomposición en valores singulares de la siguiente manera. La función recibe las matrices $U$ y $V$ , el arreglo $s$ con los valores singulares (calculados con la funcion del inciso anterior), su tamaño n (por matrices cuadradas) y un ı́ndice k. La función debe devolver el vector
# $$
#     x = \sum_{i=1}^k \frac{u_i^T b}{s_i} v_i
# $$
# donde $u_i, v_i$ son los i-esimas columnas de las matrices $U, V$ (correpondientemente).
# 
# #### Nota
# 
# Dado que la expresion requiere del vector $b$, que es el vector de terminos dependientes del sistema, este tambien sera pasado a la funcion a pesar de que no se pido en el enunciado. Hay que tener cuidado con sus dimensiones.

# In[35]:


def aproximacion_solucion(U: np.matrix, V: np.matrix, s: list, 
                          b: np.matrix, n: int, k: int):
    return sum([ ((b*U[:,i].transpose())
                  /s[i])*V[:, i] 
               for i in range(k)])


# ### Interfaz 1
# 
# Escriba un programa que reciba desde la lı́nea de comandos el nombre de un archivo que contiene una matriz.
# 
# Lea el archivo para crear la matriz $A$ y use la función del primer inciso para calcular su descomposición en valores singulares tomando $\tau = \sqrt{\epsilon_m}$
# 
# Imprima la siguiente información:
#  1. Dimensiones $m, n$
#  2. El valor del error de la ortogonalidad de $U$, $||I - U^TU||$
#  3. El valor del error de la ortogonalidad de $V$, $||I - V^TV||$
#  4. Crear la matriz $S$ con $s$ en su diagonal e imprimir $||A - USV^T ||$.
#  5. El numero de condicion de la matriz $k_2 = \frac{s_1}{s_n}$
#  
# Puede eligir la norma matricial para calcular los errores.

# In[5]:


def load_matrix(file_name: str, 
                path = "datos/", ext=".npy", 
                dtype=np.float64) -> np.matrix:
    """ Funcion para cargar una matriz de un archivo. """
    if ext == ".npy":
        return np.matrix(np.load(path+file_name+ext, 
                                 allow_pickle=True),
                         dtype=dtype)
    
    else:
        """ Sin fomato especifico, esperamoe esta en texto
        con condificacion estandar 'utf-8' e iran siendo 
        ingresados como fuera de esperarse.
        """
        return np.matrix(np.loadtxt(path+file_name+ext),
                         dtype=dtype)


# In[6]:


def proceso( file_name: str, path = "datos/", ext=".npy", show=True):
    lon = 100
    dtype = np.float64
    
    # Cargar matriz
    A = load_matrix(file_name, path, ext, 
                    dtype=dtype)
    szA = A.shape
    # Descomposicion
    U, V, s = Algoritmo1(A, szA[0], szA[1])
    
    I = np.identity(szA[1])
    # Errores ortogonalidad
    errU = LA.norm( I - U.transpose()*U)
    errV = LA.norm( I - V.transpose()*V)
    
    # Error de la factorizacion
    S = np.diag(s)
    errS = LA.norm( A - U*S*V.transpose())
    
    # Condicion de matrix
    k2 = s[1]/s[-1]
    
    if show:
        print('-'*lon)
        print(f"Dimensiones\n\t m={szA[0]}, n={szA[1]}")
        print(f"Errores ortogonaldad")
        print(f"\t U -> {errU}")
        print(f"\t V -> {errV}")
        print(f"Error factorizacion")
        print(f"\t s -> {s}")
        print(f"\t S -> {errS}")
        print(f"Condicion de matriz\n\t {k2}")
        print('-'*lon)
    
    return U, V, s


# In[7]:


if NOTEBOOK:
    U, V, s = proceso('matA5')
    S = np.diag(s)
    A = U*S*V.transpose()
    print(A)
    print(svdvals(A))


# Aqui note que no esta funcionando mi Algoritmo 1, creo que el problema esta en el calculo de la norma. Cuando este resultado es comparado contra las funciones implementadas en nmumpy, los valores difieren por mucho.

# ### Pruebas
# 
# Genere el vector $x$ que tiene sus entradas iguales a $1$ y calcule el vector $b = Ax$.
# 
# Use la función del inciso 2 para calcular la solución $x_1$ del sistema de ecuaciones
# usando $k = n$. Imprima las primeras y últimas entradas del vector $x_1$ y reporte el
# error $||x − x_1||$ y $||Ax_1 − b||$.

# In[44]:


if NOTEBOOK:
    n = 5
    file_name = 'matA' + str(n)
    
    A = load_matrix(file_name)
    U, V, s = proceso(file_name)
    
    x = np.matrix([1 for n in range(n)]).transpose()
    b = A*x
    
    print(b)
    sol = aproximacion_solucion(U, V, s, b, n, n)
    print(sol)
    print(LA.norm(x - sol))
    print(LA.norm(A*sol - b))
    
    eps = np.finfo(float).eps
    ks = ([k for k in range(len(s)-1)
          if s[k] > eps**(2/3) and s[k+1] <= eps**(2/3)])
    sol2 = aproximacion_solucion(U, V, s, b, n, ks)
    print(sol2)
    print(LA.norm(x - sol))
    print(LA.norm(A*sol - b))


# In[ ]:




