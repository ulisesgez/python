#conversion:
print('-----> conversion <-----')
numeroUno = "1"
numeroDos = "2"
print('numero 1: ', numeroUno, 'numero 2: ', numeroDos)
print('concatenacion: ', numeroUno + numeroDos)#no da una suma
print('suma: ', int(numeroUno) + int(numeroDos))#Aqui si se suma

#otra forma:
print('-----> conversion <-----')
numeroTres = int(input('Introduce primer numero: '))
numeroCuatro = int(input('Introduce segundo numero: '))
result = numeroTres + numeroCuatro
print('El resultado de la suma', result)