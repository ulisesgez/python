print('-----> listas <-----')
nombres = ['juan', 'maria', 'jose', 'jesus']
nueros = [1, 2, 3, 4, 5]
booleanos = [True, False]

print(nombres)

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