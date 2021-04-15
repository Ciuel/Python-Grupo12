notas= [4,6]
suma=0
for e in notas:
    suma += e
promedio=suma/len(notas)
menospro=0
for e in notas:
    if e<promedio:
        menospro+=1
print (f"El promedio es: {promedio} , y la cantidad de alumnos menores al promedio es: {menospro}")
