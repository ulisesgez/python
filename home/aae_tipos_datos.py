"""
Función para identificar tipos de datos type():
La función type() en Python permite conocer el tipo de dato de una variable o valor literal.
Es útil para verificar cómo interpreta Python los datos, especialmente al momento de depurar o al trabajar
con entradas de usuario. Retorna una referencia al tipo de clase del objeto.
"""
# Usando type con diferentes tipos primitivos
print(type(10))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("Hola"))    # <class 'str'>
print(type(True))      # <class 'bool'>

# También se puede usar con variables
x = "Python"
print(type(x))         # <class 'str'>
"""
Datos primitivos:
Los datos primitivos en Python son los tipos de datos más básicos e indivisibles que sirven como bloques
fundamentales para construir información. Representan valores simples como números, texto o valores lógicos.
Estos tipos son gestionados directamente por el lenguaje y no están compuestos por otros elementos.
Los principales tipos primitivos en Python son: int, float, bool y str.
"""
# int: número entero
edad = 26

# float: número decimal
altura = 1.75

# bool: valor lógico
es_mayor_de_edad = True

# str: cadena de texto
nombre = "Ulises"

# Mostrar los tipos de cada uno
print(type(edad))              # <class 'int'>
print(type(altura))            # <class 'float'>
print(type(es_mayor_de_edad))  # <class 'bool'>
print(type(nombre))            # <class 'str'>
"""
Enteros (int):
Los enteros son números sin parte decimal. Se utilizan para contar elementos, definir edades, índices,
o cualquier valor numérico discreto. En Python, cualquier número escrito sin punto decimal se interpreta
automáticamente como un entero.
"""
manzanas = 5
print(manzanas)         # 5
print(type(manzanas))   # <class 'int'>
"""
Flotantes (float):
Los flotantes son números con parte decimal. Se usan cuando se necesita más precisión, como en cálculos científicos,
financieros o mediciones físicas. Python reconoce un número como float cuando incluye un punto decimal.
"""
temperatura = 36.6
print(temperatura)       # 36.6
print(type(temperatura)) # <class 'float'>
"""
Cadenas de texto (str):
Una cadena es una secuencia de caracteres encerrada entre comillas simples o dobles.
Se usa para representar texto, como nombres, mensajes o datos alfanuméricos.
"""
nombre = "Ulises"
print(nombre)          # Ulises
print(type(nombre))    # <class 'str'>
"""
Booleanos (bool):
Los booleanos representan valores de verdad: True o False. Se utilizan en expresiones lógicas, condiciones
y estructuras de control como if.
"""
es_mayor = True
print(es_mayor)         # True
print(type(es_mayor))   # <class 'bool'>