def limpiarString(stringin):
    punt = ''':/,-.'"}{)(;]['''
    for char in stringin:
        if char in punt:
            stringin = stringin.replace(char, " ")
    return stringin



def formatearALista(stringin):
    stringin=stringin.lower()
    stringin=limpiarString(stringin)
    return stringin.split()

nombres = """'Agustin','Alan','Andrés','Ariadna','Bautista','CAROLINA','CESAR','David','Diego','Dolores','DYLAN','ELIANA','Emanuel','Fabián','Facundo','Facundo','FEDERICO','FEDERICO','GONZALO','Gregorio','Ignacio','Jonathan','Jonathan','Jorge','JOSE','JUAN','Juan','Juan','Julian','Julieta','LAUTARO','Leonel','LUIS','Luis','Marcos','María','MATEO','Matias','Nicolás','NICOLÁS','Noelia','Pablo','Priscila','TOMAS','Tomás','Ulises', 'Yanina'"""
nombres2 = """ 'Agustin','AGUSTIN','Agustín','Ailen','Alfredo','Amalia','Ariana','Bautista','Braian','Carla','CESAR','Daniel','Diego','ELIANA','Facundo','Facundo','Facundo','Facundo','Federico','Federico','Flavia','Francisco','Germán','Guido','GUSTAVO','Hilario','Ignacio','IVAN','Jimmy','Joaquín','Jose','Josue','JUAN','Juan','Laura','LAURA','Lautaro','Lautaro','Ludmila','Marcos','Marcos','MARIANELA','MARTIN','MATEO','Mateo','Matias','MAURO','Maximiliano','NESTOR','Nicolas','Pedro','Ramiro','Sofía','Tobias','Tomás','Tomás','Ulises','Yanina'"""
eval1 = '''81,60,72,24,15,91,12,70,29,42,16,3,35,67,10,57,11,69,12,77,13,86,48,65,51,41,87,43,10,87,91,15,44,85,73,37,42,95,18,7,74,60,9,65,93,63,74'''
eval2 = '''30,95,28,84,84,43,66,51,4,11,58,10,13,34,96,71,86,37,64,13,8,87,14,14,49,27,55,69,77,59,57,40,96,24,30,73,95,19,47,15,31,39,15,74,33,57,10'''


lst_nombres = formatearALista(nombres)
lst_nombres2 = formatearALista(nombres2)

nombres_en_comun = []
nombres_en_comun= [nom1 for nom1 in lst_nombres for nom2 in lst_nombres2 if (nom1==nom2) ]

nombres_en_comun=[]
for e in lst_nombres:
    for e2 in lst_nombres2:
        if (e==e2) and (e not in nombres_en_comun):
            nombres_en_comun.append(e)

lst_eval1=eval1.split(',')
lst_eval2=eval2.split(',')


#TODO terminar segundo punto y ver la comprension
        

'''
8. Con la información de los archivos de texto que se encuentran disponibles en el curso:
• nombres_1
• nombres_2
Nota: Trabaje con los datos en variables de tipo string.
• Indique los nombres que se encuentran en ambos. Nota: pruebe utilizando list comprehension.
• Genere dos variables con la lista de notas que se incluyen en los archivos: eval1.txt y eval2.txt
e imprima con formato los nombres de los estudiantes con las correspondientes nota y la suma
de ambas como se ve en la imagen:
'''