print('-----> break <-----')
for letra in 'holanda':
    if letra == 'a':
        print(f'letra encontrada: {letra}')
        #con esto rompemos:
        break
else:
    print('fin ciclo')

print('-----> sin continue <-----')
#range, funcion de rango, en este caso va del 0 a 9
for i in range(10):
    if i % 2 == 0:
        print(i)

#obteniendo el mismo resultado con contnue:
print('-----> continue <-----')
for j in range(10):
    if j % 2 != 0:
        continue
    print(j)