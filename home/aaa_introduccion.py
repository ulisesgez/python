"""
Introducción a la programación:

La programación es el proceso de diseñar y escribir instrucciones que una computadora puede entender y ejecutar.
Estas instrucciones, llamadas programas, le permiten a la computadora realizar tareas específicas,
desde operaciones matemáticas simples hasta funciones complejas como manejar una página web o controlar un robot.
Aunque las computadoras son muy potentes, no entienden conceptos por sí solas;
necesitan que se les indique exactamente qué hacer, paso a paso.
"""
# Calcular la velocidad promedio de un viaje
distancia = 150  # kilómetros
tiempo = 3       # horas

velocidad = distancia / tiempo
print("Velocidad promedio:", velocidad, "km/h")
"""
Lenguajes naturales vs. lenguajes de programación:

Un lenguaje es un sistema de comunicación que permite expresar ideas.
Los humanos usan lenguajes naturales (como el español o el inglés), mientras que las computadoras usan
lenguajes de programación para entender instrucciones. Estos lenguajes son más estructurados y formales
que los naturales, y están diseñados para ser interpretados o traducidos por una máquina.

Los lenguajes de programación permiten escribir instrucciones comprensibles tanto para el programador como,
con ayuda de traductores (como compiladores o intérpretes), para la computadora.
A diferencia del lenguaje máquina, que es difícil de leer para los humanos,
los lenguajes de alto nivel como Python son más accesibles y expresivos.
"""
# Programa en lenguaje de alto nivel (Python) para sumar dos números
a = 10
b = 5
suma = a + b
print("La suma es:", suma)
"""
Compilación vs. Interpretación:

Los programas escritos en lenguajes de alto nivel, como Python o C, no pueden ser entendidos directamente
por una computadora. Por eso, necesitan ser traducidos a lenguaje máquina. Existen dos formas principales
de hacer esta traducción:

Compilación: Traduce todo el código fuente de una vez a lenguaje máquina, generando un archivo ejecutable.
Esto ocurre antes de que se ejecute el programa.

Interpretación: Traduce y ejecuta el código línea por línea en tiempo real, mientras el programa se está ejecutando.

Ambos modelos tienen ventajas y desventajas. La compilación genera programas más rápidos y portables
(como archivos .exe), pero requiere tiempo de traducción. La interpretación permite una ejecución más flexible
y directa, ideal para pruebas rápidas y aprendizaje, aunque con menor rendimiento.
"""
# Python es un lenguaje interpretado
nombre = input("¿Cómo te llamas? ")
print("Hola,", nombre)

