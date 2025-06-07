"""
Introducción a la programación:

La programación es el proceso de diseñar y escribir instrucciones que una computadora puede entender y ejecutar.
Estas instrucciones, llamadas programas, le permiten a la computadora realizar tareas específicas,
desde operaciones matemáticas simples hasta funciones complejas como manejar una página web o controlar un robot.
Aunque las computadoras son muy potentes, no entienden conceptos por sí solas;
necesitan que se les indique exactamente qué hacer, paso a paso.
"""
# Calcular la velocidad promedio de un viaje
distancia = 150  # kilómetros
tiempo = 3       # horas

velocidad = distancia / tiempo
print("Velocidad promedio:", velocidad, "km/h")
"""
Lenguajes naturales vs. lenguajes de programación:

Un lenguaje es un sistema de comunicación que permite expresar ideas.
Los humanos usan lenguajes naturales (como el español o el inglés), mientras que las computadoras usan
lenguajes de programación para entender instrucciones. Estos lenguajes son más estructurados y formales
que los naturales, y están diseñados para ser interpretados o traducidos por una máquina.

Los lenguajes de programación permiten escribir instrucciones comprensibles tanto para el programador como,
con ayuda de traductores (como compiladores o intérpretes), para la computadora.
A diferencia del lenguaje máquina, que es difícil de leer para los humanos,
los lenguajes de alto nivel como Python son más accesibles y expresivos.
"""
# Programa en lenguaje de alto nivel (Python) para sumar dos números
a = 10
b = 5
suma = a + b
print("La suma es:", suma)
"""
Compilación vs. Interpretación:

Los programas escritos en lenguajes de alto nivel, como Python o C, no pueden ser entendidos directamente
por una computadora. Por eso, necesitan ser traducidos a lenguaje máquina. Existen dos formas principales
de hacer esta traducción:

Compilación: Traduce todo el código fuente de una vez a lenguaje máquina, generando un archivo ejecutable.
Esto ocurre antes de que se ejecute el programa.

Interpretación: Traduce y ejecuta el código línea por línea en tiempo real, mientras el programa se está ejecutando.

Ambos modelos tienen ventajas y desventajas. La compilación genera programas más rápidos y portables
(como archivos .exe), pero requiere tiempo de traducción. La interpretación permite una ejecución más flexible
y directa, ideal para pruebas rápidas y aprendizaje, aunque con menor rendimiento.
"""
# Python es un lenguaje interpretado
nombre = input("¿Cómo te llamas? ")
print("Hola,", nombre)

"""
¿Qué es Python?:

Python es un lenguaje de programación de alto nivel, interpretado, gratuito y de código abierto.
Fue diseñado para ser fácil de aprender, leer y escribir. Es ampliamente usado para desarrollar aplicaciones web,
automatización, análisis de datos, inteligencia artificial, y más.
Python destaca por su sintaxis clara y su enfoque en la legibilidad del código.

Fue creado en 1989 por Guido van Rossum como un proyecto personal. El nombre proviene de la serie de comedia
Monty Python’s Flying Circus, no de la serpiente. A lo largo de los años, Python ha crecido gracias al esfuerzo
de miles de colaboradores en todo el mundo y se ha convertido en uno de los lenguajes más populares
y versátiles del planeta.

Python pertenece a la categoría de lenguajes interpretados, lo que significa que necesita un intérprete para
ejecutarse. Esto permite probar y modificar código rápidamente, ideal para principiantes y desarrolladores ágiles.

Ventajas principales de Python:

- Fácil de aprender y enseñar
- Sintaxis simple y legible
- Multiplataforma y de código abierto
- Amplia comunidad y recursos
- Usado en ciencia, web, automatización, IA, etc.
"""
# Un programa simple que saluda al usuario
nombre = input("¿Cómo te llamas? ")
print("Hola,", nombre, "¡Bienvenido a Python!")

"""
Python 2 vs. Python 3:
Python tiene dos versiones principales: Python 2, que es la versión clásica, y Python 3,
la versión moderna y recomendada.

Python 2 fue durante mucho tiempo la base del desarrollo en Python, pero ya no recibe mejoras funcionales,
solo actualizaciones críticas de seguridad. Se considera una tecnología en desuso
(su soporte oficial finalizó en 2020), pero aún se mantiene viva en muchos sistemas heredados,
especialmente en empresas con aplicaciones antiguas que son costosas de migrar.

Python 3, lanzado en 2008, es el futuro (y presente) de Python. Introdujo cambios significativos para hacer
el lenguaje más coherente, seguro y potente, aunque eso provocó que no fuera compatible hacia atrás con Python 2.
Es decir, el código Python 2 no se puede ejecutar directamente en un entorno Python 3 sin modificaciones.

Este quiebre fue intencional: Python 3 fue diseñado con una filosofía más clara y moderna,
eliminando ambigüedades del pasado.

Hoy en día, Python 3 es el estándar. Todos los desarrollos nuevos deben hacerse en esta versión.
La comunidad, bibliotecas y herramientas modernas ya giran exclusivamente en torno a Python 3.
"""