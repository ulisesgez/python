"""
Operadores Básicos
Un operador es un símbolo del lenguaje de programación, el cual es capaz de realizar operaciones con los valores.

Por ejemplo, como en la aritmética, el signo de + (más) es un operador el cual es capaz de sumar dos números, dando el resultado de la suma.

Sin embargo, no todos los operadores de Python son tan simples como el signo de más, veamos algunos de los operadores disponibles en Python, las reglas que se deben seguir para emplearlos, y como interpretar las reglas que realizan.

Se comenzará con los operadores que están asociados con las operaciones aritméticas más conocidas:

+ - * / // % **
El orden en el que aparecen no es por casualidad. Hablaremos más de ello cuando se hayan visto todos.

Recuerda: Cuando los datos y operadores se unen, forman juntos expresiones. La expresión más sencilla es el literal.

Nota: En los ejemplos, los dobles asteriscos están rodeados de espacios, no es obligatorio hacerlo pero hace que el código sea mas legible.
Los ejemplos muestran una característica importante de los operadores numéricos de Python.

Operadores y sus prioridades:

PEMDAS:
p - parentesis
e - exponentes
m - multiplicacion
d - division
a - adicion
s - sustraccion

Hasta ahora, se ha tratado cada operador como si no tuviera relación con los otros. Obviamente, dicha situación tan simple e ideal es muy rara en la programación real.

También, muy seguido encontrarás más de un operador en una expresión, y entonces esta presunción ya no es tan obvia.

Considera la siguiente expresión:

2 + 3 * 5
Probablemente recordarás de la escuela que las multiplicaciones preceden a las sumas.

Seguramente recordarás que primero se debe multiplicar 3 por 5, mantener el 15 en tu memoria y después sumar el 2, dando como resultado el 17.

El fenómeno que causa que algunos operadores actúen antes que otros es conocido como la jerarquía de prioridades.

Python define la jerarquía de todos los operadores, y asume que los operadores de mayor jerarquía deben realizar sus operaciones antes que los de menor jerarquía.

Entonces, si se sabe que la * tiene una mayor prioridad que la +, el resultado final debe de ser obvio.

Operadores y sus enlaces
El enlace de un operador determina el orden en que se computan las operaciones de los operadores con la misma prioridad, los cuales se encuentran dentro de una misma expresión.

La mayoría de los operadores de Python tienen un enlazado hacia la izquierda, lo que significa que el cálculo de la expresión es realizado de izquierda a derecha.

Este simple ejemplo te mostrará como funciona. Observa:
"""
print(9 % 6 % 2)

"""
Existen dos posibles maneras de evaluar la expresión:

De izquierda a derecha: primero 9 % 6 da como resultado 3, y entonces 3 % 2 da como resultado 1;
De derecha a izquierda: primero 6 % 2 da como resultado 0, y entonces 9 % 0 causa un error fatal.
Ejecuta el ejemplo y observa lo que se obtiene.

El resultado debe ser 1. El operador tiene un enlazado del lado izquierdo. Pero hay una excepción interesante.

Repite el experimento, pero ahora con exponentes.

Utiliza este fragmento de código:

"""
(2 ** 2 ** 3)
"""
Los dos posibles resultados son:

2 ** 2 → 4; 4 ** 3 → 64
2 ** 3 → 8; 2 ** 8 → 256

Ejecuta el código, ¿Qué es lo que observas?

El resultado muestra claramente que el operador de exponenciación utiliza enlazado del lado derecho.

Esto contiene una excepción interesante. Si el operador de exponenciación usa el enlazado del lado derecho, ¿puedes adivinar el resultado del siguiente fragmento?
"""
print(-3 ** 2), print(-2 ** 3), print(-(3 ** 2))
"""
-9
-8
-9

Lista de prioridades
Como eres nuevo a los operadores de Python, no se presenta por ahora una lista completa de las prioridades de los operadores.

En lugar de ello, se mostrarán solo algunos, y se irán expandiendo conforme se vayan introduciendo operadores nuevos.

Observa la siguiente tabla:

Prioridad	Operador	
1	**	
2	+, - (nota: los operadores unarios a la derecha del operador exponencial enlazan con mayor fuerza.)	unario
3	*, /, //, %	
4	+, -	binario

Nota: se han enumerado los operadores en orden de la más alta (1) a la más baja (4) prioridad.

Operadores y paréntesis
Por supuesto, se permite hacer uso de paréntesis, lo cual cambiará el orden natural del cálculo de la operación.

De acuerdo con las reglas aritméticas, las sub-expresiones dentro de los paréntesis siempre se calculan primero.

Se pueden emplear tantos paréntesis como se necesiten, y seguido son utilizados para mejorar la legibilidad de una expresión, aun si no cambian el orden de las operaciones.

Un ejemplo de una expresión con múltiples paréntesis es la siguiente:
"""
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
print((2 ** 4), (2 * 4.), (2 * 4))
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
print((2 % -4), (2 % 4), (2 ** 3 ** 2))

