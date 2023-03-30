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
def sumar(a, b):
    return a + b
resSum = sumar(5, 3)
print(resSum)

#valores por default:
def restar(c = 10, d = 2):
    return c - d
resRes = restar()
print(resRes)
print(restar(15, 5))