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

#numero a texto:
print('-----> conversion <-----')
numero = int(input('Proporciona un valor del 1 al 3: '))
numeroTexto = ''
if numero == 1:
    numeroTexto = 'numero uno'
elif numero == 2:
    numeroTexto = 'numero dos'
elif numero == 3:
    numeroTexto = 'numero tres'
else:
    numeroTexto = 'valor fuera de rango'

print('-----> conversion <-----')
numeroUno = 1
numeroDos = 2
print('numero 1: ', numeroUno, 'numero 2: ', numeroDos)
print('suma: ', numeroUno + numeroDos)
print('concatenacion: ', str(numeroUno) + str(numeroDos))

print('-----> conversion <-----')
name = 'ulises'
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))

print('-----> conversion <-----')
print('ulises' + 'gutierrez')
print(10 + 20)
print('ulises' + 10)#Error
#solucion a lo anterior:
age = 12
print('Mi edad es: ' + str(age))
print(f'Mi edad es: {age}')

age = input('Escribe tu edad: ')
print(type(age))
age = int(age)
print(f'Tu edad en 10 años sera: {age}')