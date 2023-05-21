"""
Bucles en tu código con while

¿Estás de acuerdo con la sentencia presentada a continuación?

mientras haya algo que hacer
    hazlo
 
Toma en cuenta que este registro también declara que, si no hay nada que hacer, nada ocurrirá.

En general, en Python, un bucle se puede representar de la siguiente manera:

while
    instruction
 
Si observas algunas similitudes con la instrucción if, está bien. De hecho, la diferencia sintáctica es solo una: usa la palabra while en lugar de la palabra if.

La diferencia semántica es más importante: cuando se cumple la condición, if realiza sus sentencias sólo una vez; while repite la ejecución siempre que la condición se evalúe como True.

Nota: todas las reglas relacionadas con sangría también se aplican aquí. Te mostraremos esto pronto.

Observa el algoritmo a continuación:

while conditional_expression:
    instruction_one
    instruction_two
    instruction_three
    :
    :
    instruction_n
 
Ahora, es importante recordar que:

si deseas ejecutar más de una sentencia dentro de un while, debes (como con if) poner sangría a todas las instrucciones de la misma manera.
una instrucción o conjunto de instrucciones ejecutadas dentro del while se llama el cuerpo del bucle.
si la condición es False (igual a cero) tan pronto como se compruebe por primera vez, el cuerpo no se ejecuta ni una sola vez (ten en cuenta la analogía de no tener que hacer nada si no hay nada que hacer).
el cuerpo debe poder cambiar el valor de la condición, porque si la condición es True al principio, el cuerpo podría funcionar continuamente hasta el infinito. Observa que hacer una cosa generalmente disminuye la cantidad de cosas por hacer.

Un bucle infinito
Un bucle infinito, también denominado bucle sin fin, es una secuencia de instrucciones en un programa que se repite indefinidamente (bucle sin fin).

Este es un ejemplo de un bucle que no puede finalizar su ejecución:


while True:
    print("Estoy atrapado dentro de un bucle.")
 
Este bucle imprimirá infinitamente "Estoy atrapado dentro de un bucle." en la pantalla.

  Nota  
Si deseas obtener la mejor experiencia de aprendizaje al ver cómo se comporta un bucle infinito, inicia IDLE, crea un nuevo archivo, copia y pega el código anterior, guarda tu archivo y ejecuta el programa. Lo que verás es la secuencia interminable de cadenas impresas de "Estoy atrapado dentro de un bucle." en la ventana de la consola de Python. Para finalizar tu programa, simplemente presiona Ctrl-C (o Ctrl-Break en algunas computadoras). Esto provocará la excepción KeyboardInterrupt y permitirá que tu programa salga del bucle. Hablaremos de ello más adelante en el curso.

Volvamos al bosquejo del algoritmo que te mostramos recientemente. Te mostraremos como usar este bucle recién aprendido para encontrar el número más grande de un gran conjunto de datos ingresados.

Analiza el programa cuidadosamente. Localiza donde comienza el bucle (línea 8) y descubre como se sale del cuerpo del bucle:


# Almacena el actual número más grande aquí.
largest_number = -999999999
 
# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))
 
# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))
 
# Imprime el número más grande.
print("El número más grande es:", largest_number)
 
Comprueba como este código implementa el algoritmo que te mostramos anteriormente.

"""

print('-----> while <-----')

# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.
 
odd_numbers = 0
even_numbers = 0
 
# Lee el primer número.
number = int(input("Introduce un número o escribe 0 para detener: "))
 
# 0 termina la ejecución.
while number != 0:
    # Verificar si el número es impar.
    if number % 2 == 1:
        # Incrementar el contador de números impares odd_numbers.
        odd_numbers += 1
    else:
        # Incrementar el contador de números pares even_numbers.
        even_numbers += 1
    # Leer el siguiente número.
    number = int(input("Introduce un número o escribe 0 para detener: "))
 
# Imprimir resultados.
print("Conteo de números impares:", odd_numbers)
print("Conteo de números pares:", even_numbers)

"""
#Se imprime infinitamente 'ejecutando while', ya que siempre es true:
condicion = True

while condicion:
    print('ejecutando while')
else:
    print('fin ciclo while')
"""
#otro ejemplo:
numero = 1
while numero < 100:
    print(numero)
    numero += 2

#otro ejemplo:
comando = ""
while comando.lower != "salir":
    comando = input("$ ")
    print(comando)

#otro ejemplo:
n = 3
while n >= 0:
    print(n)
    n -= 1

#otro ejemplo:
n = 8
guess = None
while guess != n:
    guess = int(input('n: '))
print('Correct')

#otro ejemplo:
seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
while seq:
    print(seq.pop())
print(seq)

#otro ejemplo:
a, b = 0, 1
while b < 20:
    print(b)
    a, b = b, a + b

#otro ejemplo:
seq = 'XYZ'
index = 0
while index < len(seq):
    print(seq[index])
    index += 1

"""
El bucle while y el bloque else
Ambos bucles while y for, tienen una característica interesante (y rara vez se usa).

Te mostraremos como funciona - intenta juzgar por ti mismo si es utilizable.

En otras palabras, trata de convencerte si la función es valiosa y útil, o solo es azúcar sintáctica.

Echa un vistazo al fragmento en el editor. Hay algo extraño al final - la palabra reservada else.

Como pudiste haber sospechado, los bucles también pueden tener la rama else, como los if.

La rama else del bucle siempre se ejecuta una vez, independientemente de si el bucle ha entrado o no en su cuerpo.

¿Puedes adivinar la output? Ejecuta el programa para comprobar si tenías razón.
"""
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

