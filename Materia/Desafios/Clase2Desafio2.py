print('''Si la palabra ingresada tiene la primera y ultima letras iguales imprime, sino no''')
cadena = input("Ingresá una palabra, FIN para terminar: ")
while cadena.lower() != "fin":
    if cadena[0] == cadena[-1]:
        print(cadena)
    cadena = input("Ingresá una palabra, FIN para terminar: ")
