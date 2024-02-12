"""
Conversión de tipos:
Python ofrece dos simples funciones para especificar un tipo de dato y resolver este problema, aquí están: int() y float().

Sus nombres indican cual es su función:

La función int() toma un argumento (por ejemplo, una cadena: int(string)) e intenta convertirlo a un valor entero; si llegase a fallar, el programa entero fallará también (existe una manera de solucionar esto, se explicará mas adelante);
La función float() toma un argumento (por ejemplo, una cadena: float(string)) e intenta convertirlo a flotante (el resto es lo mismo).
Esto es muy simple y muy efectivo. Sin embargo, estas funciones se pueden invocar directamente pasando el resultado de la función input() directamente. No hay necesidad de emplear variables como almacenamiento intermedio.

Se ha implementado esta idea en el editor - observa el código.

¿Puedes imaginar como la cadena introducida por el usuario fluye desde la función input() hacía la función print()?

Intenta ejecutar el código modificado. No olvides introducir un número valido.

Prueba con diferentes valores, pequeños, grandes, negativos y positivos. El cero también es un buen valor a introducir.
"""
anything = float(input("Ingresa un número: "))
something = anything ** 2.0
print(anything, "a la potencia de 2 es", something)

print('-----> conversion <-----')
numeroUno = "1"
numeroDos = "2"
print('numero 1: ', numeroUno, 'numero 2: ', numeroDos)
print('concatenacion: ', numeroUno + numeroDos)#no da una suma
print('suma: ', int(numeroUno) + int(numeroDos))#Aqui si se suma

#otra forma:
print('-----> conversion <-----')
numeroTres = int(input('Introduce primer numero: '))
numeroCuatro = int(input('Introduce segundo numero: '))
result = numeroTres + numeroCuatro
print('El resultado de la suma', result)

#numero a texto:
print('-----> conversion <-----')
numero = int(input('Proporciona un valor del 1 al 3: '))
numeroTexto = ''
if numero == 1:
    numeroTexto = 'numero uno'
elif numero == 2:
    numeroTexto = 'numero dos'
elif numero == 3:
    numeroTexto = 'numero tres'
else:
    numeroTexto = 'valor fuera de rango'

print('-----> conversion <-----')
numeroUno = 1
numeroDos = 2
print('numero 1: ', numeroUno, 'numero 2: ', numeroDos)
print('suma: ', numeroUno + numeroDos)
print('concatenacion: ', str(numeroUno) + str(numeroDos))

print('-----> conversion <-----')
name = 'ulises'
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))

print('-----> conversion <-----')
print('ulises' + 'gutierrez')
print(10 + 20)
print('ulises' + 10)#Error
#solucion a lo anterior:
age = 12
print('Mi edad es: ' + str(age))
print(f'Mi edad es: {age}')

age = input('Escribe tu edad: ')
print(type(age))
age = int(age)
print(f'Tu edad en 10 años sera: {age}')