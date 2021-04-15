cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no contener los símbolos:@ y !):")
if len(cadena) > 10:
    print("Ingresaste más de 10 carcateres")
else:
    i=0
    while (i<len(cadena))and(cadena[i]!="@" and cadena[i]!="!"):
        i+=1
    if i!=len(cadena):
        print("Ingresaste alguno de estos símbolos: @ o !" )
    else:
        print("Ingreso ok" )








'''
4. Retomamos el código visto en la teoría, que informaba si los caracteres “@” o “!” formaban
parte de una palabra ingresada

[ ]: cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no␣
,→contener los símbolos:@ y !):")
if len(cadena) > 10:
print("Ingresaste más de 10 carcateres")
cant = 0
for car in cadena:
if car == "@" or car == "!":
cant = cant + 1
if cant >= 1:
print("Ingresaste alguno de estos símbolos: @ o !" )
else:
print("Ingreoo OK")
Ingresa la clave (debe tener menos de 10 caracteres y no contener los símbolos:@
y !):@@ggg@@!!!
Ingresaste alguno de estos símbolos: @ o !

¿Cómo podemos simplificarlo?'''