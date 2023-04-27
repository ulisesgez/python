edad = 22
if edad > 54:
    print("puede ver la pelicula con descuento")
elif edad > 17:
    print("puede ver la pelicula")
else:
    print("No puedes entrar")

#Estructuras de control:
#En este ejemlo prepararemos una bebida:

print('-----> Preparar bebida: <-----')
print('voy a la cocina')
print('abrir nevera')

hayLeche = input('Hay leche? s/n ')
hayChocolate = input('Hay Chocolate? s/n ')

if hayLeche == 's':
    print('sacamos la leche de la nevera')
else:
    print('Ha ir por leche')
    irPorLeche = input('Enserio ire por leche? ')
    if irPorLeche == 's':
        print('He ido por leche')
    else:
        print('Preparare otra cosa, y anotare faltante de leche para comprar')

if hayChocolate == 's':
    print('ponemos leche y chocolate en el vaso')
    print('Mezclamos')
    print('Tomamos')
else:
    print('Ha ir por chocolate')
    irPorChocolate = input('Enserio ire por chocolate? ')
    if irPorChocolate == 's':
        print('He ido por chocolate')
        print('ponemos leche y chocolate en el vaso')
        print('Mezclamos')
        print('Tomamos')
    else:
        print('Preparare otra cosa, y anotare faltante de chocolate para comprar')

print('-----> Fin Preparar bebida: <-----')

#verdadero
condicion = True

if condicion:
    print('verdadero')
else:
    print('falsa')

"""
otro ejemplo con elif
if condicion == True:
    print("verdadero")
elif condicion == False:
    print('falsa')
else:
    print('condicion no reconocida')
"""

#operador terneario:
dineroTotal = 2000
compras = "compramos todo" if dineroTotal > 1000 else "no compramos nada"

#otro ejemplo con operador terneario:

condicion = True

print('verdadera') if condicion else print('falsa')