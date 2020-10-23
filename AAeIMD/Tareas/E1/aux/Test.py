

def search_person(lista, nombre):
    """ Buscar persona en lista de personas. 
    
    Buscamos un nombre en una lista de instancias
    de la clase Person. 
    
    En caso de que se encuentre regresamos su
    indica, en otro caso regresamos -1
    
    Hay que tener cuidado con este valor porque
    -1 es un valor que se puede pasar como indice,
    pero esta funcon lo regresa como indicador
    de que no encontro lo que se buscaba
    """
    if nombre != None:
        for i in range(len(lista)):
            if lista[i].nombre == nombre:
                return i
    return -1  
  

    
if __name__ == '__main__':
    print("Esto es un modulo auxiliar")

