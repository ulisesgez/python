print('-----> def <-----')
def hola():
    print('hola mundo')
    print('ultimate python course')

hola()


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

#otro ejemplo con parametros yb argumentos:
#parametros:
def adios(nombre = 'pedro'):
    print(f'adios {nombre}')
#argumentos:
adios('ulises')

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

#argumentos variables llave-valor, tambien como en el caso anterior podriamos colocar **terminos:
def listaTerminos(**kwargs):
    for llave, valor in kwargs.items():
        print(f'{llave}: {valor}')

listaTerminos(IDE = 'Itegrated Development Enviroment', PK = 'Primary Key')
listaTerminos(DBMS = 'Database Management  System')

#distintos tipos de datos como argumentos:
def desplagarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ['juan', 'carla', 'guillermo']
desplagarNombres(nombres)
desplagarNombres('carlos')
#desplagarNombres(10)#no iterable
desplagarNombres((10, 11))#tupla
desplagarNombres([12, 13])#lista

#funcion recursiva:
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)
resultado = factorial(5)
print(f'El factorial de 5 es: {resultado}')