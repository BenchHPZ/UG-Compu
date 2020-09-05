
// Libreria principal
# include <GLFW/glfw3.h>


int main( void ){

// Creacion de ventana
	// Apuntador para ventana
	GLFWwindow* ventana;
	if( !glfwInit() ) return -1;

	// Variables de tamanio de ventana
	int ancho, alto;
	ancho = 700; alto = 500;

	// Creacion de ventana
	ventana = glfwCreateWindow( ancho, alto,
							"Tarea 1 de Graficos por Computadora",
							NULL, NULL);
		// Si algo sale mal terminamos
	if( !ventana ) {
		glfwTerminate();
		return -1;
	}

	//Contexto y ventana
	glfwMakeContextCurrent( ventana );

// Bucle de programa
	while( !glfwWindowShouldClose( ventana )){

		glClear( GL_COLOR_BUFFER_BIT );

		glBegin( GL_TRIANGLES );

		glVertex2f(-0.5f,-0.5f);
		glVertex2f( 0.0f, 0.5f);
		glVertex2f( 0.5f,-0.5f);

		glEnd( );

		glfwSwapBuffers( ventana );
		glfwPollEvents();
	}


	glfwTerminate();
	return 0;
}