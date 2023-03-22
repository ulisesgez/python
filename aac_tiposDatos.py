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

#conversion:
numeroUno = "1"
numeroDos = "2"
print('concatenacion: ', numeroUno + numeroDos)
print('suma: ', int(numeroUno) + int(numeroDos))

#flotantes:
print('-----> flotantes <-----')
flotante = 5.5
print(type(flotante))

#boolean:
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

#inputs:
print('-----> inputs <-----')
entrada = input("Cual es tu edad?")
print(type(entrada))
print('tu edad es', entrada)