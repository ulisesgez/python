"""
Funciones:

¿De dónde provienen las funciones?

Pueden venir de Python mismo. La función print es una de este tipo; dicha función es
un valor agregado de Python junto con su entorno (está integrada); no tienes que hacer
nada especial (por ejemplo, pedirle a alguien algo) si quieres usarla;

Pueden provenir de uno o varios de los módulos; de Python llamados complementos algunos
de los módulos vienen con Python, otros pueden requerir una instalación por separado
- cual sea el caso, todos deben estar conectados explícitamente con el código
(te mostraremos cómo hacer esto pronto);

Puedes escribirlas tú mismo, colocando tantas funciones como desees y necesites dentro
de su programa para hacerlo más simple, claro y elegante.

El nombre de la función debe ser significativo (el nombre de la función print es 
evidente) imprime en la terminal.

Si vas a utilizar alguna función ya existente, no podrás modificar su nombre, pero
cuando comiences a escribir tus propias funciones, debes considerar cuidadosamente la
elección de nombres.

Argumentos de funciones
Como se dijo anteriormente, una función puede tener:

Un efecto;
Un resultado.
También existe un tercer componente de la función, muy importante - el o los argumento(s).

Las funciones matemáticas usualmente toman un argumento. por ejemplo, sen(x) toma una x,
que es la medida de un ángulo.

Las funciones de Python, por otro lado, son más versátiles. Dependiendo de las
necesidades individuales, pueden aceptar cualquier cantidad de argumentos - tantos como
sea necesario para realizar sus tareas. Nota: Cuando dijimos cualquier número, eso
incluye el cero - algunas funciones de Python no necesitan ningún argumento.

A pesar del número de argumentos necesarios o proporcionados, las funciones de Python
demandan fuertemente la presencia de un par de paréntesis - el de apertura y de cierre,
respectivamente.
Si deseas entregar uno o más argumentos a una función, colócalos dentro de los paréntesis.
Si vas a utilizar una función que no tiene ningún argumento, aún tiene que tener los
paréntesis.

¿Qué sucede cuando Python encuentra una invocación como la que está a continuación?

function_name(argument)

Veamos:

- Primero, Python comprueba si el nombre especificado es legal (explora sus datos
internos para encontrar una función existente del nombre; si esta búsqueda falla,
Python aborta el código)
- En segundo lugar, Python comprueba si los requisitos de la función para el número de
argumentos le permiten invocar la función de esta manera (por ejemplo, si una función
específica exige exactamente dos argumentos, cualquier invocación que entregue solo un
argumento se considerará errónea y abortará la ejecución del código)
- Tercero, Python deja el código por un momento y salta dentro de la función que se
desea invocar; por lo tanto, también toma los argumento(s) y los pasa a la función;
- Cuarto, la función ejecuta el código, provoca el efecto deseado (si lo hubiera),
evalúa el (los) resultado(s) deseado(s) y termina la tarea;
- Finalmente, Python regresa al código (al lugar inmediatamente después de la invocación)
y reanuda su ejecución.

La función print() y su efecto, argumentos, y valores retornados.

Hay que responder a tres preguntas importantes lo antes posible:

1. ¿Qué efecto tiene la función print()?

El efecto es muy útil y muy espectacular. La función:

toma sus argumentos (puede aceptar más de un argumento y también puede aceptar menos de un argumento)
los convierte a un formato legible si es necesario (como puedes sospechar, las cadenas no requieren esta acción, ya que la cadena ya es legible)
y envía los datos resultantes al dispositivo de salida (normalmente la consola); en otras palabras, todo lo que pongas en la función print() se aparecerá en tu pantalla.
No es de extrañar entonces que, de ahora en adelante, utilices print() muy intensamente para ver los resultados de sus operaciones y evaluaciones.

2. ¿Qué argumentos espera print()?

Cualquiera. Pronto te mostraremos que print() puede operar con prácticamente todos los tipos de datos que ofrece Python. Cadenas, números, caracteres, valores lógicos, objetos - cualquiera de estos se puede pasar con éxito a print().

3. ¿Qué valor devuelve la función print()?

Ninguno. Su efecto es suficiente.
"""

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