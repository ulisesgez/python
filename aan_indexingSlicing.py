print('-----> indexing <-----')
languaje = 'phyton'
seq = ['a', 0, 'b', 1, 'c', 2, 'd', 3]

print(languaje[0])
print(languaje[1])
print(languaje[2])
print(languaje[3])
print(languaje[4])
print(languaje[5])

print('-----> slicing <-----')
print(languaje[0:6])#no tomamos la ultima posicion 6, es antes en la 5
print(languaje[0:])#va al final
print(languaje[0:])#inicio al final
print(languaje[0:6:2])#saltos de 2 en este caso
print(languaje[::2])#saltos de 2 en este caso
print(seq[::2])
print(seq[::3])
print(seq[1::2])
print(seq[::-2])
print(seq[5:1:-1])
print(seq[::-1])