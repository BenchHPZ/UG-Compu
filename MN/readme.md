# Curso de Métodos Numéricos

Curso de __Métodos Numéricos__, impartido por la doctora _Joaquin Peña Acevedo_ , durante el semestre _Ago-Dic 2020_ en el __Departamento de Matemáticas__ de la __Universidad de Guanajuato__. Todo lo relevante a este curso se tratara en el 
[classroom](https://classroom.google.com/u/4/c/MTIxODMyNjc2NzQy) 
y este repositorio servira para dos cosas:
 - poder compartir las tareas con mayor facilidad, donde se podra incluir las especificaciones locales, y 
 - para cuidar mi delicada computadora que se descompone seguido.

### Pre-requisitos
 - Conocimientos de programación en C, C++ o Python
 - Álgebra Lineal
 - Cálculo Diferencial e Integral


### Evaluacion

 - Taras (semanal) __45%__
 - Proyecto Final __15%__
 - Examenes (2) __30%__
 - Participación __10%__

## Temario

 - __Unidad 1__ Preliminares
 - __Unidad 2__ Solución de ecuaciones no lineales
 - __Unidad 3__ Solución de sistenas de ecuaciones lineales
 - __Unidad 4__ Mínimos cuadrados lineales
 - __Unidad 5__ Cálculo de eigenvalores, eigenvecotres y valores singulares
 - __Unidad 6__ Interpolación
 - __Unidad 7__ Integración numérica
 - __Unidad 8__ Diferenciación numérica
 - __Unidad 9__ Solución numérica de ecuaciones diferenciales

## Requerimientos

Yo llevare este curso con el __lenguaje Python__ ya que, aunque es más lento en ejecución, la programación es más rapida e intuitiva que en C/C++, lo que agilizara el desarrollo de las actividades.

Algo importante para el curso es la 
[libreria GSL](https://www.gnu.org/software/gsl/)
que esta escrita en C, esta librearia debe usarse únicamente cuando ya se haya programado el método, o cuando no haya otra opción viable. Para poder utilizarla con _Python_  se usara 
[esta interfaz](https://pypi.org/project/pygsl/#description)
, que requiere tener instalada _la libreria_, todo esto se puede instalar en __Ubuntu 20__ con

```console
user@localhost$ sudo apt-get install libgsl-dev

user@localhost$ pip3 install pygsl
```

Y por buenas práctiacs, todo esto se ejecutara sobre un ambiente virtual. Para configurarlo es necesario instalar estos 
[requerimientos](./requerimientos.txt) 

### Test

## Desarrollo

### Licencia

Para actividades institucionales, el uso del material, que sea de mi autoria, que este en este repositorio debe apegarse al 
[código de ética](https://www.ugto.mx/images/pdf/normatividad/codigo-etica-universidad-guanajuato.pdf)
de la __Universidad de Guanajuato__. Para cualquier _otro proposito_ este repositorio queda bajo la
[Mit License](./LICENSE)

### Desarroladores
- [Benjamin Rivera][sitioBench]






[//]: <> (///////////////////////////////////////////////////////////////)

[//]: <> (Enlaces de imagenes)
[memeRequerimientos]: https://cdn.memegenerator.es/imagenes/memes/full/28/13/28139681.jpg
[logoWTFPL]: http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-2.png

[//]: <> (Enlaces de siios)
[sitioBench]: http://www.google.com
[licenciaWTFPL]: http://www.wtfpl.net/
