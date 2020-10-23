# Pygame
import pygame as pg
from pygame.locals import *
# PyOpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Librerias creadas con funcionalidades
from iluminacion import *



if True:
	CABEZA_ALTO      = 1
	CABEZA_RADIO     = 1

	TORSO_ALTO       = 1
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
	glScalef(CABEZA_RADIO, CABEZA_ALTO, CABEZA_RADIO)
	glRotatef(45, 0, 1, 0)
	glutSolidSphere(1, SLICES, STACKS)
	glutSolidTeapot(1.0)
	glPopMatrix()

def torso():
	glPushMatrix()
	#glRotatef(90.0, 1.0, 0, 0)
	glScalef(TORSO_RADIO/2, TORSO_ALTO, TORSO_RADIO)
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
	# Centramos en pantalla
	glScalef(0.2, 0.2, 0.5)

	torso()
	glPushMatrix()
	if True: # Cabeza
		glTranslatef(0, CABEZA_ALTO+TORSO_ALTO, 0)
		cabeza()
	glPopMatrix()
	glPushMatrix()
	if True: # Brazo derecho
		glTranslatef(-TORSO_RADIO, 0, 0)
		glRotatef(bsd, 0, 0, 1)
		brazo_sup_der()
		glTranslatef(-BRAZO_SUP_ALTO, 0, 0)
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



def mostrar():
	# Buffer posterior
	glDrawBuffer(GL_BACK) 

	# Limpiar pantalla
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);


	# Mover camara
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

	dibujar_pupete(0, 0, 0, 
				   0, 0, 0, 0, 
				   0, 0, 0, 0)

	glFlush()


def init():

	# Fondo blanco
	#glClearColor(1.0, 1.0, 1.0, 1.0)

	iluminacion()


def main():
	# Init glut para figuras sin apuntadores
	glutInit(sys.argv)

	# Init de pygame para ventanas, botones y UI
	pg.init()

	# Crear pantallar
	sz_display = (800, 650)
	pg.display.set_mode(sz_display, DOUBLEBUF|OPENGL)

	init()
	#iluminacion()
	

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