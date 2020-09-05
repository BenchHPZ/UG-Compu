
// Libreria principal
#include <GLFW/glfw3.h>

int main(void) {

// Apuntador a ventana de clase importada de la libreria
    GLFWwindow* ventana;

    // Inicializar libreria
    //		Regresamos -1 si algo sale mal 
    if (!glfwInit())
        return -1;

    // Creamos una ventana con el contexto OpenGL
    ventana = glfwCreateWindow(640, 480, 
    						"Tarea 1 de Graficos por Computadora", 
    						NULL, NULL);
    if (!ventana) {

        glfwTerminate();
        return -1;
    }

    // Establecer relacion entre la ventana y el contexto
    glfwMakeContextCurrent(ventana);

    // Bucle eterno de vida de la ventana
    while (!glfwWindowShouldClose(ventana)) {
        
        // Renderizamos
        glClear(GL_COLOR_BUFFER_BIT);

        // Swap de buffers
        glfwSwapBuffers(ventana);

        // Preguntar por los eventos de proceso
        glfwPollEvents();
    }

    glfwTerminate();
    return 0;
}