#Queremos implementar una función que dada una cadena de texto, retorne las palabras que
#contiene en orden alfabético.


def ordenar_alfabeticamente(stringIn):
    """ Ordena alfabeticamente el string"""
      
    lst_string=stringIn.split()
    lst_string.sort(key=str.lower)
    return lst_string


print(ordenar_alfabeticamente("hola mi vida es una mierda"))