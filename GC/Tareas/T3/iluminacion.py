""" Modulo para manejar la iluminacion de la escena """

from OpenGL.GL import *


def iluminacion():
	""" Funcion para definir y configurar las preferencias
	de iluminacion en el ambiente.

	Los valores fueron robados de un codigo de prueba que 
	ya no pude volver a encontrar. Luego los movi un poco
	para llegar a lo que son ahora.
	"""
	# Propiedades del material
	mat_specular =  (0.5, 0, 0, 1.0)
	mat_diffuse  =  (0.5, 0, 0, 1.0)
	mat_ambient  =  (0.5, 0, 0, 1.0)
	mat_shininess = (6.0)

	# Propiedades de iluminacion
	light_ambient =( .5, .0, .0, 1.0)
	light_diffuse =( .5, .0, .0, 1.0)
	light_specular =( .7, .0, .0, 1.0)
	light_position =( 100.0, 80.0, 120.0 , 1.0)

	# Definir propiedades de ambiente para light0
	glLight(GL_LIGHT0, GL_AMBIENT, light_ambient)
	glLight(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
	glLight(GL_LIGHT0, GL_SPECULAR, light_specular)
	glLight(GL_LIGHT0, GL_POSITION, light_position)

	# Definir propiedades para los materiales
	glMaterial(GL_FRONT, GL_SPECULAR, mat_specular)
	glMaterial(GL_FRONT, GL_AMBIENT, mat_ambient)
	glMaterial(GL_FRONT, GL_DIFFUSE, mat_diffuse)
	glMaterial(GL_FRONT, GL_SHININESS, mat_shininess)

	glShadeModel(GL_SMOOTH)      # smooth shading
	glEnable(GL_LIGHTING)    # iluminacion
	glEnable(GL_LIGHT0)      # activar light0
