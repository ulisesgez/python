print('-----> types <-----')
"""
Inmutable:
- Numeric Data Tyoes:
    * int
    * float
    * complex
- Sequences:
    * str
    * tuple
- Sets:
    * frozenset
- (range)
- (bytes)

Mutable:
- Sequences:
    * list
- Mappings:
    * dict
- Sets:
    * set
- (bytearray)

Literales:
Un literal se refiere a datos cuyos valores están determinados por el literal mismo.

Debido a que es un concepto un poco difícil de entender, un buen ejemplo puede ser
muy útil.

Observa los siguientes dígitos:

123
¿Puedes adivinar qué valor representa? Claro que puedes - es ciento veintitrés.

Que tal este:

c
¿Representa algún valor? Tal vez. Puede ser el símbolo de la velocidad de la luz,
por ejemplo. También puede representar la constante de integración. Incluso la
longitud de una hipotenusa en el Teorema de Pitágoras. Existen muchas posibilidades.

No se puede elegir el valor correcto sin algo de conocimiento adicional.

Y esta es la pista: 123 es un literal, y c no lo es.

Se utilizan literales para codificar datos y ponerlos dentro del código.
Ahora mostraremos algunas convenciones que se deben seguir al utilizar Python.

Comencemos con un sencillo experimento - observa el fragmento de código en el editor.
"""
print("2")
print(2)
"""
La primera línea luce familiar. La segunda parece ser errónea debido a la falta
visible de comillas.

Intenta ejecutarlo.

Si todo salió bien, ahora deberías de ver dos líneas idénticas.

¿Qué paso? ¿Qué significa?

A través de este ejemplo, encuentras dos tipos diferentes de literales:

Una cadena, la cual ya conoces,
Y un número entero, algo completamente nuevo.
La función print() los muestra exactamente de la misma manera - Sin embargo,
internamente, la memoria de la computadora los almacena de dos maneras completamente
diferentes - La cadena existe como eso solo una cadena - una serie de letras.

El número es convertido a una representación máquina (una serie de bits).
La función print() es capaz de mostrar ambos en una forma legible para humanos.

Vamos a tomar algo de tiempo para discutir literales numéricas y su vida interna.

Enteros

Quizá ya sepas un poco acerca de como las computadoras hacen cálculos con números.
Tal vez has escuchado del sistema binario, y como es que ese es el sistema que
las computadoras utilizan para almacenar números y como es que pueden realizar
cualquier tipo de operaciones con ellos.

No exploraremos las complejidades de los sistemas numéricos posicionales,
pero se puede afirmar que todos los números manejados por las computadoras
modernas son de dos tipos:

enteros, es decir, aquellos que no tienen una parte fraccionaria,
y números punto-flotantes (o simplemente flotantes), los cuales contienen
(o son capaces de contener) una parte fraccionaría.
Esta definición no es tan precisa, pero es suficiente por ahora.
La distinción es muy importante, y la frontera entre estos dos tipos de números
es muy estricta. Ambos tipos difieren significativamente en como son almacenados
en una computadora y en el rango de valores que aceptan.

La característica del valor numérico que determina el tipo, rango y aplicación
se denomina el tipo.

Si se codifica un literal y se coloca dentro del código de Python, la forma del
literal determina la representación (tipo) que Python utilizará para almacenarlo
en la memoria.

Por ahora, dejemos los números flotantes a un lado (regresaremos a ellos pronto)
y analicemos como es que Python reconoce un número entero.

El proceso es casi como usar lápiz y papel - es simplemente una cadena de dígitos
que conforman el número. pero hay una condición - no se deben insertar caracteres
que no sean dígitos dentro del número.

Tomemos por ejemplo, el número once millones ciento once mil ciento once.
Si tomaras ahorita un lápiz en tu mano, escribirías el siguiente número:
11,111,111, o así: 11.111.111, incluso de esta manera: 11 111 111.

Es claro que la separación hace que sea más fácil de leer, especialmente cuando
el número tiene demasiados dígitos. Sin embargo, Python no acepta estas cosas,
está prohibido. ¿Qué es lo que Python permite?. El uso de guion bajo en los
literales numéricos.*

Por lo tanto, el número se puede escribir ya sea así: 11111111, o como sigue:
11_111_111.

  Nota     *Python 3.6 ha introducido el guion bajo en los literales numéricos,
  permitiendo colocar un guion bajo entre dígitos y después de especificadores
  de base para mejorar la legibilidad. Esta característica no está disponible
  en versiones anteriores de Python.

¿Cómo se codifican los números negativos en Python? Como normalmente se hace,
agregando un signo de menos. Se puede escribir: -11111111, o -11_111_111.

Los números positivos no requieren un signo positivo antepuesto, pero es permitido,
si se desea hacer. Las siguientes líneas describen el mismo número: +11111111 y 11111111.
"""
print('-----> enteros <-----')
print(int())
numero = 5
print(numero)
print(type(numero))
negativo = -40
cero = 0
bimario = 0b101010
hexadecimal = 0xFF

