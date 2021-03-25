def limpiarString(stringin):
    punt = ''':/,-.'"}{)(;]['''
    for char in stringin:
        if char in punt:
            stringin = stringin.replace(char, " ")
    return stringin



def formatearALista(stringin):
    stringin=limpiarString(stringin)
    return stringin.split()

nombres = """'Agustin','Alan','Andrés','Ariadna','Bautista','CAROLINA','CESAR','David','Diego','Dolores','DYLAN','ELIANA','Emanuel','Fabián','Facundo','Facundo','FEDERICO','FEDERICO','GONZALO','Gregorio','Ignacio','Jonathan','Jonathan','Jorge','JOSE','JUAN','Juan','Juan','Julian','Julieta','LAUTARO','Leonel','LUIS','Luis','Marcos','María','MATEO','Matias','Nicolás','NICOLÁS','Noelia','Pablo','Priscila','TOMAS','Tomás','Ulises', 'Yanina'"""
eval1 = '''81,60,72,24,15,91,12,70,29,42,16,3,35,67,10,57,11,69,12,77,13,86,48,65,51,41,87,43,10,87,91,15,44,85,73,37,42,95,18,7,74,60,9,65,93,63,74'''
eval2 = '''30,95,28,84,84,43,66,51,4,11,58,10,13,34,96,71,86,37,64,13,8,87,14,14,49,27,55,69,77,59,57,40,96,24,30,73,95,19,47,15,31,39,15,74,33,57,10'''

lst_nombres=formatearALista(nombres)
lst_eval1=eval1.split(',')
lst_eval2=eval2.split(',')

lst_tupla=[]
total=0
for i in range(len(lst_nombres)):
    suma = int(lst_eval1[i]) + int(lst_eval2[i])
    lst_tupla.append((lst_nombres[i],suma))
    total+=suma

prom=total/(len(lst_nombres))
men=0
for e in lst_tupla:
    if e[1]<prom:
        men+=1
    

print(f"El promedio de las notas es: {prom/20} y la cantidad de alumnos menores al promedio es: {men}")

'''
7. Trabajando con los contenidos de los archvios que pueden acceder en el curso:
• nombres
• eval1
• eval2
Copiar el contenido de los archvios en variables de tipo string y realizar.
• generar una estructura con los nombres de los estudiantes y la suma de ambas.
• Calcular el promedio de las notas totales e informar quiénes obtuvieron menos que el promedio.
notas.'''