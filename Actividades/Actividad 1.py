nombres = """'Agustin','Alan','Andrés','Ariadna','Bautista','CAROLINA','CESAR','David','Diego','Dolores','DYLAN','ELIANA','Emanuel','Fabián','Facundo','Facundo','FEDERICO','FEDERICO','GONZALO','Gregorio','Ignacio','Jonathan','Jonathan','Jorge','JOSE','JUAN','Juan','Juan','Julian','Julieta','LAUTARO','Leonel','LUIS','Luis','Marcos','María','MATEO','Matias','Nicolás','NICOLÁS','Noelia','Pablo','Priscila','TOMAS','Tomás','Ulises','Yanina'"""
eval1 = '''81,60,72,24,15,91,12,70,29,42,16,3,35,67,10,57,11,69,12,77,13,86,48,65,51,41,87,43,10,87,91,15,44,85,73,37,42,95,18,7,74,60,9,65,93,63,74'''
eval2 = '''30,95,28,84,84,43,66,51,4,11,58,10,13,34,96,71,86,37,64,13,8,87,14,14,49,27,55,69,77,59,57,40,96,24,30,73,95,19,47,15,31,39,15,74,33,57,10'''

def string_a_int (string_in):
    '''Transforma un string separado por comas en una lista de integers'''
    lst_out= list(map(lambda x: int(x), string_in.split(',')))
    return lst_out

nombres = nombres.replace("'","")
lst_nombres = nombres.split(""",""")
lst_eval1 = string_a_int(eval1)
lst_eval2 = string_a_int(eval2)


def calcuar_nota_final():
    '''.....'''
    lst_alu=[]
    suma_total=0
    promedio=0
    for i in range(len(lst_eval1)):
        suma = lst_eval1[i]+ lst_eval2[i]
        aux_tupla=(lst_nombres[i],lst_eval1[i],lst_eval2[i],suma)
        lst_alu.append(aux_tupla)
        suma_total +=suma
    promedio = suma_total / len(lst_eval1)
    return (lst_alu,promedio)


lst_alumnos,promedio=calcuar_nota_final()
print ("""Los alumnos son:
 Nombres  eval1  eval2 sumas """)
for e in lst_alumnos:
    print(e)
print(f"El promedio de todos los alumnos fue: {promedio}")