#Los bucles for se comportan de manera un poco diferente - echa un vistazo al fragmento en el editor y ejecútalo.
for i in range(5):
    print(i)
else:
    print("else:", i)


#otro ejemplo:

contador = 0

while contador < 3:
    print(contador)
    contador += 1
else:
    print('fin ciclo while')

print('-----> while <-----')
"""
while True:
    print('va a el infinito')
"""
counter = 0
while counter < 10:
    counter += 1
    print(counter)

print('-----> while <-----')
#Inicializar variable a nada.
respuesta = None

while respuesta != 'a' and respuesta != 'b' and respuesta != 'c':
    respuesta = input('Que opcion prefieres a), b) y c): ')

if respuesta == 'a':
    print('has elegido bien')
elif respuesta == 'b':
    print('pudiste haber elegido mejor')
elif respuesta == 'c':
    print('elegiste mal')
else:
    print('no me has dado una rspuesta con sentido')


"""
Bucles en tu código con for
Otro tipo de bucle disponible en Python proviene de la observación de que a veces es más importante contar los "giros o vueltas" del bucle que verificar las condiciones.

Imagina que el cuerpo de un bucle debe ejecutarse exactamente cien veces. Si deseas utilizar el bucle while para hacerlo, puede tener este aspecto:


i = 0
while i < 100:
    # do_something()
    i += 1
 
Sería bueno si alguien pudiera hacer esta cuenta aburrida por ti. ¿Es eso posible?

Por supuesto que lo es - hay un bucle especial para este tipo de tareas, y se llama for.

En realidad, el bucle for está diseñado para realizar tareas más complicadas, puede "explorar" grandes colecciones de datos elemento por elemento. Te mostraremos como hacerlo pronto, pero ahora presentaremos una variante más sencilla de su aplicación.

Observa el fragmento de código:


for i in range(100):
    # do_something()
    pass
 
Existen algunos elementos nuevos. Déjanos contarte sobre ellos:

la palabra reservada for abre el bucle for; nota - No hay condición después de eso; no tienes que pensar en las condiciones, ya que se verifican internamente, sin ninguna intervención.
cualquier variable después de la palabra reservada for es la variable de control del bucle; cuenta los giros del bucle y lo hace automáticamente.
la palabra reservada in introduce un elemento de sintaxis que describe el rango de valores posibles que se asignan a la variable de control.
la función range() (esta es una función muy especial) es responsable de generar todos los valores deseados de la variable de control; en nuestro ejemplo, la función creará (incluso podemos decir que alimentará el bucle con) valores subsiguientes del siguiente conjunto: 0, 1, 2 .. 97, 98, 99; nota: en este caso, la función range() comienza su trabajo desde 0 y lo finaliza un paso (un número entero) antes del valor de su argumento.
nota la palabra clave pass dentro del cuerpo del bucle - no hace nada en absoluto; es una instrucción vacía - la colocamos aquí porque la sintaxis del bucle for exige al menos una instrucción dentro del cuerpo (por cierto - if, elif, else y while expresan lo mismo).
Nuestros próximos ejemplos serán un poco más modestos en el número de repeticiones de bucle.
"""

print('-----> for <-----')

for n in [3, 5, 8]:
    print(n)

#otro ejemplo:
for num in range(5):
    print(num)

#otro ejemplo:
numbers = [3, 4, 5]
for n in numbers:
    print(f'the square of {n} , is {n**2}')

#otro ejemplo:
d = dict(x = 3, y = 5, z = -8)
for key in d:
    print(key)

#otro ejemplo:
buscar = 3
for num in range(5):
    if num == buscar:
        print(f'found: {buscar}')
        break
else:
    print(f'{buscar} not found')

#otro ejemplo:

cadena = 'hola'

for letra in cadena:
    print(letra)
else:
    print('fin ciclo for')

print('-----> for & if else<-----')
myList = [1, 2, 3, 4, 5]
for element in myList:
    if element % 2 == 0:
        print(element, 'is even')
    else:
        print(element, 'is odd')

print('-----> for & range <-----')
for x in range(3):
    print('Hello')

for n in range(3, 6):
    print(f'The square of {n} is {n ** 2}')

for n in range(3, -1, -1):
    print(n)

x, y, z = range(3)
print(x)
print(y)
print(z)

first, *rest = range(5)
print(first)
print(rest)

*rest, last = range(5)
print(rest)
print(last)

first, second, *rest = range(5)
print(first)
print(second)
print(rest)

first, *rest, last = range(5)
print(first)
print(last)

xy0, xy1 = [(3, 5), (2, 8)]
print(xy0)
print(xy1)

(x0, y0), (x1, y1) = [(3, 5), (2, 8)]
print(x0)
print(y0)
print(x1)
print(y1)

coords = [(3, 5), (2, 8), (4, 9)]
for x, y in coords:
    print('x:{}, y:{}'.format(x, y))

print('-----> enumerate <-----')
enumerate('abc')
print(list(enumerate('abc')))

print(list(enumerate('abc', start=1)))

print(list(enumerate('def', start=4)))

print('-----> zip <-----')
print(zip('xyz', [3, 5, 8]))
print(zip('xyz', [3, 5, 8], 'ABC'))