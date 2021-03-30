def promedio(notas):
    suma = 0
    for e in notas:
        suma += notas[e]
    return suma / len(notas)


def menospro(notas, prom):
    suma = 0
    for e in notas:
        if notas[e] < prom:
            suma += 1
    return suma


notas = {}
nombre = input("Ingrese el nombre, ingrese fin para terminar: ")
while nombre.lower() > "fin":
    nota = int(input(f"Ingrese la nota de {nombre}: "))
    notas[nombre] = nota
    nombre = input("Ingrese el nombre, ingrese fin para terminar: ")

prom = promedio(notas)

print(
    f"El promedio es: {prom} , y la cantidad de alumnos menores al promedio es: {menospro (notas,prom)}"
)
