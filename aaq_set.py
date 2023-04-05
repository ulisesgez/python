"""
Set a dieferncia de una lista y una tupla, esta no  mantiene un orden y tampoco
permite almacenar elementos duplicados, no es posible modificar elementos en un set
pero si es posible agregar mas elemntos.
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
setNUmbers = set(numbers)
print(setNUmbers)

#preguntar por un elemento en especifico:
print(6 in numbers)

#limpiar set:
planetas.clear()
print(planetas)#set vacio
print(len(planetas))

print('-----> Operaciones con conjuntos <-----')