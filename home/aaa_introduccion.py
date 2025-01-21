"""
Introducción a la programación:
¿Cómo funciona un programa de computadora?
Un programa hace que una computadora sea usable.
Sin un programa, una computadora, incluso la más poderosa, no es más que un objeto.
Del mismo modo, sin un reproductor, un piano no es más que una caja de madera.

Las computadoras pueden realizar tareas muy complejas, pero esta habilidad no es
innata. La naturaleza de una computadora es bastante diferente.

Solo puede ejecutar operaciones extremadamente simples. Por ejemplo, una computadora
no puede comprender el valor de una función matemática complicada por sí misma,
aunque esto no está fuera del alcance de la posibilidad en un futuro cercano.

Las computadoras contemporáneas solo pueden evaluar los resultados de operaciones
muy fundamentales. , como sumar o dividir, pero pueden hacerlo muy rápido y pueden
repetir estas acciones prácticamente cualquier cantidad de veces.

Imagina que quieres saber la velocidad media que has alcanzado durante un viaje
largo. Conoces la distancia, conoces el tiempo, necesitas la velocidad.

Naturalmente, la computadora podrá calcular esto, pero la computadora no es
consciente de cosas como la distancia, la velocidad o el tiempo. Por lo tanto,
es necesario instruir a la computadora para:

aceptar un número que represente la distancia;
aceptar un número que represente el tiempo de viaje;
divide el valor anterior por el segundo y almacenar el resultado en la memoria;
mostrar el resultado (que representa la velocidad promedio) en un formato legible.

Estas cuatro simples acciones forman un programa. Por supuesto, estos ejemplos no
están formalizados y están muy lejos de lo que la computadora puede entender, pero
son lo suficientemente buenos para ser traducidos a un idioma que la computadora
pueda aceptar.

El lenguaje es la palabra clave.

Lenguajes naturales vs lenguajes de programación

Un lenguaje es un medio (y una herramienta) para expresar y registrar pensamientos.
Hay muchos lenguajes a nuestro alrededor. Algunos de ellos no requieren ni hablar
ni escribir, como el lenguaje corporal; es posible expresar tus sentimientos más
profundos muy precisamente sin decir una palabra.

Otro lenguaje que utilizas cada día es tu lengua materna, que utilizas para
manifestar tu voluntad y reflexionar sobre la realidad. Las computadoras también
tienen su propio lenguaje, llamado lenguaje máquina, que es muy rudimentario.

Una computadora, incluso la más sofisticada técnicamente, está desprovista de
cualquier rastro de inteligencia. Se podría decir que es como un perro bien
adiestrado: responde sólo a un conjunto predeterminado de comandos conocidos.

Los comandos que reconoce son muy simples. Podemos imaginar que la computadora
responde a órdenes como "toma ese número, divide por otro y guarda el resultado".

Un conjunto completo de comandos conocidos se llama lista de instrucciones,
a veces abreviada IL (por sus siglas en inglés). Los diferentes tipos de
computadoras pueden variar según el tamaño de sus IL y las instrucciones pueden
ser completamente diferentes en diferentes modelos.

Nota: los lenguajes máquina son desarrollados por humanos.

Ninguna computadora es actualmente capaz de crear un nuevo idioma o lenguaje.
Sin embargo, eso puede cambiar pronto. Por otro lado, las personas también usan
varios idiomas muy diferentes, pero estos idiomas se crearon ellos mismos. Además,
todavía están evolucionando.

Cada día se crean nuevas palabras y desaparecen las viejas. Estos lenguajes se
llaman lenguajes naturales.

¿Qué compone a un lenguaje?

elementos:

Un alfabeto
un conjunto de símbolos utilizados para formar palabras de un determinado lenguaje
(por ejemplo, el alfabeto latino para el inglés, el alfabeto cirílico para el ruso,
el kanji para el japonés, y así sucesivamente)

Un léxico
(también conocido como diccionario) un conjunto de palabras que el lenguaje ofrece
a sus usuarios (por ejemplo, la palabra "computadora" proviene del diccionario en
inglés, mientras que "cmoptrue" no; la palabra "chat" está presente en los
diccionarios de inglés y francés, pero sus significados son diferentes)

Una sintaxis
un conjunto de reglas (formales o informales, escritas o interpretadas
intuitivamente) utilizadas para precisar si una determinada cadena de palabras
forma una oración válida (por ejemplo, "Soy una serpiente" es una frase
sintácticamente correcta, mientras que "Yo serpiente soy una" no lo es)

Una semántica
un conjunto de reglas que determinan si una frase tiene sentido (por ejemplo,
"Me comí una dona" tiene sentido, pero "Una dona me comió" no lo tiene)

Lenguaje máquina vs. lenguaje de alto nivel

El IL es, de hecho, el alfabeto de un lenguaje máquina. Este es el conjunto de
símbolos más simple y primario que podemos usar para dar comandos a una
computadora. Es la lengua materna de la computadora.

Desafortunadamente, esta lengua materna está muy lejos de la lengua materna humana.
Ambos (computadoras y humanos) necesitamos algo más, un lenguaje común para
computadoras y humanos, o un puente entre los dos mundos diferentes.

Necesitamos un lenguaje en el que los humanos puedan escribir sus programas y un
lenguaje que las computadoras pueden usar para ejecutar los programas, uno que es
mucho más complejo que el lenguaje de máquina y, sin embargo, mucho más simple que
el lenguaje natural.

Estos lenguajes a menudo se denominan lenguajes de programación de alto nivel.
Son al menos algo similares a los naturales en que usan símbolos, palabras y
convenciones legibles para los humanos. Estos lenguajes permiten a los humanos
expresar comandos a las computadoras que son mucho más complejos que los que
ofrecen las IL.

Un programa escrito en un lenguaje de programación de alto nivel se denomina
código fuente ( en contraste con el código máquina ejecutado por las computadoras).
Del mismo modo, el archivo que contiene el código fuente se denomina archivo
fuente.

Compilación vs. Interpretación:

La programación informática es el acto de componer los elementos del lenguaje de
programación seleccionado en el orden que provocará el efecto deseado. El efecto
podría ser diferente en cada caso específico – depende de la imaginación,
el conocimiento y la experiencia del programador.

Por supuesto, dicha composición tiene que ser correcta en muchos sentidos:

alfabéticamente – un programa debe estar escrito en un alfabeto reconocible,
como romano, cirílico, etc.
léxicamente – cada lenguaje de programación tiene su diccionario y hay que
dominarlo; afortunadamente, es mucho más simple y pequeño que el diccionario de
cualquier idioma natural;
sintácticamente – cada idioma tiene sus reglas y hay que obedecerlas;
semánticamente – el programa tiene que tener sentido.

Desafortunadamente, un programador también puede cometer errores con cada uno de
los cuatro sentidos anteriores. Cada uno de ellos puede hacer que el programa se
vuelva completamente inútil.

Supongamos que has escrito con éxito un programa. ¿Cómo persuadimos a la
computadora para que lo ejecute? Tienes que convertir tu programa en lenguaje de
máquina. Afortunadamente, la traducción la puede hacer una computadora, lo que
hace que todo el proceso sea rápido y eficiente.

Hay dos formas diferentes de transformar un programa de un lenguaje de programación
de alto nivel a un lenguaje de máquina:

Compilación - el programa fuente se traduce una vez (sin embargo, este acto debe
repetirse cada vez que se modifique el código fuente) al obtener un archivo
(por ejemplo, un .exe si el código está destinado a ejecutarse en MS Windows)
que contiene el código máquina. Ahora se puede distribuir el archivo en todo el
mundo; el programa que realiza esta traducción se llama compilador o traductor.

Interpretación - tú o cualquier usuario del código puede traducir el programa
fuente cada vez que se debe ejecutar. El programa que realiza este tipo de
transformación se denomina intérprete, ya que interpreta el código cada vez que se
pretende ejecutar. También significa que no puedes simplemente distribuir el código
fuente tal cual, porque el usuario final también necesita el intérprete para ejecutarlo.

Debido a algunas razones muy fundamentales, un lenguaje de programación de alto 
nivel en particular está diseñado para caer en una de estas dos categorías.

Hay muy pocos lenguajes que puedan compilarse e interpretarse. Por lo general,
un lenguaje de programación se proyecta con este factor en la mente de sus
constructores - ¿será compilado o interpretado?

¿Qué hace el intérprete?
Supongamos una vez más que has escrito un programa. Ahora, existe como un archivo
de computadora: un programa de computadora es en realidad un fragmento de texto,
por lo que el código fuente generalmente se coloca en archivos de texto.

Nota: tiene que ser texto puro, sin decoraciones como diferentes fuentes, colores,
imágenes incrustadas u otros medios. Ahora debes invocar al intérprete y dejar
que lea tu archivo fuente.

El intérprete lee el código fuente de la forma habitual en la cultura occidental:
de arriba a abajo y de izquierda a derecha. Hay algunas excepciones: se cubrirán
más adelante en el curso.

En primer lugar, el intérprete verifica si todas las líneas posteriores son
correctas (utilizando los cuatro aspectos cubiertos anteriormente).

Si el compilador encuentra un error, finaliza el trabajo inmediatamente.
El único resultado en este caso es un mensaje de error.

El intérprete te informará dónde se encuentra el error y qué lo causó.
Sin embargo, estos mensajes pueden ser engañosos, ya que el intérprete
no puede seguir tus intenciones exactas y puede detectar errores a cierta
distancia de sus causas reales.

Por ejemplo, si intentas utilizar una entidad de un nombre desconocido,
causará un error, pero el error se descubrirá en el lugar donde intenta usar
la entidad, no donde se introdujo el nombre de la nueva entidad.

En otras palabras, el motivo suele estar ubicado un poco antes en el código,
por ejemplo, en el lugar donde tenías que informar al intérprete que ibas a
utilizar la entidad del nombre.

Si la línea se ve bien, el intérprete intenta ejecutarlo
(nota: cada línea generalmente se ejecuta por separado, por lo que el trío
"leer-verificar-ejecutar" se puede repetir muchas veces, más veces mas que el
número real de líneas en el archivo fuente, ya que algunas partes del código
puede ejecutarse más de una vez).

También es posible que una parte significativa del código pueda ejecutarse con
éxito antes de que el interprete encuentra un error. Este es un comportamiento
normal en este modelo de ejecución.

Puedes preguntarte ahora: ¿cuál es mejor? ¿El modelo de "compilación" o el modelo
de "interpretación"? No hay una respuesta obvia. De haberlo existido, uno de
estos modelos habría dejado de existir hace mucho tiempo. Ambos tienen
sus ventajas y sus desventajas.

Compilación vs. Interpretación – Ventajas y Desventajas

Ventajas
Compilación:
✓la ejecución del código traducido suele ser más rápida;
✓solo el usuario debe tener el compilador; el usuario final puede usar el código
sin él;
✓el código traducido se almacena usando lenguaje máquina; como es muy difícil de
entender, es probable que tus propios inventos y trucos de programación sigan
siendo tu secreto.

Interpretación
✓puedes ejecutar el código tan pronto como lo completes; no hay fases adicionales
de traducción;
✓el código se almacena usando un lenguaje de programación, no un lenguaje máquina;
esto significa que se puede ejecutar en computadoras que usan diferentes lenguajes
máquina; no compila tu código por separado para cada arquitectura diferente.

Desventajas:
Compilación
❌la compilación en sí puede ser un proceso que consume mucho tiempo; es posible
que no puedas ejecutar su código inmediatamente después de realizar una
modificación;
❌debes tener tantos compiladores como plataformas de hardware donde desees que
se ejecute tu código.

Interpretación
❌no esperes que la interpretación acelere tu código a alta velocidad: tu código
compartirá el poder de la computadora con el intérprete, por lo que no puede ser
realmente rápido;
❌tanto tu como el usuario final deben tener el intérprete para ejecutar tu código.

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