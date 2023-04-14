"""
A diferncia de una lista ya no podemos agregar elemntos,
modificarlos ni tampoco eliminarlos, a una tupla se le conoce
como un tipo inmutable, a diferencia a una lista que se le
conoce como tipo mutable  modificacble.
"""
print('-----> tupla <-----')
frutas = ('naranja', 'platano', 'guayaba')
print(frutas)

verduras = ('papa', 'tomate', 'jitomate')
print(verduras)

#saber el largo:
print(len(frutas))

#acceder a un elemneto:
print(frutas[0])

#navegacion inversa:
print(frutas[-1])

#rango de valores:
print(frutas[0:2])#sin incluir el ultimo indice

#recorre una tupla:
#el end remplaza al salto de linea por defecto:
for fruta in frutas:
    print(fruta)

for fruta in frutas:
    print(fruta, end=' ')

#Modificar tupla de forma indirecta(no es buena practica):
#convertir tupla a lista:
frutasLista = list(frutas)
frutasLista[0] = 'Pera'
#ahora la volvemos a convertir a trupla:
frutas = tuple(frutasLista)
print('\n', frutas)
#otro ejemplo:
(1, 2, 3) + tuple([4, 5, 6])

#eliminar tupla:
del verduras
#print(verduras)#error