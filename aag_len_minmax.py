print('-----> len <-----')
lenUno = len('python')
print(lenUno)

lenDos = [(0, 1), (2, 3)]
lenDosRes = len(lenDos)
print(lenDosRes)# 2
posicionCero = lenDos[0]
print(posicionCero)
posicionUno = lenDos[1]
print(posicionUno)

print('-----> min / max <-----')
seq = [0, -1, 9, 10, 89, 3, 5000000]
cadenaUno = 'Python'
cadenaDos = 'python'

minimo = min(seq)
print(minimo)
maximo = max(seq)
print(maximo)

print(min(cadenaUno))
print(max(cadenaUno))
print(min(cadenaDos))