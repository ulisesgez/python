"""
Las sentencias break y continue
Hasta ahora, hemos tratado el cuerpo del bucle como una secuencia indivisible e inseparable de instrucciones que se realizan completamente en cada giro del bucle. Sin embargo, como desarrollador, podrías enfrentar las siguientes opciones:

parece que no es necesario continuar el bucle en su totalidad; se debe abstener de seguir ejecutando el cuerpo del bucle e ir más allá;
parece que necesitas comenzar el siguiente giro del bucle sin completar la ejecución del turno actual.
Python proporciona dos instrucciones especiales para la implementación de estas dos tareas. Digamos por razones de precisión que su existencia en el lenguaje no es necesaria - un programador experimentado puede codificar cualquier algoritmo sin estas instrucciones. Tales adiciones, que no mejoran el poder expresivo del lenguaje, sino que solo simplifican el trabajo del desarrollador, a veces se denominan dulces sintácticos o azúcar sintáctica.

Estas dos instrucciones son:

break - sale del bucle inmediatamente, e incondicionalmente termina la operación del bucle; el programa comienza a ejecutar la instrucción más cercana después del cuerpo del bucle.
continue - se comporta como si el programa hubiera llegado repentinamente al final del cuerpo; el siguiente turno se inicia y la expresión de condición se prueba de inmediato.
Ambas palabras son palabras clave reservadas.

Ahora te mostraremos dos ejemplos simples para ilustrar como funcionan las dos instrucciones. Mira el código en el editor. Ejecuta el programa y analiza la output. Modifica el código y experimenta.

"""
# break - ejemplo

print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

print('-----> pass <-----')
n = input('introduce un numero: ')
if n >= 0:
    pass
else:
    print(f'{n} is negative')

print('-----> break <-----')
for letra in 'holanda':
    if letra == 'a':
        print(f'letra encontrada: {letra}')
        #con esto rompemos:
        break
else:
    print('fin ciclo')

print('-----> sin continue <-----')

#range, funcion de rango:
print(range(3))
print(range(1, 10, 2))
print(list(range(3)))
print(list(range(5, 10)))
print(list(range(1, 10, 2)))


#en este caso la funcion de rango va del 0 a 9
for i in range(10):
    if i % 2 == 0:
        print(i)

#obteniendo el mismo resultado con contnue:
print('-----> continue <-----')
for j in range(10):
    if j % 2 != 0:
        continue
    print(j)


#
#
#
#
#
#
#
#
#
#
#
#