"""




¿Qué significa todo esto para ti?

Python es un lenguaje interpretado. Esto significa que hereda todas las ventajas y
desventajas descritas. Por supuesto, agrega algunas de sus características únicas
a ambos conjuntos.
Si deseas programar en Python, necesitarás el intérprete de Python. No podrás
ejecutar tu código sin él. Afortunadamente, Python es gratuito. Esta es una de
sus ventajas más importantes.

Por razones históricas, los lenguajes diseñados para ser utilizados en la
interpretación a menudo se denominan lenguajes de scripting, mientras que la
fuente los programas codificados con ellos se denominan scripts. Bien, conozcamos
a Python.

¿Qué es Python?
Python es un lenguaje de programación de alto nivel, interpretado, orientado a
objetos y de uso generalizado con semántica dinámica, que se utiliza para la



programación de propósito general.

Aunque puede que conozcas a la pitón como una gran serpiente, el nombre del
lenguaje de programación Python proviene de una vieja serie de comedia de la
BBC llamada Monty Python's Flying Circus.





En el apogeo de su éxito, el equipo de Monty Python estaba realizando sus escenas
en vivo para audiencias en todo el mundo, incluso en el Hollywood Bowl.

Dado que Monty Python es considerado uno de los dos nutrientes fundamentales para
un programador (el otro es la pizza), el creador de Python nombró el lenguaje en
honor al programa de televisión.

 ¿Quién creó Python?

 Una de las características sorprendentes de Python es el hecho de que en
 realidad es el trabajo de una persona. Por lo general, los grandes lenguajes de
 programación son desarrollados y publicados por grandes compañías que emplean a
 muchos profesionales, y debido a las normas de derechos de autor, es muy difícil
 nombrar a cualquiera de las personas involucradas en el proyecto. Python es una
 excepción.

No existen muchos lenguajes de programación cuyos autores sean conocidos por su
nombre. Python fue creado por Guido van Rossum, nacido en 1956 en Haarlem, Países
Bajos. Por supuesto, Guido van Rossum no desarrolló y evolucionó todos los
componentes de Python.

La velocidad con la que Python se ha extendido por todo el mundo es el resultado
del trabajo continuo de miles de (muy a menudo anónimos) programadores, testers,
usuarios (muchos de ellos no son especialistas en TI) y entusiastas, pero hay que
decir que la primera idea (la semilla de la que brotó Python) llegó a una cabeza:
la de Guido.

Un proyecto de programación por pasatiempo

Las circunstancias en las que se creó Python son un poco desconcertantes.
Según Guido van Rossum:

En Diciembre de 1989, estaba buscando un proyecto de programación de "pasatiempo"
que me mantendría ocupado durante la semana de Navidad. Mi oficina (...) estaría
cerrada, pero tenía una computadora en casa y no mucho más en mis manos. Decidí
escribir un intérprete para el nuevo lenguaje de scripting en el que había estado
pensando últimamente: un descendiente de ABC que atraería a los hackers de Unix/C.
Elegí Python como el título de trabajo para el proyecto, estando en un estado de
ánimo ligeramente irreverente (y un gran fanático de Monty Python's Flying Circus).
Guido van Rossum

Los objetivos de Python

En 1999, Guido van Rossum definió sus objetivos para Python:

Un lenguaje fácil e intuitivo tan poderoso como los de los principales
competidores.
De código abierto, para que cualquiera pueda contribuir a su desarrollo.
El código que es tan comprensible como el inglés simple.
Adecuado para tareas cotidianas, permitiendo tiempos de desarrollo cortos.

Unos 20 años después, está claro que todas estas intenciones se han cumplido.
Algunas fuentes dicen que Python es el lenguaje de programación más popular del
mundo, mientras que otros afirman que es el tercero o el quinto.

Python no es una lengua joven. Es maduro y digno de confianza. No es una maravilla
de un solo golpe. Es una estrella brillante en el firmamento de programación,
y el tiempo dedicado a aprender Python es una muy buena inversión.

¿Qué hace que Python sea tan especial?

¿Por qué Python?
¿Por qué los programadores, jóvenes y viejos, experimentados y novatos, quieren
usarlo? ¿Cómo fue que las grandes empresas adoptaron Python e implementaron sus
productos al usarlo?

Existen muchas razones. Ya hemos enumerado algunas de ellas, pero vamos a
enumerarlas de una manera más práctica:

es fácil de aprender - el tiempo necesario para aprender Python es más corto que
en muchos otros lenguajes; esto significa que es posible comenzar la programación
real más rápido.
es fácil de enseñar - la carga de trabajo de enseñanza es menor que la que
necesitan otros lenguajes; esto significa que el profesor puede poner más énfasis
en las técnicas de programación generales (independientes del lenguaje),
no gastando energía en trucos exóticos, extrañas excepciones y reglas
incomprensibles.
es fácil de utilizar para escribir software nuevo - a menudo es posible escribir
código más rápido cuando se emplea Python.
es fácil de entender - a menudo, también es más fácil entender el código de otra
persona más rápido si está escrito en Python.
es fácil de obtener, instalar y desplegar - Python es gratuito, abierto y
multiplataforma; no todos los lenguajes pueden presumir de eso.

¿Rivales de Python?

Python tiene dos competidores directos, con propiedades y predisposiciones
comparables. Estos son:

Perl - un lenguaje de scripting originalmente escrito por Larry Wall.
Ruby - un lenguaje de scripting originalmente escrito por Yukihiro Matsumoto.
El primero es más tradicional, más conservador que Python, y se parece a algunos
de los buenos lenguajes antiguos derivados del lenguaje de programación C clásico.

En contraste, este último es más innovador y está más lleno de ideas nuevas.
Python se encuentra en algún lugar entre estas dos creaciones.

Internet está lleno de foros con discusiones infinitas sobre la superioridad de
uno de estos tres sobre los otros, por si deseas obtener más información sobre
cada uno de ellos.

¿Dónde podemos ver a Python en acción?

Lo vemos todos los días y en casi todas partes. Se utiliza ampliamente para
implementar complejos Servicios de Internet como motores de búsqueda,
almacenamiento en la nube y herramientas, redes sociales, etc. Cuando utilizas
cualquiera de estos servicios, en realidad estás muy cerca de Python.

Muchas herramientas de desarrollo se implementan en Python. Cada vez se escriben
más aplicaciones de uso diario en Python. Muchos científicos han abandonado las
costosas herramientas patentadas y se han cambiado a Python. Muchos testers de
proyectos de TI han comenzado a usar Python para llevar a cabo procedimientos de
prueba repetibles. La lista es larga.

¿Por qué no Python?

A pesar de la creciente popularidad de Python, todavía existen algunos nichos en
los que Python está ausente o rara vez se ve:

Programación de bajo nivel (a veces llamada programación "cercana al metal"):
si deseas implementar un controlador o motor gráfico extremadamente efectivo,
no se usaría Python.
Aplicaciones para dispositivos móviles: este territorio aún está a la espera de
ser conquistado por Python, lo más probable es que suceda algún día.

Existe más de un Python

Python 2 vs. Python 3
Existen dos tipos principales de Python, llamados Python 2 y Python 3.

Python 2 es una versión anterior del Python original. Su desarrollo se ha
estancado intencionalmente, aunque eso no significa que no haya actualizaciones.
Por el contrario, las actualizaciones se emiten de forma regular, pero no
pretenden modificar el idioma de manera significativa. Prefieren arreglar
cualquier error recién descubierto y agujeros de seguridad. La ruta de desarrollo
de Python 2 ya ha llegado a un callejón sin salida, pero Python 2 en sí todavía
está muy vivo.

Python 3 es la versión más nueva (para ser precisos, la actual) del lenguaje.
Está atravesando su propio camino de evolución, creando sus propios estándares
y hábitos.

Estas dos versiones de Python no son compatibles entre sí. Las secuencias de
comandos de Python 2 no se ejecutarán en un entorno de Python 3 y viceversa,
por lo que si deseas que un intérprete de Python 3 ejecute el código Python 2
anterior, la única solución posible es volver a escribirlo, no desde cero, por
supuesto. Grandes partes del código pueden permanecer intactas, pero tienes que
revisar todo el código para encontrar todas las incompatibilidades posibles.
Desafortunadamente, este proceso no puede ser completamente automatizado.

Es demasiado difícil, consume mucho tiempo, es demasiado caro y es demasiado
arriesgado migrar una aplicación Python 2 antigua a una nueva plataforma.
Es posible que reescribir el código le introduzca nuevos errores. Es más fácil
y mas sensato dejar estos sistemas solos y mejorar el intérprete existente,
en lugar de intentar trabajar dentro del código fuente que ya funciona.

Python 3 no es solo una versión mejorada de Python 2, es un lenguaje
completamente diferente, aunque es muy similar a su predecesor.
Cuando se miran a distancia, parecen ser el mismo, pero cuando se observan de
cerca, se notan muchas diferencias.

Si estás modificando una solución de Python existente, entonces es muy probable
que esté codificada en Python 2. Esta es la razón por la que Python 2 todavía
está en uso. Hay demasiadas aplicaciones de Python 2 existentes para descartarlo
por completo.

Si se va a comenzar un nuevo proyecto de Python, deberías usar Python 3, esta es
la versión de Python que se usará durante este curso.

Es importante recordar que puede haber diferencias mayores o menores entre las
siguientes versiones de Python 3 (p. Ej., Python 3.6 introdujo claves de
diccionario ordenadas de forma predeterminada en la implementación de CPython).
La buena noticia es que todas las versiones más nuevas de Python 3 son
compatibles con las versiones anteriores de Python 3. Siempre que sea
significativo e importante, intentaremos resaltar esas diferencias en el curso.

 Implementaciones de Python

 Además de Python 2 y Python 3, hay más de una versión de cada uno.

Siguiendo la Página wiki de Python, una implementación de Python se refiere a
"un programa o entorno que brinda soporte para la ejecución de programas escritos
en el lenguaje Python, representado por la Implementación de Referencia de CPython."

La implementación tradicional de Python, llamada CPython, es la versión de
referencia del lenguaje informático Python de Guido van Rossum, y se suele
llamar simplemente "Python". Cuando escuches el nombre CPython, lo más
probable es que se use para distinguirlo de otras implementaciones alternativas
no tradicionales.

Pero, lo primero es lo primero. Están los Pythons que son mantenidos por la
gente reunida alrededor de la PSF (Python Software Foundation), una comunidad
que tiene como objetivo desarrollar, mejorar, expandir y popularizar Python y
su entorno. El presidente del PSF es el mismo Guido von Rossum, y por eso,
estos pythons se llaman canónicos. También se consideran Pythons de referencia,
ya que cualquier otra implementación del lenguaje debe seguir todos los
estándares establecidos por la PSF.

Guido van Rossum usó el lenguaje de programación "C" para implementar la primera
versión de su lenguaje y esta decisión aún está vigente. Todos los Pythons que
provienen del PSF están escritos en el lenguaje "C". Hay muchas razones para
este enfoque. Uno de ellos (probablemente el más importante) es que gracias a él,
Python puede ser portado y migrado fácilmente a todas las plataformas con la
capacidad de compilar y ejecutar programas en lenguaje "C" (prácticamente todas
las plataformas tienen esta función, lo que abre muchas posibilidades de expansión).
oportunidades para Python).

Esta es la razón por la cual la implementación de PSF a menudo se denomina CPython.
Este es el Python más influyente entre todos los Pythons del mundo.

Este componente es una tarjeta invertida compuesta por tarjetas invertibles que
contienen una imagen de visualización. Selecciona la imagen de la cara frontal
para pasar a la cara posterior de estas tarjetas para mostrar el texto asociado.
Haz clic en las imágenes para obtener más información sobre los miembros de la
familia Python y algunas de las implementaciones alternativas de Python más
populares.

Cython es una de las posibles soluciones al rasgo de Python más doloroso - la
falta de eficiencia. Los cálculos matemáticos grandes y complejos pueden ser
fácilmente codificados en Python (mucho más fácil que en "C" o en cualquier
otro lenguaje tradicional), pero la ejecución del código resultante puede
requerir mucho tiempo.

¿Cómo se reconcilian estas dos contradicciones? Una solución es escribir tus
ideas matemáticas usando Python, y cuando estés absolutamente seguro de que
tu código es correcto y produce resultados válidos, puedes traducirlo a "C".
Ciertamente, "C" se ejecutará mucho más rápido que Python puro.

Esto es lo que pretende hacer Cython: traducir automáticamente el código de
Python (limpio y claro, pero no demasiado rápido) al código "C"
(complicado y hablador, pero ágil).

Otra versión de Python se llama Jython.

"J" es de "Java". Imagina un Python escrito en Java en lugar de C. Esto es
útil, por ejemplo, si desarrollas sistemas grandes y complejos escritos
completamente en Java y deseas agregarles cierta flexibilidad de Python.
El tradicional CPython puede ser difícil de integrar en un entorno de este tipo,
ya que C y Java viven en mundos completamente diferentes y no comparten muchas
ideas comunes.

Jython puede comunicarse con la infraestructura Java existente de manera más
efectiva. Es por esto que algunos proyectos lo encuentran útil y necesario.

Nota: la implementación actual de Jython sigue los estándares de Python 2.
Hasta ahora, no hay Jython conforme a Python 3.

Echa un vistazo al logo de abajo. ¿Puedes resolverlo?

Es el logotipo de PyPy - un Python dentro de un Python. En otras palabras,
representa un entorno de Python escrito en un lenguaje similar a Python llamado
RPython (Restricted Python). En realidad es un subconjunto de Python.

El código fuente de PyPy no se ejecuta de manera interpretativa, sino que se
traduce al lenguaje de programación C y luego se ejecuta por separado.

Esto es útil porque si deseas probar cualquier característica nueva que pueda
ser o no introducida en la implementación de Python, es más fácil verificarla
con PyPy que con CPython. Esta es la razón por la que PyPy es más una herramienta
para las personas que desarrollan Python que para el resto de los usuarios.

Esto no hace que PyPy sea menos importante o menos serio que CPython.

Además, PyPy es compatible con el lenguaje Python 3.

Hay muchos más Pythons diferentes en el mundo. Los encontrarás sí los buscas,
pero este curso se centrará en CPython.

MicroPython es una implementación eficiente de software de código abierto de
Python 3 que está optimizada para ejecutarse en microcontroladores. Incluye un
pequeño subconjunto de la biblioteca estándar de Python, pero está repleto de
una gran cantidad de funciones, como mensajes interactivos o números enteros de
precisión arbitraria, así como módulos que dan acceso al programador a hardware
de bajo nivel.

Creado originalmente por Damien George, un programador australiano, que en el
año 2013 realizó una exitosa campaña en Kickstarter y lanzó la primera versión
de MicroPython con una placa de desarrollo con tecnología STM32F4 llamada pyboard.

En 2017, MicroPython se utilizó para crear CircuitPython, otro lenguaje de
programación de código abierto que se ejecuta en el hardware del microcontrolador,
que es un derivado del lenguaje MicroPython.

Instrucciones
Ya has visto un programa de computadora que contiene una invocación de función.
La invocación de una función es uno de los muchos tipos posibles de instrucciones
de Python.

Por supuesto, cualquier programa complejo generalmente contiene muchas más
instrucciones que una. La pregunta es: ¿Cómo se acopla más de una instrucción en el
código de Python?

La sintaxis de Python es bastante específica en esta área. A diferencia de la mayoría
de los lenguajes de programación, Python requiere que no haya más de una instrucción
por línea.

Una línea puede estar vacía (por ejemplo, puede no contener ninguna instrucción) pero
no debe contener dos, tres o más instrucciones. Esto está estrictamente prohibido.

Nota: Python hace una excepción a esta regla - permite que una instrucción se extienda
por más de una línea (lo que puede ser útil cuando el código contiene construcciones
complejas).

Vamos a expandir el código un poco, puedes verlo en el editor. Ejecútalo y observa lo
que aparece en la consola.

"""
print("La Witsi Witsi Araña subió a su telaraña.")
print("Vino la lluvia y se la llevó.")

