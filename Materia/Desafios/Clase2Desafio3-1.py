def promedio(notas):
    suma = 0
    for e in notas:
        suma += e
    return suma / len(notas)


def menospro(notas,prom):
    suma = 0
    for e in notas:
        if e < prom:
            suma += 1
    return suma1



notas = []
nota = int(input("Ingrese la nota, ingrese una nota negativa para terminar: "))
while nota > -1:
    notas.append(nota)
    nota = int(
        input("Ingrese la nota, ingrese una nota negativa para terminar: "))

prom=promedio(notas)


print(
    f"El promedio es: {prom} , y la cantidad de alumnos menores al promedio es: {menospro (notas,prom)}"
)
