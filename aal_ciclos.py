#while:
"""
#Se imprime infinitamente 'ejecutando while', ya que siempre es true:
condicion = True

while condicion:
    print('ejecutando while')
else:
    print('fin ciclo while')
"""

contador = 0

while contador < 3:
    print(contador)
    contador += 1
else:
    print('fin ciclo while')

#for:
cadena = 'hola'

for letra in cadena:
    print(letra)
else:
    print('fin ciclo for')