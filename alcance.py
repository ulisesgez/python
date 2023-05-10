saludo = "Hola, soy una variable global"#variable global, existe en todo el programa

def saludoUno():
    #print(saludo)#error, no existe la variable saludo
    saludo = "Hola, soy la función saludoUno"#variable local, solo existe dentro de la funcion
    print(saludo)

def saludoDos():
    saludo = "Hola, soy la función saludoDos"
    print(saludo)

#print(saludo)#error, no existe la variable saludo(previamente a agregar saludo de forma global)