"""
Números octales y hexadecimales
Existen dos convenciones adicionales en Python que no son conocidas en el mundo de
las matemáticas. El primero nos permite utilizar un número en su representación octal.

Si un número entero esta precedido por un código 0O o 0o (cero-o), el número será
tratado como un valor octal. Esto significa que el número debe contener dígitos
en el rango del [0..7] únicamente.

0o123 es un número octal con un valor (decimal) igual a 83.

La función print() realiza la conversión automáticamente. Intenta esto:
"""
print(0o123)

"""
La segunda convención nos permite utilizar números en hexadecimal. Dichos números
deben ser precedidos por el prefijo 0x o 0X (cero-x).

0x123 es un número hexadecimal con un valor (decimal) igual a 291.
La función print() puede manejar estos valores también. Intenta esto:
"""
print(0x123)
"""
Flotantes:
Ahora es tiempo de hablar acerca de otro tipo, el cual esta designado para
representar y almacenar los números que (como lo diría un matemático) tienen
una parte decimal no vacía.

Son números que tienen (o pueden tener) una parte fraccionaria después del
punto decimal, y aunque esta definición es muy pobre, es suficiente para lo
que se desea discutir.

Cuando se usan términos como dos y medio o menos cero punto cuatro, pensamos en
números que la computadora considera como números punto-flotante:

2.5
-0.4
Nota: dos punto cinco se ve normal cuando se escribe en un programa, sin embargo
si tu idioma nativo prefiere el uso de una coma en lugar de un punto, se debe
asegurar que el número no contenga comas.

Python no lo aceptará, o (en casos poco probables) puede malinterpretar el número,
debido a que la coma tiene su propio significado en Python.

Si se quiere utilizar solo el valor de dos punto cinco, se debe escribir como
se mostró anteriormente. Nota que: hay un punto entre el 2 y el 5, no una coma.

Como puedes imaginar, el valor de cero punto cuatro puede ser escrito en Python como:

0.4
Pero no hay que olvidar esta sencilla regla - se puede omitir el cero cuando
es el único dígito antes del punto decimal.

En esencia, el valor 0.4 se puede escribir como:

.4

Por ejemplo: el valor de 4.0 puede ser escrito como:

4.

Esto no cambiará su tipo ni su valor.
"""

print('-----> flotantes <-----')
print(float())
flotante = 5.5
print(type(flotante))
#precision decimal:
a = 3.3
print(a)
b = 1.1 + 2.2
print(b)
print(a == b)#False
#entonces como los comparamos, de forma brusca podemos recortar la presicion, pero este pasa a ser un string:
bStr = format(b, ".2g")
print(bStr)
#no podemos comparar un string con entero, asi que:
print(bStr == str(a))#True

#ahora de una forma mas amtematica:
tolerance = 0.00001
print(abs(a - b) < tolerance)#True

