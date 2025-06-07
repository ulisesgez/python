"""
Estructuras de datos:
Los tipos de datos compuestos o estructuras de datos en Python son colecciones que agrupan múltiples valores
(de cualquier tipo, incluso otros compuestos). A diferencia de los datos primitivos, estos tipos permiten organizar,
almacenar y manipular conjuntos de datos.
Python ofrece varias estructuras incorporadas como list, tuple, set, frozenset y dict, cada una con sus
propias reglas de mutabilidad, orden y unicidad.
"""
# list: lista mutable y ordenada
frutas = ["manzana", "plátano", "naranja"]

# tuple: tupla inmutable y ordenada
coordenadas = (10.5, 20.3)

# set: conjunto mutable, desordenado y sin elementos repetidos
numeros_unicos = {1, 2, 3, 2, 1}

# frozenset: conjunto inmutable
colores = frozenset(["rojo", "verde", "azul"])

# dict: diccionario de pares clave:valor
persona = {"nombre": "Ulises", "edad": 26, "nacionalidad": "mexicana"}

# Mostrar tipos
print(type(frutas))       # <class 'list'>
print(type(coordenadas))  # <class 'tuple'>
print(type(numeros_unicos))  # <class 'set'>
print(type(colores))      # <class 'frozenset'>
print(type(persona))      # <class 'dict'>

"""
List:
Una list en Python es una colección ordenada de elementos que puede modificarse.
Puede contener cualquier tipo de datos, incluidos otros objetos compuestos, y permite duplicados.
"""
nombres = ["Ana", "Luis", "Carlos"]
nombres.append("Sofía")   # Se agrega un nuevo elemento
print(nombres)  # ['Ana', 'Luis', 'Carlos', 'Sofía']

"""
Tuple:
Una tuple es una colección ordenada que no puede modificarse una vez creada.
Es útil para representar datos fijos o que no deben cambiarse, y también permite duplicados.
"""
punto = (4, 5)
# punto[0] = 10  # Esto causaría un error, porque las tuplas son inmutables
print(punto)  # (4, 5)

"""
Dict:
Un dict es una colección no ordenada (hasta Python 3.6) o ordenada por inserción (desde Python 3.7), compuesta
por pares clave:valor. Las claves deben ser únicas e inmutables, y los valores pueden ser de cualquier tipo.
"""
alumno = {"nombre": "Ulises", "edad": 26}
alumno["edad"] = 27  # Se puede actualizar un valor
print(alumno)  # {'nombre': 'Ulises', 'edad': 27}

"""
Set:
Un set es una colección no ordenada y sin elementos duplicados. Es útil para operaciones de teoría de conjuntos
como uniones, intersecciones y diferencias.
"""
numeros = {1, 2, 2, 3}
print(numeros)  # {1, 2, 3} — los duplicados son eliminados automáticamente

"""
Frozenset:
Un frozenset es similar a un set, pero no puede modificarse una vez creado.
Es útil cuando necesitas un conjunto constante o como clave en un diccionario.
"""
colores = frozenset(["rojo", "verde", "azul"])
# colores.add("amarillo")  # Error: no se puede modificar un frozenset
print(colores)  # frozenset({'verde', 'azul', 'rojo'})