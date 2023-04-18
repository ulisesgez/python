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