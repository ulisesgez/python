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

toma sus argumentos (puede aceptar más de un argumento y también puede aceptar menos
de un argumento) los convierte a un formato legible si es necesario
(como puedes sospechar, las cadenas no requieren esta acción, ya que la cadena ya es
legible)
y envía los datos resultantes al dispositivo de salida (normalmente la consola);
en otras palabras, todo lo que pongas en la función print() se aparecerá en tu pantalla.
No es de extrañar entonces que, de ahora en adelante, utilices print() muy intensamente
para ver los resultados de sus operaciones y evaluaciones.

2. ¿Qué argumentos espera print()?

Cualquiera. Pronto te mostraremos que print() puede operar con prácticamente todos los
tipos de datos que ofrece Python. Cadenas, números, caracteres, valores lógicos,
objetos - cualquiera de estos se puede pasar con éxito a print().

3. ¿Qué valor devuelve la función print()?

Ninguno. Su efecto es suficiente.

Usando múltiples argumentos
Hasta ahora hemos probado el comportamiento de la función print() sin argumentos y con
un argumento. También vale la pena intentar alimentar a la función print() con más de
un argumento.

Mira la ventana del editor. Esto es lo que vamos a probar ahora:

"""
print("La Witsi Witsi Araña" , "subió" , "a su telaraña.")
"""
Hay una invocación de la función print(), pero contiene tres argumentos. Todos ellos son cadenas.

Los argumentos están separados por comas. Los hemos rodeado de espacios para hacerlos más visibles, pero no es realmente necesario, y no lo haremos más.

En este caso, las comas al separar los argumentos juega un papel completamente diferente al de la coma dentro de la cadena. El primero es parte de la sintaxis de Python, mientras que el segundo está diseñado para mostrarse en la consola.

Si observas el código nuevamente, verás que hay no hay espacios dentro de las cadenas.

Los espacios, eliminados de las cadenas, han vuelto a aparecer. ¿Puedes explicar por qué?

Dos conclusiones emergen de este ejemplo:

La función print() invocada con más de un argumento los muestra todos en una sola línea.
La función print() pone un espacio entre los argumentos de salida por iniciativa propia.

Argumentos posicionales
Ahora que sabes un poco sobre las costumbres de la función print(), te mostraremos cómo cambiarlas.

Deberías poder predecir la salida sin ejecutar el código en el editor.
"""
print("Mi nombre es", "Python.")
print("Monty Python.")

"""
La forma en que estamos pasando los argumentos a la función print() es la más común en Python, y se llama la forma posicional. Este nombre proviene del hecho de que el significado del argumento está dictado por su posición (por ejemplo, el segundo argumento se mostrará después del primero, no al revés).

Ejecuta el código y comprueba si el resultado coincide con tus predicciones.

Argumentos de palabra clave
Python ofrece otro mecanismo para el paso de argumentos, que puede ser útil cuando deseas convencer a la función print() para que cambie un poco su comportamiento.

No vamos a explicarlo en profundidad ahora. Planeamos hacerlo cuando hablemos de funciones. Por ahora, simplemente queremos mostrarte cómo funciona. Siéntete libre de usarlo en tus propios programas.

El mecanismo se llama argumentos de palabras clave. El nombre proviene del hecho de que el significado de estos argumentos se toma no de su ubicación (posición) sino de la palabra especial (palabra clave) utilizada para identificarlos.

La función print() tiene dos argumentos de palabra clave que puedes usar para tus propósitos. El primero se llama end.

En la ventana del editor puedes ver un ejemplo muy simple de cómo usar un argumento de palabra clave.
"""
print("Mi nombre es", "Python.", end=" ")
print("Monty Python.")

"""
Para usarlo, es necesario conocer algunas reglas:

Un argumento de palabra clave consta de tres elementos: una palabra clave se identifica el argumento (end aquí); un signo de igual (=); y un valor asignado a ese argumento;
cualquier argumento de palabra clave debe colocarse después del último argumento posicional (esto es muy importante)
En nuestro ejemplo, hemos utilizado el argumento de palabra clave end, y lo hemos configurado como cadena que contiene un espacio.

Como puedes ver, el argumento de palabra clave end determina los caracteres que la función print() envía a la salida una vez que llega al final de sus argumentos posicionales.

El comportamiento predeterminado refleja la situación en la que el argumento de palabra clave end se usa implícitamente de la siguiente manera: end="\n".


Y ahora es el momento de intentar algo más difícil.

Si miras con atención, verás que hemos usado el argumento end, pero la cadena que se le asignó está vacía (no contiene ningún carácter).

¿Qué sucederá ahora? Ejecuta el programa en el editor para averiguarlo.
"""
print("Mi nombre es ", end="")
print("Monty Python.")

"""
Como el argumento end se ha establecido a nada, la función print() tampoco genera nada, una vez que se han agotado sus argumentos posicionales.

Nota: no se han enviado líneas nuevas a la salida.

La cadena asignada al argumento de palabra clave end puede ser de cualquier longitud. Experimenta con él si quieres.

Dijimos anteriormente que la función print() separa sus argumentos de salida con espacios. Este comportamiento también se puede cambiar.

El argumento de palabra clave que puede hacer esto se denomina sep (como en separador).

Mira el código en el editor, y ejecútalo.
"""
print("Mi", "nombre", "es", "Monty", "Python.", sep="-")

"""
La función print() ahora usa un guión, en lugar de un espacio, para separar los argumentos de salida.

Nota: el valor del argumento sep también puede ser una cadena vacía. Pruébalo tu mismo.

Ambos argumentos de palabra clave pueden mezclarse en una invocación, como aquí en la ventana del editor.


"""
print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

"""

El ejemplo no tiene mucho sentido, pero presenta de forma visible las interacciones entre end y sep.

¿Puedes predecir el resultado?

Ejecuta el código y comprueba si coincide con tus predicciones.

Ahora que comprendes la función print(), estás listo para considerar cómo almacenar y procesar datos en Python.

Sin print(), no podrías ver ningún resultado."""

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