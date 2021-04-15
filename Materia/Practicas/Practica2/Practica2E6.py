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



frase = """Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría
automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y
reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar
un montón de archivos con fotos de una manera compleja. Tal vez quieras
escribir alguna pequeña base de datos personalizada, o una aplicación
especializada con interfaz gráfica, o UN juego simple."""

frase=formatearString(frase)

fraselst = frase.split()

setout=set()

for word in fraselst:
    setout.add(word)

print(setout)



'''
6. Dada una frase donde las palabras pueden estar repetidas e indistintamente en mayúsculas y
minúsculas, imprimir una lista con todas las palabras sin repetir y en letra minúscula.'''