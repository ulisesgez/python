#Nos permitiran comparar dos expreseiones bolleanas:
a = True
b = False

#and, todos deben ser verdaderos para que sea verdadero:
gas = True
encendido = True

if gas and encendido:
    print("Puedes avanzar")

result = a and b
print(result)

#or, almenos uno debe ser verdadero para que sea verdadero:
cafe = True
leche = False
te = False

if cafe or leche or te:
    print("Puedes desayunar")

result = a or b
print(result)

#not, invetimos el valor de true o false:
casa = True
deártamento = True
if not casa or deártamento:
    print("No puedes salir")

result = not a
print(result)

#comprobamos que ambas ya son falsos:
test = result or b
print(test)