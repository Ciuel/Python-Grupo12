palabra = input("Escriba una palabra: ").lower()

lst_palabra=[]
i = 0
while (i < len(palabra)) and (palabra[i] not in lst_palabra):
    lst_palabra.append(palabra[i])
    i+=1
if (i < len(palabra)):
    print (f"{palabra} no es un heterograma")
else:
    print (f"{palabra} es un heterograma")


'''
Escbriba un programa que solicite que se ingrese una palabra o frase y permita identificar si la
misma es un Heterograma (tenga en cuenta que el contenido del enlace es una traducción del
inglés por lo cual las palabras que nombra no son heterogramas en español). Un Heterograma
es una palabra o frase que no tiene ninguna letra repetida entre sus caracteres.
'''