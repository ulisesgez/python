"""
Set a dieferncia de una lista y una tupla, esta no  mantiene un orden y tampoco
permite almacenar elemntos duplicados, no es posible modificar elementos en un set
pero si es posible agregar mas elemntos
"""

print('-----> set <-----')
planetas = {'marte', 'jupiter', 'venus'}
#podra percatarse que es posible cambie el orden al imprimir:
print(planetas)

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

#eliminar elemntos:
planetas.remove('marte')
print(planetas)
#a diferencia de remove, discar no genera error si no encuentra el elemnto a eliminar:
planetas.discard('venus')
print(planetas)

#agregar elementos a unuestro set:
planetas.add('marte')
planetas.add('venus')
print(planetas)

#limpiar set:
planetas.clear()
#print(planetas)