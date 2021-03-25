def limpiarString(stringin):
    punt = ''':/,-.'"}{)(;]['''
    for char in stringin:
        if char in punt:
            stringin = stringin.replace(char, " ")
    return stringin

def formatearString(stringin):
    stringin=stringin.lower()
    stringin=limpiarString(stringin)
    return stringin


frase = '''Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban
trigo tres tristes tigres'''#input("ingrese una frase: ")

palabra = (input("Ingrese una palabra: ")).lower()

frase=formatearString(frase)



fraselst=frase.split()
cant=0
for pal in fraselst:
    if pal==palabra:
        cant+=1

print(f"La palbara es: {palabra} y se repite: {cant}")




'''
5. Dada una frase y un string ingresados por teclado (en ese orden), genere una lista de palabras,
y sobre ella, informe la cantidad de palabras en las que se encuentra el string. No distingir
entre mayúsculas y minúsculas.'''