"""
Enteros vs Flotantes
El punto decimal es esencialmente importante para reconocer números
punto-flotantes en Python.

Observa estos dos números:

4
4.0
Se puede pensar que son idénticos, pero Python los ve de una manera completamente
distinta.

4 es un número entero mientras que 4.0 es un número punto-flotante.

El punto decimal es lo que determina si es flotante.

Por otro lado, no solo el punto hace que un número sea flotante. Se puede utilizar
la letra e.

Cuando se desea utilizar números que son muy pequeños o muy grandes, se puede
implementar la notación científica.

Por ejemplo, la velocidad de la luz, expresada en metros por segundo.
Escrita directamente se vería de la siguiente manera: 300000000.

Para evitar escribir tantos ceros, los libros de texto emplean la forma abreviada,
la cual probablemente hayas visto: 3 x 108.

Se lee: tres por diez elevado a la octava potencia.

En Python, el mismo efecto puede ser logrado de una manera similar - observa lo
siguiente:

3E8

La letra E (también se puede utilizar la letra minúscula e - proviene de la palabra
exponente) la cual significa por diez a la n potencia.

Nota:

El exponente (el valor después de la E) debe ser un valor entero;
La base (el valor antes de la E) puede ser un valor entero o flotante.
Codificando Flotantes
Veamos ahora como almacenar números que son muy pequeños (en el sentido de que
están muy cerca del cero).

Una constante de física denominada La Constante de Planck (denotada como h),
de acuerdo con los libros de texto, tiene un valor de: 6.62607 x 10-34.

Si se quisiera utilizar en un programa, se debería escribir de la siguiente manera:

6.62607E-34

Nota: el hecho de que se haya escogido una de las posibles formas de
codificación de un valor flotante no significa que Python lo presentará
de la misma manera.

Python podría en ocasiones elegir una notación diferente.

Por ejemplo, supongamos que se ha elegido utilizar la siguiente notación:

0.0000000000000000000001

Cuando se corre en Python:

print(0.0000000000000000000001)
 
Output
este es el resultado:
1e-22
Output
Python siempre elige la presentación más corta del número, y esto se debe de tomar
en consideración al crear literales.

Cadenas:
Las cadenas se emplean cuando se requiere procesar texto (como nombres de cualquier
tipo, direcciones, novelas, etc.), no números.

Ya conoces un poco acerca de ellos, por ejemplo, que las cadenas requieren comillas
así como los flotantes necesitan punto decimal.

Este es un ejemplo de una cadena: "Yo soy una cadena."

Sin embargo, hay una cuestión. Cómo se puede codificar una comilla dentro de una
cadena que ya está delimitada por comillas.

Supongamos que se desea mostrar un muy sencillo mensaje:

Me gusta "Monty Python"
¿Cómo se puede hacer esto sin generar un error? Existen dos posibles soluciones.

La primera se basa en el concepto ya conocido del carácter de escape, el cual
recordarás se utiliza empleando la diagonal invertida. La diagonal invertida
puede también escapar de la comilla. Una comilla precedida por una diagonal
invertida cambia su significado - no es un limitador, simplemente es una comilla.
Lo siguiente funcionará como se desea:
"""
print("Me gusta \"Monty Python\"")

"""
Nota: ¿Existen dos comillas con escape en la cadena - puedes observar ambas?

La segunda solución puede ser un poco sorprendente. Python puede utilizar
una apóstrofe en lugar de una comilla. Cualquiera de estos dos caracteres
puede delimitar una cadena, pero para ello se debe ser consistente.

Si se delimita una cadena con una comilla, se debe cerrar con una comilla.

Si se inicia una cadena con un apóstrofe, se debe terminar con un apóstrofe.

Este ejemplo funcionará también:
"""
print('Me gusta "Monty Python"')
"""
Nota: en este ejemplo no se requiere nada de escapes.

Codificando Cadenas
Ahora, la siguiente pregunta es: ¿Cómo se puede insertar un apóstrofe en una 
cadena la cual está limitada por dos apóstrofes?

A estas alturas ya se debería tener una posible respuesta o dos.

Intenta imprimir una cadena que contenga el siguiente mensaje:

I'm Monty Python.
"""
print('I\'m Monty Python.')
"""
Como se puede observar, la diagonal invertida es una herramienta 
muy poderosa - puede escapar no solo comillas, sino también apóstrofes.

Ya se ha mostrado, pero se desea hacer énfasis en este fenómeno una vez mas: 
una cadena puede estar vacía - puede no contener carácter alguno.

Una cadena vacía sigue siendo una cadena:
''
""

Booleanos
Para concluir con los literales de Python, existen dos más.

No son tan obvios como los anteriores y se emplean para representar un valor 
muy abstracto - la veracidad.

Cada vez que se le pregunta a Python si un número es más grande que otro, el 
resultado es la creación de un tipo de dato muy específico - un valor booleano.

El nombre proviene de George Boole (1815-1864), el autor de Las Leyes del 
Pensamiento, las cuales definen el Álgebra Booleana - una parte del álgebra 
que hace uso de dos valores: True y False, denotados como 1 y 0.

Un programador escribe un programa, y el programa hace preguntas. 
Python ejecuta el programa, y provee las respuestas. 
El programa debe ser capaz de reaccionar acorde a las respuestas recibidas.

Afortunadamente, las computadoras solo conocen dos tipos de respuestas:

Si, esto es verdad.
No, esto es falso.
Nunca habrá una respuesta como: No lo sé o probablemente si, pero no estoy seguro.

Python, es entonces, un reptil binario.

Estos dos valores booleanos tienen denotaciones estrictas en Python:

True
False

No se pueden cambiar - se deben tomar estos símbolos como son, incluso respetando 
las mayúsculas y minúsculas.

"""

