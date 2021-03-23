import string
for i in range(4):
    cadena = input("Ingresá una palabra: ")
    print("TIENE R" if "r" in cadena.lower()  else "NO TIENE R")
print(cadena.lower())