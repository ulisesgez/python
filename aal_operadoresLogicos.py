#Nos permitiran comparar dos expreseiones bolleanas:
a = True
b = False

#and, todos deben ser verdaderos para que sea verdadero:
result = a and b
print(result)

#or, almenos uno debe ser verdadero para que sea verdadero:
result = a or b
print(result)

#not, invetimos el valor de true o false:
result = not a
print(result)
#comprobamos que ambas ya son falsos:
test = result or b
print(test)