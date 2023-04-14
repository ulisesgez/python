print('-----> methods  / dir<-----')
"""
La función dir() devuelve todas las propiedades y métodos del
objeto especificado, sin los valores. Esta función devolverá
todas las propiedades y métodos, incluso las propiedades
integradas que son predeterminadas para todos los objetos.

Sintaxis: dir(objeto)
"""
print(dir(dict))
print(dir(set))

print('-----> methods<-----')

texto = '  helloWorld My name is Ulises  '
diccionario = {'x': 3, 'y': 4, 'z': 5}

print(texto.upper())
print(texto.lower())
print(texto.title())
print(texto.capitalize())
print(texto.swapcase())
print(texto.strip())
print(texto.lstrip())
print(texto.rstrip())
print('helloWorld'.strip('hello'))
print('uno dos tres'.split())
print('uno-dos-tres'.split('-'))
print('uno-dos-tres'.split('-', 1))
print('uno-dos-tres'.rsplit('-', 1))
print('127.0.0.1'.split('.'))
print('-'.join(['uno dos tres']))
print('.'.join(['127.0.0.1']))
print('abcdedcba'.find('b'))
print('abcdedcba'.find('x'))
print('abcdedcba'.find('y'))
print('abcdedcba'.rfind('b'))
print('python'.startswith('py'))
print('python'.startswith('py'))
print('python'.endswith('n'))
print('python'.replace('thon', 'py'))
print('10101010'.replace('0', '1'))
print('left'.ljust(15))
print('right'.rjust(15))
print('center'.center(15))
print('42'.zfill(15))
print('{0}{1}{0}'.format('abra', 'cad'))
print('coordenadas: {lat}, {long}'.format(lat='18.345', long='-66.752'))
print('{:<15}'.format('left'))
print('{:>15}'.format('right'))
print('{:^15}'.format('center'))
print('{:015}'.format(42))
print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())
print(diccionario.get('x', 0))
print(diccionario.update({'y': 2, 'z': 5}))
print(diccionario)
print(diccionario.pop('z'))
print(diccionario)
#clonamos antes de ir borrando:
clon = diccionario.copy()
#se va quitando uno por uno:
diccionario.popitem()
print(diccionario)
diccionario.popitem()
print(diccionario)
print(clon)
#volvemos a clonar antes de eliminar:
original = clon.copy()
clon.clear()
print(clon)