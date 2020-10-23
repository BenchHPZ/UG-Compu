import pygame as pg

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

if True:
	CABEZA_ALTO      = 1
	CABEZA_RADIO     = 1

	TORSO_ALTO       = 2
	TORSO_RADIO      = 1

	BRAZO_SUP_ALTO   = 1
	BRAZO_SUP_RADIO  = 0.5
	BRAZO_INF_ALTO   = 1
	BRAZO_INF_RADIO  = 0.5

	PIERNA_SUP_ALTO  = 1
	PIERNA_SUP_RADIO = 0.5
	PIERNA_INF_ALTO  = 1
	PIERNA_INF_RADIO = 0.5

	SLICES = 10
	STACKS = 10


		


def cabeza():
	glPushMatrix()
	glScalef(CABEZA_RADIO, CABEZA_ALTO/2, CABEZA_RADIO)
	glRotatef(45, 0, 1, 0)
	glutSolidTeapot(1.0)
	glPopMatrix()

def torso():
	glPushMatrix()
	glRotatef(90.0, 1.0, 0, 0)
	glScalef(TORSO_RADIO/2, TORSO_ALTO/2, TORSO_ALTO)
	glutSolidSphere(1, SLICES, STACKS)
	glPopMatrix()

def brazo_sup_izq():
	glPushMatrix()
	glRotatef(-90, 0, 1, 0)
	glScalef(BRAZO_SUP_RADIO, BRAZO_SUP_ALTO/2, BRAZO_SUP_RADIO)
	glutSolidSphere(1, SLICES, STACKS)
	glPopMatrix()


def brazo_inf_izq():
	glPushMatrix()
	glRotatef(-90, 0, 1, 0)
	glScalef(BRAZO_INF_RADIO, BRAZO_INF_ALTO/2, BRAZO_INF_RADIO)
	glutSolidSphere(1, SLICES, STACKS)
	glPopMatrix()

def brazo_sup_der():
	glPushMatrix()
	glRotatef(-90, 0, 1, 0)
	glScalef(BRAZO_SUP_RADIO, BRAZO_SUP_ALTO/2, BRAZO_SUP_RADIO)
	glutSolidSphere(1, SLICES, STACKS)
	glPopMatrix()

def brazo_inf_der():
	glPushMatrix()
	glRotatef(-90, 0, 1, 0)
	glScalef(BRAZO_INF_RADIO, BRAZO_INF_ALTO/2, BRAZO_INF_RADIO)
	glutSolidSphere(1, SLICES, STACKS)
	glPopMatrix()

def pierna_sup_izq():
	glPushMatrix()
	glRotatef(-90, 1, 0, 0)
	glScalef(PIERNA_SUP_RADIO, PIERNA_SUP_ALTO/2, PIERNA_SUP_RADIO)
	glutSolidSphere(1, SLICES, STACKS)
	glPopMatrix()

def pierna_inf_izq():
	glPushMatrix()
	glRotatef(-90, 1, 0, 0)
	glScalef(PIERNA_INF_RADIO, PIERNA_INF_ALTO/2, PIERNA_INF_RADIO)
	glutSolidSphere(1, SLICES, STACKS)
	glPopMatrix()

def pierna_sup_der():
	glPushMatrix()
	glRotatef(90, 1, 0, 0)
	glScalef(PIERNA_SUP_RADIO, PIERNA_SUP_ALTO/2, PIERNA_SUP_RADIO)
	glutSolidSphere(1, SLICES, STACKS)
	glPopMatrix()

def pierna_inf_der():
	glPushMatrix()
	glRotatef(90, 1, 0, 0)
	glScalef(PIERNA_INF_RADIO, PIERNA_INF_ALTO/2, PIERNA_INF_RADIO)
	glutSolidSphere(1, SLICES, STACKS)
	glPopMatrix()

def dibujar_pupete(x, y, z, # Posicion absoluta
	               bsi, bii, bsd, bid,  #Angulos de brazos
	               psi, pii, psd, pid): #Angulos de piernas
	""" Funcion para dibujar el cuerpo completo.
	
	Las sentencias de control if son incesesarias pero ayudan
	a tener una mejor visualizacion de la estructura generada.
	"""
	glScalef(0.2, 0.2, 0.5)
	torso()
	
	glPushMatrix()
	if True: # Cabeza
		glTranslatef(0, TORSO_ALTO, 0)
		cabeza()
	glPopMatrix()
	'''
	glPushMatrix()
	if True: # Brazo derecho
		glTranslatef(-TORSO_RADIO, 0, 0)
		glRotatef(bsd, 0, 0, 1)
		brazo_sup_der()
		glTranslatef(BRAZO_SUP_ALTO, 0, 0)
		glRotatef(bid, 0, 0, 1)
		brazo_inf_der()
	glPopMatrix()
	glPushMatrix()
	if True: # Brazo izquierdo
		glTranslatef(TORSO_RADIO, 0, 0)
		glRotatef(bsi, 0, 0, 1)
		brazo_sup_izq()
		glTranslatef(BRAZO_SUP_ALTO, 0, 0)
		glRotatef(bii, 0, 0, 1)
		brazo_inf_izq()
	glPopMatrix()
	glPushMatrix()
	if True: # Pierna derecha
		glTranslatef(-TORSO_RADIO, -TORSO_ALTO, 0);
		glRotatef(psd, 1, 0, 0);
		pierna_sup_der();
		glTranslatef(0, -PIERNA_SUP_ALTO, 0);
		glRotatef(pid, 1, 0, 0);
		pierna_inf_der();
	glPopMatrix()
	glPushMatrix()
	if True: # Pierna izquierda
		glTranslatef(TORSO_RADIO, -TORSO_ALTO, 0);
		glRotatef(psi, 1, 0, 0);
		pierna_sup_izq();
		glTranslatef(0, -PIERNA_SUP_ALTO, 0);
		glRotatef(pii, 1, 0, 0);
		pierna_inf_izq();
	glPopMatrix()
	'''

def iluminacion():
	# Propiedades del material
	mat_specular =  (0.7, 0, 0, 1.0)
	mat_diffuse  =  (0.5, 0, 0, 1.0)
	mat_ambient  =  (0.5, 0, 0, 1.0)
	mat_shininess = (7.0)

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

def mostrar():
	# Buffer posterior
	glDrawBuffer(GL_BACK) 

	# Limpiar pantalla
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);


	# Mover camara
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	#gluLookAt(eye[0], eye[1], eye[2], at[0], at[1], at[2], 0, 1, 0)
	"""
	glRotatef(xRotate, 0, 1, 0);
	glRotatef(yRotate, 1, 0, 0);
	"""
	# Cambiar estos valores para mover todo
	dibujar_pupete(0, 0, 0, 
					0, 0, 0, 0, 
					0, 0, 0, 0)

	glFlush()
	#glutSwapBuffers()


def init():

	glClearColor(1.0, 1.0, 1.0, 1.0)

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(60, 1, 1, -10)

	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(0,0,20,
		      0,0,0,
		      0,1,0)

	glEnable(GL_DEPTH_TEST)
	iluminacion()

def main():
	# Init glut para figuras sin apuntadores
	glutInit(sys.argv)

	# Init de pygame para ventanas, botones y UI
	pg.init()

	# Crear pantallar
	sz_display = (800, 650)
	pg.display.set_mode(sz_display, DOUBLEBUF|OPENGL)

	#init()
	

	while True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				quit()

		mostrar()

		pg.display.flip()
		pg.time.wait(10)


if __name__ == '__main__':
	main()