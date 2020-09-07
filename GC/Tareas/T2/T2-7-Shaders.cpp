
// Librerias principales
# include <GL/glew.h>		// Libreria de extension para OpenGL
# include <GLFW/glfw3.h>	// Libreria para ventanas basicas

# include <iostream>

using namespace std;


static unsigned int compileShader(unsigned int tipo, const string &source){

	unsigned int id = glCreateShader(tipo);
	const char *src = source.c_str();
	glShaderSource(id, 1, &src, nullptr);
	glCompileShader(id);

	int result;
	glGetShaderiv(id, GL_COMPILE_STATUS, &result);
	if (result == GL_FALSE){
		int lenght;
		glGetShaderiv(id, GL_INFO_LOG_LENGTH, &lenght);
		char* message = (char*)alloca(lenght * sizeof(char));
		glGetShaderInfoLog(id, lenght, &lenght, message);

		cout << "Error al crear el shader" << endl;
		cout << message << endl;
		glDeleteShader(id);

		return 0;
	}

	return id;
}

static unsigned int createShader(const string &vertexShader, const string &fragmentShader){

	unsigned int program = glCreateProgram();
	unsigned int vs = compileShader(GL_VERTEX_SHADER, vertexShader);
	unsigned int fs = compileShader(GL_FRAGMENT_SHADER, fragmentShader);

	glAttachShader(program, vs);
	glAttachShader(program, fs);
	glLinkProgram(program);
	glValidateProgram(program);

	glDeleteShader(vs);
	glDeleteShader(fs);

	return program;
}



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

	cout << glGetString( GL_VERSION ) << endl;


	float posiciones[6] = {
		-0.5f,-0.5f,
		 0.0f, 0.5f,
		 0.5f,-0.5f
	};

	unsigned int buffer;
	glGenBuffers(1, &buffer);
	glBindBuffer(GL_ARRAY_BUFFER, buffer);
	glBufferData(GL_ARRAY_BUFFER, 6*sizeof(float),
				 posiciones, GL_STATIC_DRAW);

	glEnableVertexAttribArray(0);
	glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE,
				 2*sizeof(float), 0);

	string fragmentShader =
		"#version 330 core\n"
		"\n"
		"layout(location = 0) out vec4 color;"
		"\n"
		"void main(){\n"
		" 	color = vec4(1.0,0.0,0.0,1.0); \n"
		"};\n";

	string vertexShader =
		"#version 330 core\n"
		"\n"
		"layout(location = 0) in vec4 position;"
		"\n"
		"void main(){\n"
		" 	gl_Position = position; \n"
		"};\n";



	unsigned int shader = createShader(vertexShader, fragmentShader);
	glUseProgram(shader);


// Bucle de programa
	while( !glfwWindowShouldClose( ventana )){

		glClear( GL_COLOR_BUFFER_BIT );

		glDrawArrays(GL_TRIANGLES, 0, 3);

		glfwSwapBuffers( ventana );
		glfwPollEvents();
	}

	glDeleteProgram(shader);

	glfwTerminate();
	return 0;
}