print('-----> boolean <-----')
#false:
not True
not 15
not -15
not 'hello'
not [1, 2, 3, 4, 5]

#true:
not False
not 0
not 0.0
not ''
not []

print('-----> boolean <-----')
booleano = True
print(booleano)
print(type(booleano))

print('-----> boolean <-----')
mayorQue = 1 > 2
print(mayorQue)
print(type(mayorQue))

print('-----> boolean <-----')
if mayorQue:
    print('verdadero')
else:
    print('falso')
print(type(mayorQue))

print('-----> boolean with is methods<-----')
print('Python'.isupper())
print('Python'.islower())
print('Python'.istitle())

print('-----> boolean / contencion <-----')
entero = 2 in [1, 2, 3, 4, 5]
flotante = 2.5 in [1, 2, 3, 4, 5]
listaTupla = [1, 2] in [1, 2, 3, 4, 5]
listaTupla = 1 in [(0, 1), (2, 3)]
listaTupla = (0, 1) in [(0, 1), (2, 3)]
seq = [(0, 1), (2, 3)]
seqResultado = 1 in seq
holaMundo = 'h' in 'helloWorld'
print(holaMundo)
python = 'Py' in 'Python'
print(python)

"""
Operadores cadena
Es tiempo de regresar a estos dos operadores aritméticos: + y *.

Ambos tienen una función secundaría. Son capaces de hacer algo 
más que sumar y multiplicar.

Los hemos visto en acción cuando sus argumentos son (flotantes o enteros, 
no hay diferencia).

Ahora veremos que son capaces también de manejar o manipular cadenas, aunque, 
en una manera muy específica.

El signo de + (más), al ser aplicado a dos cadenas, se convierte en un operador 
de concatenación:

string + string

Simplemente concatena (junta) dos cadenas en una. Por supuesto, 
puede ser utilizado más de una vez en una misma expresión, y en tal 
contexto se comporta con enlazado del lado izquierdo.

En contraste con el operador aritmético, el operador de concatenación 
no es conmutativo, por ejemplo, "ab" + "ba" no es lo mismo que "ba" + "ab".

No olvides, si se desea que el signo + sea un concatenador, no un sumador, 
solo se debe asegurar que ambos argumentos sean cadenas.

No se pueden mezclar los tipos de datos aquí.

Este sencillo programa muestra el signo + en su segundo uso:
"""
fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + fnam + " " + lnam + ".")

"""
Nota: el usar + para concatenar cadenas te permite construir la salida de
una manera más precisa que con una función print() pura, incluso si está 
enriquecida con end= y sep= argumentos de palabras clave.

Replicación
El signo de * (asterisco), cuando es aplicado a una cadena y a un número 
(o a un número y cadena) se convierte en un operador de replicación:


string * number
number * string
 
Replica la cadena el numero de veces indicado por el número.

Por ejemplo:

"James" * 3 produce "JamesJamesJames"
3 * "an" produce "ananan"
5 * "2" (o "2" * 5) produce "22222" (no 10!)
  Recuerda  
Un número menor o igual a cero produce una cadena vacía.

Este sencillo programa "dibuja" un rectángulo, haciendo uso del antiguo 
operador (+) en un nuevo rol:

"""
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

print('-----> string <-----')
print(str())
cadenaTexto = 'cadenaTexto'
print(cadenaTexto)
#ver tipo de variable:
print(type(cadenaTexto))

print('-----> listas <-----')
print(complex())

print('-----> listas <-----')
print(list())

print('-----> set <-----')
print(set())

print('-----> functions <-----')

bimarioDos = bin(15)
octal = oct(8)
hexadecimalDos = hex(65535)

print('-----> built in function <-----')
help(bin)