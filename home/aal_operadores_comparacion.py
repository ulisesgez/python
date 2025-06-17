Comparación de igualdad entre enteros (==)
El operador == compara si dos valores son exactamente iguales. Si los operandos son del mismo tipo y tienen el mismo valor, devuelve True; de lo contrario, False.
a = 4
b = 2
result = a == b  # False, porque 4 no es igual a 2
print(result)
Comparación de igualdad entre entero y cadena
Aunque parezcan similares, un número y una cadena que lo representa no son iguales. Python distingue entre tipos de datos.
b = 2
c = '2'
result = b == c  # False, porque 2 (int) no es igual a '2' (str)
print(result)

Comparación de desigualdad (!=)
El operador != devuelve True si los valores comparados no son iguales, y False si son iguales.

a = 4
b = 2
result = a != b  # True, porque 4 y 2 no son iguales
print(result)

d = 2
result = b != d  # False, porque ambos valen 2
print(result)

Comparación mayor que (>)
El operador > devuelve True si el valor de la izquierda es mayor que el de la derecha.
a = 4
b = 2
result = a > b  # True, porque 4 es mayor que 2
print(result)

Comparación mayor o igual que (>=)
El operador >= devuelve True si el valor de la izquierda es mayor o igual que el de la derecha.
b = 2
d = 2
result = b >= d  # True, porque ambos son iguales (2)
print(result)
