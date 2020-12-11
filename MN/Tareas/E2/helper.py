def romberg_iterativo(f, i, lim):
    """ Funcion para ejecutar el metodo de Romberg iterativo. 
    
    Esta funcion trata de ejecutar el metodo de Romberg iterativo 
    con un acercamiento iterativo. Regresara el valor calculado, 
    con la condicion de termino i == 0 donde no se llamara a si 
    misma de nuevo.
    
    Para que esta funcion sea un poco mas "pythonica" no pediremos 
    el valor previo del metodo y lo calcularemos de manera interna
    con el enfoque recursivo. 
    Claramente este no es el metodo que se explica en la tarea,
    pero el otro se me revolvio y este funciona (aunque algo lento)
    
    Input:
        f := funcion para aproximar integral
        i := iteracion del metodo
        lim := tupla de limites de la evaluacion
    
    Regresa el valor de R(i,0), un flotante.
    """
    
    try:
        a, b = lim
    except TypeError:
        raise Exception("Err: lim debe contener valores (a,b)")

    if i == 0:
        return ((b-a)/2)*(f(a) + f(b))
    else:
        h = (b-a)/(2**i)
        r_im1 = romberg_iterativo(f, i-1, lim)
        
        suma = 0
        for k in range(1, 2**(i-1)+1):
            suma += f(a + (2*k - 1)*h)
        
        return 0.5*r_im1 + h*suma
    
    
def regla_trapecio_iterativa(f, i, r_im1, lim):
    """ Funcion para ejecutar la regla del trapecio. 
    
    Esta funcion trata de ejecutar la regla del trapecio mediante
    un acercamiento iterativo. Regresara el valor calculado, con
    la condicion de termino i == 0 donde no se llamara a si misma
    de nuevo.
    
    Este es mi intento de implementacion de la funcion solicitada
    en la tarea. Algo que no se solicita en la tarea pero que si
    se pide en la funcion, son los limites de integracion.
    
    Input:
        f := funcion para aproximar integral
        i := iteracion del metodo
        rim1 := Evaluacion de la regla en la iteracion anterior.
        lim := tupla de limites de la evaluacion
    
    Regresa el valor de R(i,0), un flotante.
    """
    try:
        a, b = lim
    except TypeError:
        raise Exception("Err: lim debe contener valores (a,b)")

    if i == 0:
        return ((b-a)/2)*(f(a) + f(b))
    else:
        h = (b-a)/(2**i)
        suma = 0
        for k in range(1, 2**(i-1)+1):
            suma += f(a + (2*k - 1)*h)
        
        return 0.5*r_im1 + h*suma
    
    
def romberg_matricial(f, n, lim):
    """Funcion para ejecutar el metodo de Romberg iterativo. 
    
    Esta funcion trata de ejecutar el metodo de Romberg con la 
    ayuda de una matriz para guardar las iteraciones del mismo. 
    Regresara la matriz calculada de las iteraciones.
    
    Input:
        f := funcion para aproximar integral
        n := profundidad de iteracion del metodo
        lim := tupla de limites de la evaluacion
    
    Regresara la matriz calculada con las iteraciones.
    """
    # Preparacion de datos
    try:
        a, b = lim
    except TypeError:
        raise Exception("Err: lim debe contener valores (a,b)")
    n += 1
    # init matriz
    matriz_romberg = np.zeros((n,n))
    
    for i in range(n):
        matriz_romberg[i, 0] = regla_trapecio_iterativa(f, i, 
                                                        matriz_romberg[i-1, 0], 
                                                        lim)
        
    for j in range(1, n):
        for i in range(n):
            matriz_romberg[i,j] = (matriz_romberg[i, j-1] 
                                   + 1/(4**j - 1)
                                   * (matriz_romberg[i, j-1] 
                                      - matriz_romberg[i-1, j-1])
                                  )
    
    return matriz_romberg
