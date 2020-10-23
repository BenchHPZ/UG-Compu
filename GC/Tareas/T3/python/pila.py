
from ordered_set import OrderedSet
import numpy as np



class Nodo(object):
	""" Objeto estandar de nodo. """
	
	def __init__(self, root, name):
		self.data = None
		self.root = root
		self.name = name
		self.sons = OrderedSet()

	# Getters de nodo
	def get_sons(self):
		return self.sons
	def get_name(self):
		return self.name
	def get_root(self):
		return self.root
	def get_data(self):
		return self.data

	# Setters de Nodo
	def set_data(self, data):
		self.data = data
	def set_root(self, root):
		self.root = root
	def set_sons(self, list_sons):
		self.sons = list_sons 

	# Funciones para nodos hijo
	def add_son(self, node_name):
		""" Funcion para agregar un nodo hijo. """
		self.sons.add(node_name)
	def get_son(self, index=0):
		""" Funcion para obtener nodo por index. """
		return self.sons[index]
	def remove_son(self, node_name, prnt=True):
		""" Funcion para quitar nodo por nombre. """
		try:
			self.sons.remove(node_name)
			return True
		except KeyError:
			if prnt: print(f'{node_name} no esta en sons')
			return False






class NodoTransformacion(Nodo):
	""" Nodo de transformacion"""
	dtype = np.float16

	def __init__(self, arg):

		Nodo.__init__(self, root, name)
		self.data = np.identity(4, dtype=dtype)

	def rotacion(self, tetax, tetay, tetaz):
		pass

	def traslacion(self, deltax, deltay, deltaz):
		pass

	def escalamiento(self, deltax, deltay, deltaz):
		pass

	def 


class NodoObjeto(Nodo):
	""" Nodo para guardar objeto grafico.

	Nodo heredaro donde se busca almacenar objetos
	que se deban imprimir de alguna forma.
	"""
		



class PilaTransformaciones(object):
	"""docstring for PilaTransformaciones"""

	def __init__(self):
		self.root = "Fin"
		
