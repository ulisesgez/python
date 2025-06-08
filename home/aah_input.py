"""
Función input():
La función input() se utiliza para capturar datos introducidos por el usuario desde la consola.
Siempre devuelve un valor de tipo cadena de texto (str), incluso si el usuario escribe un número.
Para operar matemáticamente con la entrada, se debe convertir con int(), float(), etc.
"""
input('Enter your name: ')
result = input('Hola, ¿cómo estás? ')
print('Me alegra que te encuentres', result)

entrada = input("¿Cuál es tu edad? ")
print(type(entrada))           # <class 'str'>
print('Tu edad es', entrada)