print('-----> listas <-----')
nombres = ['juan', 'maria', 'jose', 'jesus']
nueros = [1, 2, 3, 4, 5]
booleanos = [True, False]
#conversion:
coversionUno = list()
print(coversionUno)
coversionDos = list('Hello')
print(coversionDos)
print(nombres)

#otro ejemplo:
carro = ['mazda', 'chevrolet', 'kia']
print(carro)

#acceder a los elementos:
print(nombres[0])

#acceder a lo elementos de la lista de manera inversa:
print(nombres[-1])

#Imprimir rango:
print(nombres[0:2])#si incluir el indice 2

#Va del inicio de la lista hasta el indice(sin incluirlo)
print(nombres[:3])

#desde el indice indicado hasta el final de la lista:
print(nombres[1:])

#cambiar valor de indice:
print(nombres)
nombres[3] = 'moises'
print(nombres)

#Modificar lista:
ceros = [0] * 5
print(ceros)

#iterar lista:
mascotas = ['perro', 'gato', 'pez']

for mascota in mascotas:
    print(mascota)

#enumerate(hace referencia a las tuplas:
productos = ['laptop', 'mouse', 'teclado', 'monitor']
for producto in enumerate(productos):
    print(producto)

#Iterar cadena:
for nombre in nombres:
    print(nombre)
else:
    print('no existen mas nombres en la lista')

#conocer el largo de una lista
print(len(nombres))

#agregar un nuevo elemento a la lista:
print(nombres)
nombres.append('lucas')
print(nombres)

#insertar un elemento en un indice en especifico(se recorren los elementos):
print(nombres)
nombres.insert(1, 'genaro')
print(nombres)

#remover elemento:
nombres.remove('maria')
print(nombres)

#eliminarr ultimo elemento de la lista:
nombres.pop()
print(nombres)

#elimianr un elemento en un indice indicado:
del nombres[0]
print(nombres)
del nombres[1]
print(nombres)

#limpiar la lista (eliminar elementos):
nombres.clear()
print(nombres)

#borrar la lista por completo:
#del nombres
#print(nombres)#manda error ya que nombres no existe

#metodos:
numbers = [1, 2, 4, 5, 6]

#agregar elemento al final:
numbers.append(7)
print(numbers)

#agregar elemento al inicio:
numbers.insert(0, 'cero')
print(numbers)
numbers.insert(3, 'tres')
print(numbers)

#unir listas:
otherNumbers = [8, 'nueve']
newList = numbers + otherNumbers
print(newList)

#conocer posicion:
print(newList.index('cero'))

#remover primner elemento:
newList.remove(('cero'))
print(newList)

#remover ultimo elemento:
newList.pop()
print(newList)

#remover cierto elemento especifico:
newList.pop(2)
print(newList)

#transformar array al reverso:
newList.reverse()
print(newList)

#ordenar:
jumbledNumbers = [0, 9, 3]
jumbledNumbers.sort()
print(jumbledNumbers)
letters = ['f', 'a', 'e', 'b', 'd', 'c']
letters.sort()
print(letters)
#error:
#no = ['f', 'a', 'e', 'b', 'd', 'c', 0, 9, 3]
#no.sort()
#print(no)

#List Comprehension:
numbers = []
for element in range(1, 11):
    numbers.append(element)

print(numbers)

#Utilizando List Comprehension, es el codigo de arriba pero en una sola linea:

numbersV2 = [element for element in range(1, 11)]
print(numbersV2)

#Desempaquetado de listas:
productos = ["laptop", "mouse", "keyboard", "microphone"]
"""
Esto no:
primero = productos[0]
segundo = productos[1]
tercero = productos[2]
cuarto = productos[3]
Mejor forma:
"""
primero, *otros = productos
print(primero, otros)

"""
De lo anterior podemos ver otro ejemplo:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primero, segundo, *otros, penultimo, ultimo = numeros
print(primero, segundo, otros, penultimo, ultimo)
print(segundo, penultimo, otros)
"""