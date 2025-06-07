"""
Variables:

En Python, las variables son contenedores que permiten almacenar valores como números, cadenas de texto,
y más. Se usan para guardar resultados intermedios y reutilizarlos posteriormente en otras operaciones.
El contenido de una variable puede cambiar a lo largo del programa.
"""
var = 1
print(var)
"""
Componentes de una variable:

Una variable en Python tiene dos componentes esenciales:
- Un nombre: el identificador del contenedor.
- Un valor: el contenido que se almacena.
El nombre debe seguir ciertas reglas para ser válido.

Nombres de variables:

Los nombres de variables deben comenzar con una letra (a-z, A-Z) o un guion bajo _, y pueden contener letras,
dígitos (0-9) y guiones bajos. Son sensibles a mayúsculas y minúsculas, por lo que var y Var son diferentes.
No se deben usar palabras clave reservadas de Python como nombres de variables.

Ejemplos válidos:

my_variable
Exchange_Rate
counter
переменная

_

Ejemplos inválidos:

10t (empieza con un número)
!important (carácter inválido)
exchange rate (contiene espacio)

PEP 8:
El PEP 8 es una propuesta de mejora de Python que define cómo escribir código de forma legible. 
Recomienda usar nombres de variables y funciones en minúsculas y separar palabras con guion bajo (snake_case). 
También sugiere mantener estilos consistentes con el proyecto.
"""
my_variable = 10
def my_function():
    pass
"""
Palabras clave reservadas:
Python tiene un conjunto de palabras clave que no se pueden usar como nombres de variables, funciones u objetos.
Estas palabras tienen un significado especial para el lenguaje.

Ejemplos de palabras clave:
if, else, while, import, class, def, True, None, etc.

Ejemplo incorrecto:
import = 5  #Error: 'import' es una palabra clave.

Ejemplo permitido por la sensibilidad de mayúsculas:
"""
Import = 5  #válido, aunque no recomendado
"""
Asignación de valores a variables:

Una variable se crea al asignarle un valor con el signo =, sin necesidad de declaración previa.
Puedes asignarle cualquier tipo de dato compatible con Python.
"""
var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
"""
Uso de variables:

Puedes utilizar cualquier número de variables para lograr el objetivo de un programa.
Sin embargo, no se pueden usar variables que no han sido previamente definidas (asignadas).
"""
var = 1
print(var)
"""
Mostrar variables con print():

Puedes mostrar el contenido de una variable usando print(). Además, puedes combinar texto con variables
usando el operador +.
"""
version = "3.8.5"
print("Python version: " + version)
"""
Reasignar valores a variables:

Una variable puede recibir nuevos valores en cualquier momento.
Python interpreta el signo = como un operador de asignación, no de igualdad. El valor de la derecha
se evalúa y se asigna a la variable de la izquierda.
"""
var = 1
print(var)
var = var + 1
print(var)

var = 100
var = 200 + 300
print(var)