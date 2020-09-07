
// Librerias principales
# include <GL/glew.h>		// Libreria de extension para OpenGL
# include <GLFW/glfw3.h>	// Libreria para ventanas basicas

# include <iostream>



int main( void ){

// Creacion de ventana
	// Apuntador para ventana
	GLFWwindow* ventana;

	// Iniciar GLFW
	if( !glfwInit() ) return -1;

	// Variables de tamanio de ventana
	int ancho, alto;
	ancho = 700; alto = 500;

	// Creacion de ventana
	ventana = glfwCreateWindow( ancho, alto,
							"Tarea 2 de Graficos por Computadora",
							NULL, NULL);
		// Si algo sale mal terminamos
	if( !ventana ) {
		glfwTerminate();
		return -1;
	}

	// Contexto y ventana
	glfwMakeContextCurrent( ventana );

	// Inicializar GLEW
	if ( glewInit() != GLEW_OK ) return -2;

	std::cout << glGetString( GL_VERSION ) << std::endl;


	float vertices[6] = {
		-0.5f,-0.5f,
		 0.0f, 0.5f,
		 0.5f,-0.5f
	};

	unsigned int buffer;
	glGenBuffers(1, &buffer);
	glBindBuffer(GL_ARRAY_BUFFER, buffer);
	glBufferData(GL_ARRAY_BUFFER, 6*sizeof(float),
				 vertices, GL_STATIC_DRAW);

// Bucle de programa
	while( !glfwWindowShouldClose( ventana )){

		glClear( GL_COLOR_BUFFER_BIT );

		glDrawArrays(GL_TRIANGLES, 0, 3);

		glfwSwapBuffers( ventana );
		glfwPollEvents();
	}


	glfwTerminate();
	return 0;
}