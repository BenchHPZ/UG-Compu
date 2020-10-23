#!/usr/bin/env python
# coding: utf-8

# # Tarea 1
# 
# Este notebook ayudara a crear todos los modulos necesarios para esta tarea (Ze Pupette).

# ## Pila de matrices

# In[ ]:





# ## Visualizacion en OpenGl

# In[2]:


import glfw
import moderngl
import numpy as np

from OpenGL.GL import *
from OpenGL.arrays import ArrayDatatype

from PIL import Image


# In[4]:


def get_shader(vs='vertexShader.bch', fs='fragmentShader.bch'):
    """ Get shader from separated files """
    vertex_shader = "".join(open(vs, 'r'))
    fragment_shader = "".join(open(fs, 'r'))
    
    return vertex_shader, fragment_shader

    
def compile_shader(tipo, shader):
    try:
        shader_id = glCreateShader(tipo)
        glShaderSource( shader_id, shader)
        glCompileShader( shader_id )


        result = glGetShaderiv( shader_id, GL_COMPILE_STATUS)
        if result == GL_FALSE:
            print("Error al crear el shader")
            glDeleteShader(shader_id)
            return None
        
        print(shader)
        return shader_id
    except:
        raise Exception("Error al compilar shaders")

def createShader():
    vs, fs = get_shader()
    
    program = glCreateProgram()
    vs = compile_shader(GL_VERTEX_SHADER, vs)
    fs = compile_shader(GL_FRAGMENT_SHADER, fs)
    glLinkProgram(program)
    glValidateProgram(program)
    
    glDeleteShader(vs)
    glDeleteShader(fs)
    
    return program


def main():
    # GLFW window
    if not glfw.init():
        return None
    ventana = glfw.create_window(512, 512,
                                 "La marioneta",
                                 None, None)
    if not ventana:
        glfw.terminate()
        return None
    glfw.make_context_current(ventana)
    print(glGetString(GL_VERSION) )
        
    dtype = np.float32

    posiciones = np.array( [-0.5,-0.5,
                             0.0, 0.5,
                             0.5,-0.5 ],
                          dtype=np.dtype)
    _helper = np.array([1.0,1.0],
                       dtype=np.dtype)
    
    buffer = glGenBuffers(1)
    glBindBuffer( GL_ARRAY_BUFFER, buffer)
    glBufferData( GL_ARRAY_BUFFER, 
                 ArrayDatatype.arrayByteCount(posiciones), 
                 posiciones, GL_STATIC_DRAW)
    
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 
                          ArrayDatatype.arrayByteCount(_helper),
                          0)
    
    programShader = createShader()
    glUseProgram(programShader)
    
    while not glfw.window_should_close(ventana):
        
        glClear( GL_COLOR_BUFFER_BIT );

        glDrawArrays(GL_TRIANGLES, 0, 3);
        
        glfw.swap_buffers(ventana)
        glfw.poll_events()
        
        
    glDeleteProgram(programShader)
    glfw.terminate()
    
    
main()


# In[5]:


"""

def main():
    # GLFW window
    if not glfw.init():
        return None
    ventana = glfw.create_window(512, 512,
                                "La marioneta",
                                None, None)
    if not ventana:
        glfw.terminate()
        return None
    glfw.make_context_current(ventana)


    # Contexto de opengl
    ctx = moderngl.create_context()


    vertex_shader = "".join(open('vertexShader.bch', 'r'))
    fragment_shader = "".join(open('fragmentShader.bch', 'r'))

    prog = ctx.program(vertex_shader=vertex_shader, 
                       fragment_shader=fragment_shader, )

    x = np.linspace(-1.0, 1.0, 50)
    y = np.random.rand(50) - 0.5
    b = np.random.rand(50)
    g = np.random.rand(50)
    r = np.random.rand(50)

    vertices = np.dstack([x, y, r, g, b])

    vbo = ctx.buffer(vertices.astype('f4').tobytes())
    vao = ctx.simple_vertex_array(prog, vbo, 'in_vert', 'in_color')

    fbo = ctx.simple_framebuffer((512, 512))
    
    fbo.use()
    fbo.clear(0.0, 0.0, 0.0, 1.0)
    vao.render(moderngl.LINE_STRIP)
    
    
    i=0
    while not glfw.window_should_close(ventana):
        
        glClear(GL_COLOR_BUFFER_BIT)
        
        glBegin( GL_TRIANGLES)
        
        glVertex2f(-0.5, -0.5)
        glVertex2f( 0.0,  0.5)
        glVertex2f( 0.5, -0.5)
        
        glEnd()

        #i=1
        
        glfw.swap_buffers(ventana)
        #glfw.wait_events()
        glfw.poll_events()
    
    
    glfw.terminate()
    
    
main()
"""
None


# In[ ]:





# ## GUI  y concatenar lo anterior

# In[5]:


import tkinter as tk

w = tk.Tk()

w.mainloop()


# In[ ]:




