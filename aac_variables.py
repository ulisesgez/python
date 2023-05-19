"""
Variables – cajas con forma de datos
Es justo que Python nos permita codificar literales las cuales contengan valores
numéricos y cadenas.

Ya hemos visto que se pueden hacer operaciones aritméticas con estos números: sumar,
restar, etc. Esto se hará una infinidad de veces en un programa.

Pero es normal preguntar como es que se pueden almacenar los resultados de estas
operaciones, para poder emplearlos en otras operaciones, y así sucesivamente.

¿Cómo almacenar los resultados intermedios, y después utilizarlos de nuevo para
producir resultados subsecuentes?

Python ayudará con ello. Python ofrece "cajas" (o "contenedores") especiales para
este propósito, estas cajas son llamadas variables ‒ el nombre mismo sugiere que el
contenido de estos contenedores puede variar en casi cualquier forma.

¿Cuáles son los componentes o elementos de una variable en Python?

Un nombre;
Un valor (el contenido del contenedor)
Comencemos con lo relacionado al nombre de la variable.

Las variables no aparecen en un programa automáticamente. Como desarrollador,
tu debes decidir cuantas variables deseas utilizar en tu programa.

También las debes de nombrar.

Nombres de Variables
Si se desea nombrar una variable, se deben seguir las siguientes reglas:

El nombre de la variable debe de estar compuesto por MAYÚSCULAS, minúsculas, dígitos,
y el carácter _ (guion bajo)
El nombre de la variable debe comenzar con una letra;
El carácter guion bajo es considerado una letra;
Las mayúsculas y minúsculas se tratan de forma distinta (un poco diferente que en el
mundo real - Alicia y ALICIA son el mismo nombre, pero en Python son dos nombres de
variable distintos, subsecuentemente, son dos variables diferentes);
El nombre de las variables no pueden ser igual a alguna de las palabras reservadas de
Python (las palabras clave - explicará más de esto pronto).
Nota que la misma restricción aplica a los nombres de funciones.

Python no impone restricciones en la longitud de los nombres de las variables,
pero eso no significa que un nombre de variable largo sea mejor que uno corto.

Aquí se muestran algunos nombres de variable que son correctos, pero que no siempre
son convenientes:

MyVariable
i
l
t34
Exchange_Rate
counter
days_to_christmas
TheNameIsTooLongAndHardlyReadable
_
Estos nombres de variables también son correctos:

Adiós_Señora
sûr_la_mer
Einbahnstraße
переменная.
Python te permite usar no solo letras latinas sino también caracteres específicos de
idiomas que usan otros alfabetos.
Ahora veamos algunos nombres incorrectos:

10t (no comienza con una letra)
!important (no comienza con una letra)
exchange rate (contiene un espacio).

El PEP 8 -- Style Guide for Python Code recomienda la siguiente convención de
nomenclatura para variables y funciones en Python:

Los nombres de las variables deben estar en minúsculas, con palabras separadas por
guiones bajos para mejorar la legibilidad (por ejemplo, var, my_variable)
Los nombres de las funciones siguen la misma convención que los nombres de las
variables (por ejemplo, fun, my_function)
También es posible usar letras mixtas (por ejemplo, myVariable), pero solo en contextos
donde ese ya es el estilo predominante, para mantener la compatibilidad retroactiva
con la convención adoptada.

Palabras Clave
Observa las palabras que juegan un papel muy importante en cada programa de Python.

['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def',
'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import',
'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
'while', 'with', 'yield']

Son llamadas palabras clave o (mejor dicho) palabras clave reservadas. Son reservadas
porque no se deben utilizar como nombres: ni para variables, ni para funciones,
ni para cualquier otra cosa que se desee crear.

El significado de la palabra reservada está predefinido, y no debe cambiar.

Afortunadamente, debido al hecho de que Python es sensible a mayúsculas y minúsculas,
cualquiera de estas palabras se pueden modificar cambiando una o varias letras de
mayúsculas a minúsculas o viceversa, creando una nueva palabra, la cual no esta
reservada.

Por ejemplo - no se puede nombrar a la variable así:

import

No se puede tener una variable con ese nombre - esta prohibido. pero se puede hacer lo
siguiente:

Import

Estas palabras podrían parecer un misterio ahorita, pero pronto se aprenderá acerca de
su significado.

Cómo crear una variable
¿Qué se puede poner dentro de una variable?

Cualquier cosa.

Se puede utilizar una variable para almacenar cualquier tipo de los valores que ya se
han mencionado, y muchos mas de los cuales aun no se han explicado.

El valor de la variable en lo que se ha puesto dentro de ella. Puede variar tanto como
se necesite o requiera. El valor puede ser entero, después flotante, y eventualmente
ser una cadena.

Hablemos de dos cosas importantes - como son creadas las variables, y como poner
valores dentro de ellas (o mejor dicho, como dar o pasarles valores).

Una variable se crea cuando se le asigna un valor. A diferencia de otros lenguajes
de programación, no es necesario declararla.

Si se le asigna cualquier valor a una variable no existente, la variable será
automáticamente creada. No se necesita hacer algo más.

La creación (o su sintaxis) es muy simple: solo utiliza el nombre de la variable
deseada, después el signo de igual (=) y el valor que se desea colocar dentro de la
variable.

Observa el fragmento en el editor:
"""
var = 1
print(var)
"""
Consiste de dos simples instrucciones:

La primera crea una variable llamada var, y le asigna un literal con un valor entero
de 1.
La segunda imprime el valor de la variable recientemente creada en la consola.
Como puedes ver, print() tiene otro lado: también puede manejar variables.
¿Sabes cuál será el resultado del fragmento? Ejecuta el código para verificar.

Cómo emplear una variable
Se tiene permitido utilizar cuantas declaraciones de variables sean necesarias para
lograr el objetivo del programa, por ejemplo:
"""
var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)
"""
Sin embargo, no se permite utilizar una variable que no exista, (en otras palabras,
una variable a la cual no se le ha dado un valor).

Este ejemplo ocasionará un error:
"""
var = 1
print(Var)

"""
Se ha tratado de utilizar la variable llamada Var, la cual no tiene ningún valor
(nota: var y Var son entidades diferentes, y no tienen nada en común dentro de Python).

  RECUERDA  
Se puede utilizar print() para combinar texto con variables utilizando
el operador + para mostrar cadenas con variables, por ejemplo:
"""
var = "3.8.5"
print("Python version: " + var)

"""
Cómo asignar un nuevo valor a una variable ya existente
¿Cómo se le asigna un valor nuevo a una variable que ya ha sido creada? De la misma
manera. Solo se necesita el signo de igual.

El signo de igual es de hecho un operador de asignación. Aunque esto suene un poco
extraño, el operador tiene una sintaxis simple y una interpretación clara y precisa.

Asigna el valor del argumento de la derecha al de la izquierda, aún cuando el argumento
de la derecha sea una expresión arbitraria compleja que involucre literales, operadores
y variables definidas anteriormente.

Observa el siguiente código:
"""
var = 1
print(var)
var = var + 1
print(var)

"""
El código envía dos líneas a la consola:

1
2

La primer línea del código crea una nueva variable llamada var y
le asigna el valor de 1.

La sentencia se lee de la siguiente manera: asigna el valor de 1 a una variable
llamada var.

De manera más corta: asigna 1 a var.

Algunos prefieren leer el código así: var se convierte en 1.

La tercera línea le asigna a la misma variable un nuevo valor tomado de la variable
misma, sumándole 1.Al ver algo así, un matemático
probablemente protestaría - ningún valor puede ser igualado a si mismo más uno.
Esto es una contradicción. Pero Python trata el signo = no como igual a, sino como
asigna un valor.

Entonces, ¿Cómo se lee esto en un programa?

Toma el valor actual de la variable var, sumale 1 y guárdalo en la variable var.

En efecto, el valor de la variable var ha sido incrementado por uno, lo cual no
está relacionado con comparar la variable con otro valor.

¿Puedes predecir cuál será el resultado del siguiente fragmento de código?
"""
var = 100
var = 200 + 300
print(var)

"""
500 ‒ ¿por qué? Bueno, primero, se crea la variable var y se le asigna un valor de 100.
Luego, a la misma variable se le asigna un nuevo valor: el resultado de sumar 200 a 300,
que es 500.
"""