#class y str, uno dice el valor y otro es el tipo.
#string:
print('-----> string <-----')
cadenaTexto = 'cadenaTexto'
print(cadenaTexto)
#ver tipo de variable:
print(type(cadenaTexto))

#enteros:
print('-----> enteros <-----')
numero = 5
print(numero)
print(type(numero))
negativo = -40
cero = 0
bimario = 0b101010
hexadecimal = 0xFF

#flotantes:
print('-----> flotantes <-----')
flotante = 5.5
print(type(flotante))
#precision decimal:
a = 3.3
print(a)
b = 1.1 + 2.2
print(b)
print(a == b)#False
#entonces como los comparamos, de forma brusca podemos recortar la presicion, pero este pasa a ser un string:
bStr = format(b, ".2g")
print(bStr)
#no podemos comparar un string con entero, asi que:
print(bStr == str(a))#True

#ahora de una forma mas amtematica:
tolerance = 0.00001
print(abs(a - b) < tolerance)#True

#boolean:
print('-----> boolean <-----')
#false:
not True
not 15
not -15
not 'hello'
not [1, 2, 3, 4, 5]

#true:
not False
not 0
not 0.0
not ''
not []

print('-----> boolean <-----')
booleano = True
print(booleano)
print(type(booleano))

print('-----> boolean <-----')
mayorQue = 1 > 2
print(mayorQue)
print(type(mayorQue))

print('-----> boolean <-----')
if mayorQue:
    print('verdadero')
else:
    print('falso')
print(type(mayorQue))

print('-----> boolean with is methods<-----')
print('Python'.isupper())
print('Python'.islower())
print('Python'.istitle())

print('-----> boolean / contencion <-----')
entero = 2 in [1, 2, 3, 4, 5]
flotante = 2.5 in [1, 2, 3, 4, 5]
listaTupla = [1, 2] in [1, 2, 3, 4, 5]
listaTupla = 1 in [(0, 1), (2, 3)]
listaTupla = (0, 1) in [(0, 1), (2, 3)]
seq = [(0, 1), (2, 3)]
seqResultado = 1 in seq
holaMundo = 'h' in 'helloWorld'
print(holaMundo)
python = 'Py' in 'Python'
print(python)

print('-----> functions <-----')

bimarioDos = bin(15)
octal = oct(8)
hexadecimalDos = hex(65535)

print('-----> built in function <-----')
help(bin)

print('-----> escape sequences <-----')
"""
\\ ---> \
\' ---> '
\" ---> "
\n ---> newline
\r ---> carriage return
\t ---> tab
"""
'\x61\x62\x63'#abc
'\x58\u0058\U00000058'#XXX
'I\N{GROWING HEART} \N{SNAKE}'#I💗 🐍