print('-----> suma <-----')
print(-4 + 4)
print(-4. + 8)
operandoUno = 2
operandoDos = 3
suma = operandoUno + operandoDos
print('Resultado suma: ', suma)
#Imorimir con interpolecion:
print(f'Resultado suma: {suma}')

"""
El operador de resta, operadores unarios y binarios
El símbolo del operador de resta es obviamente - (el signo de menos), sin embargo debes notar que este operador tiene otra función - puede cambiar el signo de un número.

Esta es una gran oportunidad para mencionar una distinción muy importante entre operadores unarios y binarios.

En aplicaciones de resta, el operador de resta espera dos argumentos: el izquierdo (un minuendo en términos aritméticos) y el derecho (un sustraendo).

Por esta razón, el operador de resta es considerado uno de los operadores binarios, así como los demás operadores de suma, multiplicación y división.

Pero el operador negativo puede ser utilizado de una forma diferente - observa la ultima línea de código del siguiente fragmento:
"""
print('-----> resta <-----')
print(-4 - 4)
print(4. - 8)
print(-1.1)
operandoUno = 2
operandoDos = 3
resta = operandoUno - operandoDos
print('Resultado resta: ', resta)
#Imorimir con interpolecion:
print(f'Resultado resta: {resta}')

print('-----> multiplicacion <-----')
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)
operandoUno = 2
operandoDos = 3
multiplicacion = operandoUno * operandoDos
print('Resultado multiplicacion: ', multiplicacion)
#Imorimir con interpolecion:
print(f'Resultado multiplicacion: {multiplicacion}')

print('-----> division <-----')
dividendo = 450
divisor = 5
division = dividendo / divisor
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)
operandoUno = 2
operandoDos = 3
division = operandoUno / operandoDos
print('Resultado division: ', division)
#Imorimir con interpolecion:
print(f'Resultado division: {division}')
#Sin punto flotante:
divisionEntera = operandoUno // operandoDos
print('Resultado division: ', divisionEntera)
#Imorimir con interpolecion:
print(f'Resultado division: {divisionEntera}')

print('-----> division entera <-----')
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

print('-----> residuo (módulo)<-----')
print(14 % 4)
operandoUno = 2
operandoDos = 3
modulo = operandoUno % operandoDos
print('Resultado modulo: ', modulo)
#Imprimir con interpolecion:
print(f'Resultado modulo: {modulo}')

print('-----> exponente <-----')
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)
operandoUno = 2
operandoDos = 3
exponente = operandoUno ** operandoDos
print('Resultado exponente: ', exponente)
#Imorimir con interpolecion:
print(f'Resultado exponente: {exponente}')

"""
Operadores Abreviados
Es tiempo de explicar el siguiente conjunto de operadores que harán la vida del programador/desarrollador más fácil. Muy seguido, se desea utilizar la misma variable al lado derecho y al lado izquierdo del operador = operator.

Por ejemplo, si se necesita calcular una serie de valores sucesivos de la potencia de 2, se puede usar el siguiente código:
x = x * 2

También, puedes utilizar una expresión como la siguiente si no puedes dormir y estas tratando de resolverlo con alguno de los métodos tradicionales:
sheep = sheep + 1


Python ofrece una manera más corta de escribir operaciones como estas, lo cual se puede codificar de la siguiente manera:
x *= 2
sheep += 1

A continuación se intenta presentar una descripción general para este tipo de operaciones. Si op es un operador de dos argumentos (esta es una condición muy importante) y el operador es utilizado en el siguiente contexto...:

variable = variable op expresión

...entonces se puede simplificar y mostrar de la siguiente manera:

variable op= expresión

Observa los siguientes ejemplos. Asegúrate de entenderlos todos.

Expresión	            | Operador abreviado
i = i + 2 * j           | i += 2 * j
var = var / 2           | var /= 2
rem = rem % 10          | rem %= 10
j = j - (i + var + rem) | j -= (i + var + rem)
x = x ** 2              | x **= 2
"""