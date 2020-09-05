
import glfw
import OpenGL.GL as gl
import moderngl.Context as mgc


def main():
    # Inicializar libreria
    if not glfw.init():
        return

    # Crear ventana
    ventana = glfw.create_window(700, 500, 
            "Tarea 1 de Graficos por Computadora en Python", 
            None, None)

    # Precaucion
    if not ventana:
        glfw.terminate()
        return

    # Establecer contexto con la ventana
    glfw.make_context_current(ventana)

    # Ciclo de aplicacion
    while not glfw.window_should_close(ventana):
        gl.glClear( gl.GL_COLOR_BUFFER_BIT )


        gl.glBegin( gl.GL_TRIANGLES )

        gl.glVertex2f(-0.5,-0.5);
        gl.glVertex2f( 0.0, 0.5);
        gl.glVertex2f( 0.5,-0.5);

        gl.glEnd()

        # Swap front and back buffers
        glfw.swap_buffers(ventana)
        # Poll for and process events
        glfw.poll_events()

    # Terminar GLFW
    glfw.terminate()


if __name__ == "__main__":
    main()