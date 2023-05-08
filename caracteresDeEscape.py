"""
Caracteres de escape y nueva línea en Python
Hemos modificado el código de nuevo. Obsérvalo con cuidado.

Hay dos cambios muy sutiles - hemos insertado un par extraño de caracteres dentro del texto. Se ven así: \n.
"""
print("La Witsi Witsi Araña\nsubió a su telaraña.")
print()
print("Vino la lluvia\ny se la llevó.")
"""
Curiosamente, mientras puedes ver dos caracteres, Python ve uno.

La barra invertida (\) tiene un significado muy especial cuando se usa dentro de cadenas - se llama carácter de escape.

La palabra escape debe entenderse específicamente - significa que la serie de caracteres en la cadena se escapa por un momento (un momento muy breve) para introducir una inclusión especial.

En En otras palabras, la barra invertida no significa nada en sí misma, sino que es solo una especie de anuncio de que el siguiente carácter después de la barra invertida también tiene un significado diferente.

La la letra n colocada después de la barra invertida proviene de la palabra newline.

Tanto la barra invertida como n forman un símbolo especial llamado un carácter de nuevalínea, que insta a la consola a iniciar una nuevalínea de salida.

Como se puede observar, aparecen dos nuevas líneas en la canción infantil, en los lugares donde se ha utilizado \n.

Esta convención tiene dos consecuencias importantes:

1. Si deseas colocar solo una barra invertida dentro de una cadena, no olvides su naturaleza de escape - tienes que duplicarla. Por ejemplo, una invocación como esta provocará un error:
print("\")

mientras que esta no lo hará:
"""
print("\\")
"""
2. No todos los pares de escape (la barra invertida junto con otro carácter) significan algo.
Experimenta con tu código en el editor, ejecútalo y ve qué sucede.
"""
print("La Witsi Witsi Araña\nsubió a su telaraña.")
print()
print("Vino la lluvia\nay se la llevó.")