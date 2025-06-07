"""
Conversión de tipos:
La conversión de tipos en Python permite transformar datos de un tipo a otro usando funciones como
int(), float(), str() y otras. Esto es útil para operar correctamente sobre datos que originalmente
son cadenas de texto, números o booleanos.

Conversión a entero:
Convierte un valor (como una cadena) a un número entero. Si la conversión falla (por ejemplo, con texto no numérico),
se genera un error
"""
numero = "10"
entero = int(numero)
print(entero + 5)  # 15
"""
Conversión a flotante:
Convierte una cadena o número entero a tipo flotante (decimal).
"""
dato = input("Ingresa un número: ")
numero = float(dato)
cuadrado = numero ** 2
print(numero, "a la potencia de 2 es", cuadrado)
"""
Conversión a cadena:
Convierte números, booleanos u otros datos a tipo cadena. Útil para concatenar con texto.
"""
edad = 12
print("Mi edad es: " + str(edad))
# También puedes usar f-strings:
print(f"Mi edad es: {edad}")
"""
Conversión automática al reasignar:
En Python, una variable puede cambiar su tipo de dato según el valor que se le asigne.
"""
dato = "ulises"
print(type(dato))  # <class 'str'>
dato = 12
print(type(dato))  # <class 'int'>
dato = True
print(type(dato))  # <class 'bool'>