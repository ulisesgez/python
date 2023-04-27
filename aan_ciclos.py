print('-----> while <-----')
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