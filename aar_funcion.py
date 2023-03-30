print('-----> def <-----')
#definor funcion:

def miFuncion():
    print('heloWorldinPython')

#mandar a llamar:
miFuncion()

#parametros:
def miFuncion(nombre, apellido):
    print(f'{nombre} {apellido}')

#mandar a llamar:
miFuncion('ulises', 'gutierrez')
miFuncion('juan', 'perez')

#return:
def suma(a, b):
    return a + b
resultado = suma(5, 3)
print(resultado)