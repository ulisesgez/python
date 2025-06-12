"""
Operadores básicos
Un operador es un símbolo del lenguaje de programación capaz de realizar operaciones sobre valores.
En Python, los operadores aritméticos incluyen +, -, *, /, //, % y **, los cuales permiten realizar sumas,
restas, multiplicaciones, divisiones, divisiones enteras, obtener residuos y exponenciaciones, respectivamente.
"""
print(2 + 3)
print(4 - 1)
print(5 * 2)
print(8 / 4)
print(9 // 4)
print(14 % 4)
print(2 ** 3)
"""
Prioridad de operadores (Jerarquía)
Cuando una expresión contiene múltiples operadores, Python evalúa primero aquellos con mayor prioridad.
La jerarquía se puede recordar con PEMDAS: Paréntesis, Exponentes, Multiplicación y División, Adición y Sustracción.
Esta jerarquía garantiza resultados correctos sin ambigüedad.
"""
print(2 + 3 * 5)  # Resultado: 17, porque se evalúa primero 3 * 5 = 15, luego 2 + 15
"""
Enlace de operadores (Asociatividad)
El enlace define el orden de evaluación cuando varios operadores con la misma prioridad están presentes.
La mayoría se evalúan de izquierda a derecha, excepto la exponenciación (**), que se evalúa de derecha a izquierda.
"""
print(9 % 6 % 2)      # Resultado: 1 (de izquierda a derecha)
print(2 ** 2 ** 3)    # Resultado: 256 (de derecha a izquierda)
print(-3 ** 2)        # Resultado: -9
print(-(3 ** 2))      # Resultado: -9
"""
Lista parcial de prioridades
Esta tabla muestra algunos operadores y su prioridad en orden descendente (1 = mayor prioridad):

Prioridad:	Operador:
-	        **
-	        +, - (unarios, junto a **)
-	        *, /, //, %
-	        +, - (binarios)

Paréntesis
El uso de paréntesis permite alterar la jerarquía predeterminada, forzando la evaluación de expresiones
en el orden deseado. También mejora la legibilidad del código, aunque no cambie el resultado.
"""
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
print((2 ** 4), (2 * 4.), (2 * 4))
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
print((2 % -4), (2 % 4), (2 ** 3 ** 2))
"""
Operadores unarios y binarios
Un operador binario requiere dos operandos (ej. suma o resta entre dos valores). Un operador 
unario requiere solo uno (como el signo negativo que cambia el valor de un número).
"""
print(-4 + 4)            # -4 es un operador unario
print(-4 - 4)            # Primer - es unario, segundo es binario
print(-1.1)              # Operador unario
"""
Operadores aritméticos
Los operadores aritméticos en Python permiten realizar operaciones matemáticas básicas entre valores numéricos.
Puedes usarlos entre enteros o flotantes, y combinarse libremente.
"""
# Suma
operandoUno = 2
operandoDos = 3
suma = operandoUno + operandoDos
print(f'Resultado suma: {suma}')

# Resta
resta = operandoUno - operandoDos
print(f'Resultado resta: {resta}')

# Multiplicación
multiplicacion = operandoUno * operandoDos
print(f'Resultado multiplicacion: {multiplicacion}')

# División flotante y entera
division = operandoUno / operandoDos
divisionEntera = operandoUno // operandoDos
print(f'Resultado division: {division}')
print(f'Resultado division entera: {divisionEntera}')

# Módulo
modulo = operandoUno % operandoDos
print(f'Resultado modulo: {modulo}')

# Exponente
exponente = operandoUno ** operandoDos
print(f'Resultado exponente: {exponente}')
"""
Operadores abreviados
Python permite combinar operadores aritméticos con el operador de asignación = para hacer más concisas
ciertas expresiones. En lugar de x = x + 1, se puede escribir x += 1. Esto es útil para operaciones repetitivas
o de actualización.
"""
i = 0
j = 2
i += 2 * j       # Equivale a i = i + (2 * j)
var = 10
var /= 2
rem = 23
rem %= 10
x = 3
x **= 2
print(i, var, rem, x)  # Salida: 4, 5.0, 3, 9
"""
Operador * con secuencias
El operador * también puede usarse para repetir secuencias como cadenas (str), listas (list) o tuplas (tuple).
Multiplicar una secuencia por un entero genera una nueva con los elementos repetidos esa cantidad de veces.
"""
pyTwice = 'Py' * 2
print(pyTwice)  # 'PyPy'

lista = [1, 0, 0, 0, 1] * 3
print(lista)  # [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1]

tupla = (2, 4, 8, 16, 32, 64) * 2
print(tupla)  # (2, 4, 8, 16, 32, 64, 2, 4, 8, 16, 32, 64)

caracteres = '~' * 50
print(caracteres)  # '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'