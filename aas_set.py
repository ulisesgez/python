"""
Set a dieferncia de una lista y una tupla, esta no  mantiene un orden y tampoco
permite almacenar elementos duplicados, no es posible modificar elementos en un set
pero si es posible agregar mas elementos.
EN algunas ocasiones los Set hace referencia a conjuntos, se parecen a un diccionario
pero estos no tiene par clave - valor (key, value).
"""
print('-----> set <-----')
planetas = {'marte', 'jupiter', 'venus'}
countries = {'col', 'mex', 'usa', 'mex'}
#podra percatarse que es posible cambie el orden al imprimir:
print(planetas)
#no se repite mex:
print(countries)

#largo de elemntos
print(len(planetas))

#verficar si un elemnto esta presente:
print('jupiter' in planetas)#true
print('tierra' in planetas)#false

#agregar elementos a unuestro set:
planetas.add('tierra')
print(planetas)

#no se pueden duplicar elemntos:
planetas.add('marte')
print(planetas)

#actualizar:
countries.update({'arg', 'pe'})
print(countries)

#eliminar elementos:
planetas.remove('marte')
print(planetas)
#a diferencia de remove, discar no genera error si no encuentra el elemnto a eliminar:
planetas.discard('venus')
print(planetas)

#agregar elementos a unuestro set:
planetas.add('marte')
planetas.add('venus')
print(planetas)

#otra forma de definir conjuntos,a partir de otras estructuras de datos:
setString = set('saturno')
print(setString)

#tupla a set:
setTupla = set(('urano', 'neptuno'))
print(setTupla)
setTupla = set(('pluton'))
print(setTupla)

#ahora con listas:
numbers = [1, 2, 3, 4, 5, 4, 5, 3, 2, 1]
setNumbers = set(numbers)
print(setNumbers)

#preguntar por un elemento en especifico:
print(6 in numbers)

#limpiar set:
planetas.clear()
print(planetas)#set vacio
print(len(planetas))

print('-----> Operaciones con conjuntos <-----')
conjuntoA = {'elem1', 'elem2', 'elem3', 'elem4', 'elem5'}
conjuntoB = {'elem5', 'elem6', 'elem7', 'elem8', 'elem9', 'elem0'}

#union:
#set1 |= set2
conjuntoC = conjuntoA.union(conjuntoB)
print(conjuntoC)
#otra forma:
print(conjuntoA | conjuntoB)

#interseccion:
#set1 & set2
conjuntoD = conjuntoA.intersection(conjuntoB)
print(conjuntoD)
#otra forma:
print(conjuntoA & conjuntoB)

#Diferencia:
#set1 -= set2
conjuntoE = conjuntoA.difference(conjuntoB)
print(conjuntoE)
print(conjuntoA - conjuntoB)

#Diferencia Simetrica:
#set1 ^= set2
conjuntoF = conjuntoA.symmetric_difference(conjuntoB)
print(conjuntoF)
print(conjuntoA ^ conjuntoB)

#frozenset:
s = {'a', 'b', 'c', 'b', 'a'}
print(frozenset(s))

print('comparar')

compararSet = set('senselessness')
print(compararSet)

compararFrozenset = frozenset('senselessness')
print(compararFrozenset)

print('modificar')

modificarSet = set('senselessness')
print(modificarSet)
modificarSet.add('takeashower')
print(modificarSet)

modificarFrozenset = frozenset('senselessness')
print(modificarFrozenset)
#no se puede añadir:
#modificarFrozenset.add('takeashower')
#print(modificarFrozenset)

#isdisjoint:
numeros = {0, 1, 2, 3, 4, 5, 6, 7, 8}
numeros.isdisjoint({9})#true
numeros.isdisjoint({0})#false