## Autor: Benjamín Rivera
# Tarea 1, IA

## Instrucciones

Estimados,

 - Investigar el problema del Entscheidungsproblem.

> Recuerden lo que platicamos en la clase: Turing creó su modelo teórico ahora llamado Máquina de Turing, y Alonzo Church creó el cálculo lambda; cada quien por su lado pero en el mismo momento científico en que se trabajaba para resolver este problema que propuso el gran matemático David Hilbert. Es el décimo problema de Hilbert, uno de los 23 que propuso en el año 1900.
 
No es tarea de copy-paste. Lean y escriban las ideas que vayan procesando. Algunas las irán entendiendo, pero todas se van procesando y estructurando entre sí. Eso es lo que quiero leer
en sus documentos. 3 hojas carta máximo.

## Actividad

La primera fuente que revise fue [wikipedia](https://es.wikipedia.org/wiki/Entscheidungsproblem) seguida por [wikipedia](https://en.wikipedia.org/wiki/Entscheidungsproblem).

Empieza por definirlo como el reto de lógica simbólica que buscaba encontrar un algoritmo para decidir si cierta formula, de primer orden, era un teorema.

El problema, empezando con la motivación de Leibniz, por querer construir una calculadora de teoremas en el siglo XVII. Siguiendo por la formalización de la pregunta por parte de Hilbert y Ackerman. Luego con los trabajos de Church (calculo lambda) y Turing (maquina de turing), quienes refinaban el concepto de algoritmo y calculabilidad efectiva. Finalmente estos últimos dos, con los conceptos y procesos que cada uno había desarrollado por su cuenta, respondieron negativamente al problema.

Entonces pasando directamente a la formulación de la pregunta de Hilbert. Esta era parte de la lista de 23 problemas que publico en 1900. Lo que entiendo de la formulación es que busca un algoritmo que sea capaz de decidir si un enunciado, lógico de primer orden, es un teorema (verdadero para todos los casos).

Antes de tratar de resolverlo, tanto Church como Turing centraron sus esfuerzos en mejorar la definición de algoritmo. 
 - Church creo el concepto de _efectivamente calculable_ que estaba basado en el desarrollo del \lambda-Calculus.
 - Por otro lado, Turing formalizo la idea de algoritmo con su _maquina automática._ La que hoy en día conocemos como __Maquina de Turing.__
 
Me parece curioso que estos dos modelos descriptivos sean equivalentes, mas porque fueron profesor y alumno en algún momento.
 
Con estas ideas en la cabeza, ya bien formalizadas, ambos dieron una respuesta negativa a la pregunta. Como buen computologo que quiero ser, le entendí mas a la demostración de Turing. El demostró esta idea al hacerlo equivalente al problema de la parada, el cual vimos en la parte anterior de este curso.

Como pequeño resumen, el problema de la parada (Halting Problem) es el que trata de determinar si existe algún algoritmo para decidir si una Maquina de Turing se detendra, o no, en algun momento dada una entrada. Este problema, en general, no es decidible. Y la demostración de esto procede por contradicción. Me parece que la simplificación del [video de udiprod](https://www.youtube.com/watch?v=92WHN-pAFCs) representa bastante bien la situación.




