"""
Operador de asignación (=)
El operador = se usa para asignar valores a una variable. No se trata de una comparación, sino de almacenar 
un valor en una variable. A la izquierda va el nombre de la variable, y a la derecha el valor o expresión 
que se asignará.
"""
variableA = 10  # Asignamos 10 a la variableA
print(variableA)  # Salida: 10
"""
Reasignación con el mismo nombre
Puedes reasignar un nuevo valor a una variable usando su propio valor anterior. Esto permite modificarla paso a paso, como en un contador.
"""
variableA = variableA + 1  # Ahora vale 11
print(variableA)  # Salida: 11
"""
Operadores abreviados (asignación compuesta)
Python permite usar operadores abreviados para modificar variables combinando operadores aritméticos con =, como +=, -=, *=, etc. Esto hace el código más conciso.
"""
variableA += 1  # Ahora vale 12
print(variableA)

variableA -= 2  # Ahora vale 10
print(variableA)

variableA *= 3  # Ahora vale 30
print(variableA)
"""
Operador de igualdad (==)
El operador == se utiliza para comparar si dos valores son iguales. Si lo son, el resultado es True; si no lo son, False. No debe confundirse con =, que asigna valores.
"""
var = 0
print(var == 0)  # True

var = 1
print(var == 0)  # False
"""
Igualdad con expresiones
Puedes usar == para comparar expresiones más complejas. En Python, la expresión a == b * 2 será evaluada como a == (b * 2) debido a la prioridad de operadores.
"""
black_sheep = 6
white_sheep = 3
print(black_sheep == 2 * white_sheep)  # True
"""
Operador de desigualdad (!=)
El operador != evalúa si dos valores no son iguales. Si son distintos, el resultado es True; si son iguales, es False.
"""
var = 0
print(var != 0)  # False

var = 1
print(var != 0)  # True
"""Operador mayor que (>)
El operador > compara si el valor de la izquierda es estrictamente mayor que el de la derecha. Es útil para evaluar condiciones como si una cantidad ha superado cierto umbral.
"""
black_sheep = 6
white_sheep = 5
print(black_sheep > white_sheep)  # True
"""
Operador mayor o igual que (>=)
El operador >= verifica si el valor de la izquierda es mayor o igual al valor de la derecha. Es una comparación no estricta.
"""
centigrade_outside = 0.0
print(centigrade_outside >= 0.0)  # True
"""
Operador menor que (<)
El operador < evalúa si el valor de la izquierda es estrictamente menor que el de la derecha. Se usa para condiciones en donde se busca que algo no sobrepase un límite.
"""
current_velocity_mph = 80
print(current_velocity_mph < 85)  # True
"""
Operador menor o igual que (<=)
El operador <= evalúa si el valor de la izquierda es menor o igual al de la derecha. Es la versión no estricta del operador <.
"""
current_velocity_mph = 85
print(current_velocity_mph <= 85)  # True