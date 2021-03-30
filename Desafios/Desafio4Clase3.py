#Usando expresiones lambda escribir una función que permita codificar una
#frase según el siguiente algoritmo:
#encripto("a") --> "b"
#encripto("ABC") --> "BCD"
#encripto("Rock2021") --> "Spdl3132"



import string


letras= string.digits + string.ascii_letters
letras=letras[::-1]
print(letras)

def encripto_con_lambda(string_in):
    """ Esta funcion encripta el string recibido pero con lambda"""

    lst_string= map(lambda char: letras[letras.index(char)-1],string_in)
    str_out=""
    return  str_out.join(lst_string)

def encripto(string_in):
    """ Encripta el string de entrada, moviendo los caracteres uno hacia la derecha, sin Lambda"""
    
    string_out=""
    for char in string_in:
        index_letra=letras.index(char)
        string_out+= letras[index_letra-1]
    
    return string_out

print(encripto("a"))
print(encripto("ABC"))
print(encripto("Rock2021"))

print(encripto_con_lambda("aaaa"))
print(encripto_con_lambda("a"))
print(encripto_con_lambda("ABC"))
print(encripto_con_lambda("Rock2021"))



