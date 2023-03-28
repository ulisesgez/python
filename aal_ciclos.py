print('-----> while <-----')
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

print('-----> while <-----')
#Inicializar variable a nada.
respuesta = None

while respuesta != 'a' and respuesta != 'b' and respuesta != 'c':
    respuesta = input('Que opcion prefieres a), b) y c): ')

if respuesta == 'a':
    print('has elegido bien')
elif respuesta == 'b':
    print('pudiste haber elegido mejor')
elif respuesta == 'c':
    print('elegiste mal')
else:
    print('no me has dado una rspuesta con sentido')

print('-----> for <-----')
cadena = 'hola'

for letra in cadena:
    print(letra)
else:
    print('fin ciclo for')