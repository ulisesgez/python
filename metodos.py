print('-----> methods<-----')
texto = '  helloWorld My name is Ulises  '
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
print('python'.startswith('py', 'Py'))
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