"""
Comparación: operador de igualdad
Pregunta: ¿son dos valores iguales?

Para hacer esta pregunta, se utiliza el == (igual igual) operador.

No olvides esta importante distinción:

= es un operador de asignación, por ejemplo, a = b asigna a la varable a el valor de b;
== es una pregunta ¿Son estos valores iguales? así que a == b compara a y b.
Es un operador binario con enlazado del lado izquierdo. Necesita dos argumentos y verifica si son iguales.

Operadores
Igualdad: El operador igual a (==)
El operador == (igual a) compara los valores de dos operandos. Si son iguales, el
resultado de la comparación es True. Si no son iguales, el resultado de la comparación
es False.

Observa la comparación de igualdad a continuación - ¿Cuál es el resultado de esta operación?

var == 0

Toma en cuenta que no podemos encontrar la respuesta si no sabemos qué valor está almacenado actualmente en la variable var.

Si la variable se ha cambiado muchas veces durante la ejecución del programa, o si se ingresa su valor inicial desde la consola, Python solo puede responder a esta pregunta en el tiempo de ejecución del programa.

Ahora imagina a un programador que sufre de insomnio, y tiene que contar las ovejas negras y blancas por separado siempre y cuando haya exactamente el doble de ovejas negras que de las blancas.

La pregunta será la siguiente:
black_sheep == 2 * white_sheep

Debido a la baja prioridad del operador ==, la pregunta será tratada como la siguiente:
black_sheep == (2 * white_sheep)

"""
var = 0  # Asignando 0 a var
print(var == 0)

var = 1  # Asignando 1 a var
print(var == 0)

"""
Desigualdad: el operador no es igual a (!=)
El operador != (no es igual a) también compara los valores de dos operandos. Aquí está la diferencia: si son iguales, el resultado de la comparación es False. Si no son iguales, el resultado de la comparación es True.

Ahora echa un vistazo a la comparación de desigualdad a continuación - ¿puedes adivinar el resultado de esta operación?
"""
var = 0  # Asignando 0 a var
print(var != 0)
 
var = 1  # Asignando 1 a var
print(var != 0)

"""
Operadores de comparación: mayor que
También se puede hacer una pregunta de comparación usando el operador > (mayor que).

Si deseas saber si hay más ovejas negras que blancas, puedes escribirlo de la siguiente manera:

black_sheep > white_sheep  # Mayor que

True lo confirma; False lo niega.


Operadores de comparación: mayor o igual que
El operador mayor que tiene otra variante especial, una variante no estricta, pero se denota de manera diferente que la notación aritmética clásica: >= (mayor o igual que).

Hay dos signos subsecuentes, no uno.

Ambos operadores (estrictos y no estrictos), así como los otros dos que se analizan en la siguiente sección, son operadores binarios con enlazado del lado izquierdo, y su prioridad es mayor que la mostrada por == y !=.

Si queremos saber si tenemos que usar un gorro o no, nos hacemos la siguiente pregunta:
centigrade_outside >= 0.0  # Mayor o igual que

Operadores de comparación: menor o igual que
Como probablemente ya hayas adivinado, los operadores utilizados en este caso son: El operador < (menor que) y su hermano no estricto: <= (menor o igual que).

Observa este ejemplo simple:
current_velocity_mph < 85  # Menor que
current_velocity_mph <= 85  # Menor o igual que
Vamos a comprobar si existe un riesgo de ser multados por la ley (la primera pregunta es estricta, la segunda no).


"""
#asignamos:
variableA = 10
print(variableA)

#reasignacion, ahora sera el valor de 11:
variableA = variableA + 1
print(variableA)

#sintaxis reducida al reasignar, equivalente a lo anterior (Nos dara 12):
variableA += 1
print(variableA)

#nos dara 10
variableA -= 2
print(variableA)

#nos dara 30:
variableA *= 3
print(variableA)