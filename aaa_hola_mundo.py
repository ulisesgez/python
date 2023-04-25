"""Mi primer programa, hola mundo:"""
print('Hola mundo')

"""
Introducción a la programación:
¿Cómo funciona un programa de computadora?
Un programa hace que una computadora sea usable. Sin un programa, una computadora, incluso la más poderosa, no es más que un objeto. Del mismo modo, sin un reproductor, un piano no es más que una caja de madera.

Las computadoras pueden realizar tareas muy complejas, pero esta habilidad no es innata. La naturaleza de una computadora es bastante diferente.

Solo puede ejecutar operaciones extremadamente simples. Por ejemplo, una computadora no puede comprender el valor de una función matemática complicada por sí misma, aunque esto no está fuera del alcance de la posibilidad en un futuro cercano.

Las computadoras contemporáneas solo pueden evaluar los resultados de operaciones
muy fundamentales. , como sumar o dividir, pero pueden hacerlo muy rápido y pueden
repetir estas acciones prácticamente cualquier cantidad de veces.

Imagina que quieres saber la velocidad media que has alcanzado durante un viaje largo. Conoces la distancia, conoces el tiempo, necesitas la velocidad.

Naturalmente, la computadora podrá calcular esto, pero la computadora no es consciente de cosas como la distancia, la velocidad o el tiempo. Por lo tanto, es necesario instruir a la computadora para:

aceptar un número que represente la distancia;
aceptar un número que represente el tiempo de viaje;
divide el valor anterior por el segundo y almacenar el resultado en la memoria;
mostrar el resultado (que representa la velocidad promedio) en un formato legible.

Estas cuatro simples acciones forman un programa. Por supuesto, estos ejemplos no están formalizados y están muy lejos de lo que la computadora puede entender, pero son lo suficientemente buenos para ser traducidos a un idioma que la computadora pueda aceptar.

El lenguaje es la palabra clave.

 Lenguajes naturales vs lenguajes de programación

 Un lenguaje es un medio (y una herramienta) para expresar y registrar pensamientos. Hay muchos lenguajes a nuestro alrededor. Algunos de ellos no requieren ni hablar ni escribir, como el lenguaje corporal; es posible expresar tus sentimientos más profundos muy precisamente sin decir una palabra.

Otro lenguaje que utilizas cada día es tu lengua materna, que utilizas para manifestar tu voluntad y reflexionar sobre la realidad. Las computadoras también tienen su propio lenguaje, llamado lenguaje máquina, que es muy rudimentario.

Una computadora, incluso la más sofisticada técnicamente, está desprovista de cualquier rastro de inteligencia. Se podría decir que es como un perro bien adiestrado: responde sólo a un conjunto predeterminado de comandos conocidos.

Los comandos que reconoce son muy simples. Podemos imaginar que la computadora responde a órdenes como "toma ese número, divide por otro y guarda el resultado".

Un conjunto completo de comandos conocidos se llama lista de instrucciones, a veces abreviada IL (por sus siglas en inglés). Los diferentes tipos de computadoras pueden variar según el tamaño de sus IL y las instrucciones pueden ser completamente diferentes en diferentes modelos.

Nota: los lenguajes máquina son desarrollados por humanos.

Ninguna computadora es actualmente capaz de crear un nuevo idioma o lenguaje. Sin embargo, eso puede cambiar pronto. Por otro lado, las personas también usan varios idiomas muy diferentes, pero estos idiomas se crearon ellos mismos. Además, todavía están evolucionando.

Cada día se crean nuevas palabras y desaparecen las viejas. Estos lenguajes se llaman lenguajes naturales.

¿Qué compone a un lenguaje?

elementos:


Un alfabeto
un conjunto de símbolos utilizados para formar palabras de un determinado lenguaje (por ejemplo, el alfabeto latino para el inglés, el alfabeto cirílico para el ruso, el kanji para el japonés, y así sucesivamente)

Un léxico
(también conocido como diccionario) un conjunto de palabras que el lenguaje ofrece a sus usuarios (por ejemplo, la palabra "computadora" proviene del diccionario en inglés, mientras que "cmoptrue" no; la palabra "chat" está presente en los diccionarios de inglés y francés, pero sus significados son diferentes)

Una sintaxis
un conjunto de reglas (formales o informales, escritas o interpretadas intuitivamente) utilizadas para precisar si una determinada cadena de palabras forma una oración válida (por ejemplo, "Soy una serpiente" es una frase sintácticamente correcta, mientras que "Yo serpiente soy una" no lo es)

Una semántica
un conjunto de reglas que determinan si una frase tiene sentido (por ejemplo, "Me comí una dona" tiene sentido, pero "Una dona me comió" no lo tiene)

Lenguaje máquina vs. lenguaje de alto nivel

El IL es, de hecho, el alfabeto de un lenguaje máquina. Este es el conjunto de símbolos más simple y primario que podemos usar para dar comandos a una computadora. Es la lengua materna de la computadora.

Desafortunadamente, esta lengua materna está muy lejos de la lengua materna humana. Ambos (computadoras y humanos) necesitamos algo más, un lenguaje común para computadoras y humanos, o un puente entre los dos mundos diferentes.

Necesitamos un lenguaje en el que los humanos puedan escribir sus programas y un lenguaje que las computadoras pueden usar para ejecutar los programas, uno que es mucho más complejo que el lenguaje de máquina y, sin embargo, mucho más simple que el lenguaje natural.

Estos lenguajes a menudo se denominan lenguajes de programación de alto nivel. Son al menos algo similares a los naturales en que usan símbolos, palabras y convenciones legibles para los humanos. Estos lenguajes permiten a los humanos expresar comandos a las computadoras que son mucho más complejos que los que ofrecen las IL.

Un programa escrito en un lenguaje de programación de alto nivel se denomina código fuente ( en contraste con el código máquina ejecutado por las computadoras). Del mismo modo, el archivo que contiene el código fuente se denomina archivo fuente.

Compilación vs. Interpretación:

La programación informática es el acto de componer los elementos del lenguaje de programación seleccionado en el orden que provocará el efecto deseado. El efecto podría ser diferente en cada caso específico – depende de la imaginación, el conocimiento y la experiencia del programador.

Por supuesto, dicha composición tiene que ser correcta en muchos sentidos:

alfabéticamente – un programa debe estar escrito en un alfabeto reconocible, como romano, cirílico, etc.
léxicamente – cada lenguaje de programación tiene su diccionario y hay que dominarlo; afortunadamente, es mucho más simple y pequeño que el diccionario de cualquier idioma natural;
sintácticamente – cada idioma tiene sus reglas y hay que obedecerlas;
semánticamente – el programa tiene que tener sentido.

Desafortunadamente, un programador también puede cometer errores con cada uno de los cuatro sentidos anteriores. Cada uno de ellos puede hacer que el programa se vuelva completamente inútil.

Supongamos que has escrito con éxito un programa. ¿Cómo persuadimos a la computadora para que lo ejecute? Tienes que convertir tu programa en lenguaje de máquina. Afortunadamente, la traducción la puede hacer una computadora, lo que hace que todo el proceso sea rápido y eficiente.

Hay dos formas diferentes de transformar un programa de un lenguaje de programación de alto nivel a un lenguaje de máquina:

Compilación - el programa fuente se traduce una vez (sin embargo, este acto debe repetirse cada vez que se modifique el código fuente) al obtener un archivo (por ejemplo, un .exe si el código está destinado a ejecutarse en MS Windows) que contiene el código máquina. Ahora se puede distribuir el archivo en todo el mundo; el programa que realiza esta traducción se llama compilador o traductor.

Interpretación - tú o cualquier usuario del código puede traducir el programa fuente cada vez que se debe ejecutar. El programa que realiza este tipo de transformación se denomina intérprete, ya que interpreta el código cada vez que se pretende ejecutar. También significa que no puedes simplemente distribuir el código fuente tal cual, porque el usuario final también necesita el intérprete para ejecutarlo.

Debido a algunas razones muy fundamentales, un lenguaje de programación de alto nivel en particular está diseñado para caer en una de estas dos categorías.

Hay muy pocos lenguajes que puedan compilarse e interpretarse. Por lo general, un lenguaje de programación se proyecta con este factor en la mente de sus constructores - ¿será compilado o interpretado?

¿Qué hace el intérprete?
Supongamos una vez más que has escrito un programa. Ahora, existe como un archivo de computadora: un programa de computadora es en realidad un fragmento de texto, por lo que el código fuente generalmente se coloca en archivos de texto.

Nota: tiene que ser texto puro, sin decoraciones como diferentes fuentes, colores, imágenes incrustadas u otros medios. Ahora debes invocar al intérprete y dejar que lea tu archivo fuente.

El intérprete lee el código fuente de la forma habitual en la cultura occidental: de arriba a abajo y de izquierda a derecha. Hay algunas excepciones: se cubrirán más adelante en el curso.

En primer lugar, el intérprete verifica si todas las líneas posteriores son correctas (utilizando los cuatro aspectos cubiertos anteriormente).

Si el compilador encuentra un error, finaliza el trabajo inmediatamente. El único resultado en este caso es un mensaje de error.

El intérprete te informará dónde se encuentra el error y qué lo causó. Sin embargo, estos mensajes pueden ser engañosos, ya que el intérprete no puede seguir tus intenciones exactas y puede detectar errores a cierta distancia de sus causas reales.

Por ejemplo, si intentas utilizar una entidad de un nombre desconocido, causará un error, pero el error se descubrirá en el lugar donde intenta usar la entidad, no donde se introdujo el nombre de la nueva entidad.

En otras palabras, el motivo suele estar ubicado un poco antes en el código, por ejemplo, en el lugar donde tenías que informar al intérprete que ibas a utilizar la entidad del nombre.

Si la línea se ve bien, el intérprete intenta ejecutarlo (nota: cada línea generalmente se ejecuta por separado, por lo que el trío "leer-verificar-ejecutar" se puede repetir muchas veces, más veces mas que el número real de líneas en el archivo fuente, ya que algunas partes del código puede ejecutarse más de una vez).

También es posible que una parte significativa del código pueda ejecutarse con éxito antes de que el interprete encuentra un error. Este es un comportamiento normal en este modelo de ejecución.

Puedes preguntarte ahora: ¿cuál es mejor? ¿El modelo de "compilación" o el modelo de "interpretación"? No hay una respuesta obvia. De haberlo existido, uno de estos modelos habría dejado de existir hace mucho tiempo. Ambos tienen sus ventajas y sus desventajas.

Compilación vs. Interpretación – Ventajas y Desventajas

Ventajas
Compilación:
✓la ejecución del código traducido suele ser más rápida;
✓solo el usuario debe tener el compilador; el usuario final puede usar el código sin él;
✓el código traducido se almacena usando lenguaje máquina; como es muy difícil de entender, es probable que tus propios inventos y trucos de programación sigan siendo tu secreto.

Interpretación
✓puedes ejecutar el código tan pronto como lo completes; no hay fases adicionales de traducción;
✓el código se almacena usando un lenguaje de programación, no un lenguaje máquina; esto significa que se puede ejecutar en computadoras que usan diferentes lenguajes máquina; no compila tu código por separado para cada arquitectura diferente.

Desventajas:
Compilación
❌la compilación en sí puede ser un proceso que consume mucho tiempo; es posible que no puedas ejecutar su código inmediatamente después de realizar una modificación;
❌debes tener tantos compiladores como plataformas de hardware donde desees que se ejecute tu código.

Interpretación
❌no esperes que la interpretación acelere tu código a alta velocidad: tu código compartirá el poder de la computadora con el intérprete, por lo que no puede ser realmente rápido;
❌tanto tu como el usuario final deben tener el intérprete para ejecutar tu código.

¿Qué significa todo esto para ti?

Python es un lenguaje interpretado. Esto significa que hereda todas las ventajas y desventajas descritas. Por supuesto, agrega algunas de sus características únicas a ambos conjuntos.
Si deseas programar en Python, necesitarás el intérprete de Python. No podrás ejecutar tu código sin él. Afortunadamente, Python es gratuito. Esta es una de sus ventajas más importantes.

Por razones históricas, los lenguajes diseñados para ser utilizados en la interpretación a menudo se denominan lenguajes de scripting, mientras que la fuente los programas codificados con ellos se denominan scripts. Bien, conozcamos a Python.
"""