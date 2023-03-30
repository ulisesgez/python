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

#argumentos variables:
#no sabemos el numero de parametros, anteponemos el asterisco:
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)

listarNombres('juan', 'mises', 'ulises', 'jesus')
listarNombres('maria', 'jose')

#otro ejemplo, ahora con args, es lo mismo solo es un distintivo, podriamos poner *miTupla por ejemplo:
def sumarValores (*args):
    resultado = 0
    #iteramos:
    for valor in args:
        #resultado = resultado + valor:
        resultado += valor
    return resultado

print(sumarValores(5, 5, 5))

#otro ejemplo *args
def multiplicarValores(*numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado

print(multiplicarValores(2, 2, 2, 2, 2, 2, 2))