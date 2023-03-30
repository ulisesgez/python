"""
Coleccion de datos:
key = llave
value = valor
"""

print('-----> dict <-----')

diccionario = {
    'ide': 'Integrated Development Enviroment',
    'oop': 'object oriented programming',
    'dbms': 'database management system'
}

print(diccionario)

#largo:
print(len(diccionario))

#acceder a un elementos del diccionario:
print(diccionario['ide'])

#otra forma:
print(diccionario.get('oop'))

#modificando elementos:
diccionario['ide'] = 'integrated development enviroment'
print(diccionario)

#recorrer elemntos:
for termino in diccionario:
    print(termino)
"""
Podrias pensar que es de la siguiente forma:
#recorrer elemntos, acceder al valor:
for termino, valor in diccionario:
    print(termino, valor)
"""
#key + value:
for termino, valor in diccionario.items():
    print(termino, valor)

#key:
for termino in diccionario.keys():
    print(termino)

#value:
for valor in diccionario.values():
    print(valor)

#comprobar existencia de algun elemento:
print('ide'in diccionario)
print('editor'in diccionario)

#agregar:
diccionario['pk'] = 'primary key'
print(diccionario)

#remover elemento:
diccionario.pop('dbms')
print(diccionario)

#limpiar diccionario:
diccionario.clear()
print(diccionario)

#eliminar diccionario:
del diccionario
#print(diccionario)

#