"""
Esta es una buena oportunidad para hacer algunas observaciones:

El programa invoca a la función print() dos veces, y puedes ver dos líneas separadas
en la consola - esto significa que print() comienza su salida desde una nuevalínea
cada vez que comienza su ejecución; puedes cambiar este comportamiento, pero también
puedes usarlo a tu favor;
Cada invocación de print() contiene una cadena diferente, como su argumento, y el
contenido de la consola lo refleja - esto significa que las instrucciones en el código
se ejecutan en el mismo orden en el que se han colocado en el archivo fuente; no se
ejecuta ninguna instrucción posterior hasta que se completa la anterior (hay algunas
excepciones a esta regla, pero puede ignorarlas por ahora.)

Hemos cambiado un poco el ejemplo - hemos agregado una invocación vacía de la función
print(). La llamamos vacía porque no hemos entregado ningún argumento a la función.

Puedes verlo en la ventana del editor. Ejecuta el código.

¿Qué sucede?
"""
print("La Witsi Witsi Araña subió a su telaraña.")
print()
print("Vino la lluvia y se la llevó.")

"""
Como puedes ver, la invocación vacía de print() no está tan vacía como podrías haber
esperado - genera una línea vacía o (esta interpretación también es correcta) genera
una nuevalínea.

Esta no es la única forma de producir una nuevalínea en la consola de salida. Ahora
le mostraremos otra manera.

Comentarios – ¿por qué, cuándo, y dónde?

Quizá en algún momento será necesario poner algunas palabras en el código dirigidas
no a Python, sino a las personas quienes estén leyendo el código con el fin de
explicarles como es que funciona, o tal vez especificar el significado de las variables,
también para documentar quien es el autor del programa y en que fecha fue escrito.

Un texto insertado en el programa el cual es, omitido en la ejecución, es denominado un
comentario.

¿Cómo se colocan este tipo de comentarios en el código fuente? Tiene que ser hecho de
cierta manera para que Python no intente interpretarlo como parte del código.

Cuando Python se encuentra con un comentario en el programa, el comentario es
completamente transparente - desde el punto de vista de Python, el comentario es solo
un espacio vacío, sin importar que tan largo sea.

En Python, un comentario es un texto que comienza con el símbolo # y se extiende hasta
el final de la línea.

Si se desea colocar un comentario que abarca varias líneas, se debe colocar este
símbolo en cada línea. Justo como en el siguiente código:
"""
# Este programa evalúa la hipotenusa c. # a y b son las longitudes de los cátetos.
# a = 3.0 b = 4.0 c = (a ** 2 + b ** 2) ** 0.5 # Se emplea **
# en lugar de una raíz cuadrada. print("c =", c)
"""
Los desarrolladores buenos y responsables describen cada pieza importante de código,
por ejemplo, el explicar el rol de una variables. Aunque la mejor manera de comentar
una variable es dándole un nombre que no sea ambiguo.

Por ejemplo, si una variable determinada esta diseñada para almacenar el área de un
cuadrado, el nombre square_area será muchísimo mejor que aunt_jane.

El nombre dado a la variable se puede definir como auto-comentable.

Marcar fragmentos de código
Los comentarios pueden ser útiles en otro aspecto - se pueden utilizar para marcar un
fragmento de código que actualmente no se necesita, cual sea la razón. Observa el
siguiente ejemplo, sí se descomenta la línea resaltada, esto afectara la salida o
resultado del código:

"""
# Este es un programa de prueba. x = 1 y = 2 # y = y + x print(x + y)
"""
Esto es frecuentemente realizado cuando se esta probando un programa, con el fin de
aislar un fragmento de código donde posiblemente se encuentra un error.

Consejo 
Si deseas comentar o descomentar rápidamente varias línea(s) de código, selecciona
las líneas que deseas modificar y utiliza el siguiente método abreviado de teclado:
CTRL + / (Windows) or CMD + / (Mac OS). Es un truco muy útil, ¿no? Ahora experimenta
con el código en el editor.
"""