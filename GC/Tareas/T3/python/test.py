#! /usr/bin/env python
"""
from OpenGLContext import testingcontext
BaseContext = testingcontext.getInteractive()
"""

from OpenGL.GL import *
from OpenGL.arrays import vbo
from OpenGL.GL import shaders

import glfw
import numpy as np



class TestContext():
    """Creates a simple vertex shader..."""
    
    def OnInit( self ):        
        VERTEX_SHADER = shaders.compileShader("""#version 120
        void main() {
            gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
        }""", GL_VERTEX_SHADER)
        FRAGMENT_SHADER = shaders.compileShader("""#version 120
        void main() {
            gl_FragColor = vec4( 1, 1, 0, 1 );
        }""", GL_FRAGMENT_SHADER)

        self.shader = shaders.compileProgram(VERTEX_SHADER,FRAGMENT_SHADER)
        
        
        self.vbo = vbo.VBO(
            np.array( [
                [  0, 0.3, 0 ],
                [ -0.3,-0.3, 0 ],
                [  0.3,-0.3, 0 ],
                [  0.6,-0.3, 0 ],
                [  0.9,-0.3, 0 ],
                [  0.9, 0.3, 0 ],
                [  0.6,-0.3, 0 ],
                [  0.9, 0.3, 0 ],
                [  0.6, 0.3, 0 ],
            ],'f')
        )
        
        
    def Render( self):
        """Render the geometry for the scene."""
        shaders.glUseProgram(self.shader)        
        try:
            self.vbo.bind()
            try:
                glEnableClientState(GL_VERTEX_ARRAY);
                glVertexPointerf( self.vbo )
                glDrawArrays(GL_PATCHES, 0, 9)
            finally:
                self.vbo.unbind()
                glDisableClientState(GL_VERTEX_ARRAY);
        finally:
            shaders.glUseProgram( 0 )      

            
            
def compute():
    # GLFW window
    if not glfw.init():
        raise("GLFW error")
    ventana = glfw.create_window(512, 512,
                                 "La marioneta",
                                 None, None)
    if not ventana:
        glfw.terminate()
        raise("GLFW error")
    glfw.make_context_current(ventana)
    
    
    ren = TestContext()
    ren.OnInit()
    
    
    while not glfw.window_should_close(ventana):
        
        glClear( GL_COLOR_BUFFER_BIT );
 
        ren.Render()
        
        glfw.swap_buffers(ventana)
        glfw.poll_events()
        
        
    glfw.terminate()

if __name__ == "__main__":
    compute()