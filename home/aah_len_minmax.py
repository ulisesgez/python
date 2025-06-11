"""
Función len():
La función len() devuelve el número de elementos en un objeto iterable, como una cadena,
lista, tupla, diccionario, etc.
"""
lenUno = len('python')
print(lenUno)  # 6

lenDos = [(0, 1), (2, 3)]
lenDosRes = len(lenDos)
print(lenDosRes)  # 2

posicionCero = lenDos[0]
print(posicionCero)  # (0, 1)
posicionUno = lenDos[1]
print(posicionUno)  # (2, 3)
"""
Funciones min() y max():
Las funciones min() y max() devuelven, respectivamente, el valor más pequeño y el más grande de una secuencia
o conjunto de elementos comparables (como listas, tuplas o cadenas de caracteres).
"""
seq = [0, -1, 9, 10, 89, 3, 5000000]
print(min(seq))  # -1
print(max(seq))  # 5000000

cadenaUno = 'Python'
cadenaDos = 'python'

print(min(cadenaUno))  # 'P' (mayúscula tiene menor valor Unicode que minúsculas)
print(max(cadenaUno))  # 'y'
print(min(cadenaDos))  # 'h'