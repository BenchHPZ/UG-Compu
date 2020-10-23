""" Modulo para ayuda.

En este modulo programar todas las funciones nada pegajosas,
no interesantes y tediosas pero que se necesitan para dejar
esto corriendo.
"""

################################
#           Shaders             #
##################################


class helperShaders(object):
    """ Clase para manejar los shaders y ponerlos en program. """
    
    def __init__(self, vertex, fragment):
        """
        Input: 
            vertex := nombre del archivo para cargar el vertex
                shader
            fragment := nombre del archivo para cargar el fragment
                shader
        """
        
        shader, fragment = self._get_shader(vertex, fragment)
        
        self.program_id = glCreateProgram()
        vs_id = self.add_shader(vertex, GL_VERTEX_SHADER)
        frag_id = self.add_shader(fragment, GL_FRAGMENT_SHADER)

        glAttachShader(self.program_id, vs_id)
        glAttachShader(self.program_id, frag_id)
        glLinkProgram(self.program_id)

        if glGetProgramiv(self.program_id, GL_LINK_STATUS) != GL_TRUE:
            info = glGetProgramInfoLog(self.program_id)
            glDeleteProgram(self.program_id)
            glDeleteShader(vs_id)
            glDeleteShader(frag_id)
            raise RuntimeError('Error linking program: %s' % (info))
        glDeleteShader(vs_id)
        glDeleteShader(frag_id)
        
    def _get_shader(vs='vertexShader.bch', fs='fragmentShader.bch'):
        """ Obtener shaders y ponerlos en un string cada uno. """
        vertex_shader = "".join(open(vs, 'r'))
        fragment_shader = "".join(open(fs, 'r'))

        return vertex_shader, fragment_shader

    def add_shader(self, source, shader_type):
        """  Funcion para compilar y agregar shaders
        
        Input
            source := String que contiene al shader
            shader_type := Tipo de shader de OpenGl
        Output
            shader_id := ID del shader compilado
        """
        try:
            shader_id = glCreateShader(shader_type)
            glShaderSource(shader_id, source)
            glCompileShader(shader_id)
            if glGetShaderiv(shader_id, GL_COMPILE_STATUS) != GL_TRUE:
                info = glGetShaderInfoLog(shader_id)
                raise RuntimeError('El shader no se pudo compilar: %s' % (info))
            return shader_id
        except:
            glDeleteShader(shader_id)
            raise

    def uniform_location(self, var):
        """ Getter de variable uniforme. """
        return glGetUniformLocation(self.program_id, var)

    def attribute_location(self, var):
        """ Getter de la direccion de atributo. """
        return glGetAttribLocation(self.program_id, var)