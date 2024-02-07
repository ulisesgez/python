"""
Direccion de memoria:
La direccion de memoria es un numero unico que identifica la ubicacion de un dato en 
la memoria de la computadora.
La funcion id() devuelve la direccion de memoria de un objeto.
"""

#posicion de memoria donde se encuentra el valor que almacena x:
x = 1
print(id(x))

#posicion de memoria donde se encuentra el valor que almacena r:
y = 2
print(id(y))

#posicion de memoria donde se encuentra el valor que almacena result:
result = x + y
print(id(result))