from ArchivoStrings import *
#from statistics import mean


def string_a_int(string_in):
    '''Transforma un string separado por comas en una lista de integers'''
    return list(map(lambda x: int(x), string_in.split(',')))


def modificando_string(string_in):
    '''Borra las comillas extra del archivo de nombres'''
    string_modificado = string_in.replace("'", "")
    return string_modificado.split(""",""")


def calcuar_nota_final(lst_nombres, lst_eval1, lst_eval2):
    '''Toma todos los datos de los alumnos y los convierte a una lista de tuplas agregandole la suma de las evaluaciones'''
    lst_alu = []
    suma_total = 0
    promedio = 0
    for i in range(len(lst_eval1)):
        suma = lst_eval1[i] + lst_eval2[i]
        aux_tupla = (lst_nombres[i], lst_eval1[i], lst_eval2[i], suma)
        lst_alu.append(aux_tupla)
        suma_total += suma
    promedio = suma_total / len(lst_eval1)
    return (lst_alu, promedio)


def reporteAlumnos(lst_alu, criterio_reporte, valor_min=0, valor_max=200):
    """Recibe un máximo, un mínimo y devuelve los nombres de los alumnos que cumplen con el criterio"""
    if criterio_reporte in range(1,4):
        return list(filter((lambda alumno: alumno[criterio_reporte] in range(valor_min,valor_maximo+1)),lst_alu))
    else:
        return "criterio fuera de rango"


def ordenar(lst_reordenado, criterio_para_reordenar):
    """Reordena una lista lista de menor a mayor usando la función sorted y el criterio elegido por el usuario"""
    if criterio_para_reordenar in range(0,4):
        return sorted(lst_reordenado, key=lambda x: x[criterio_para_reordenar])
    else:
        return 'Valor fuera de rango'




#Main
lst_nombres = modificando_string(nombres) #Nombres ahora se encuentra en el modulo importado
lst_eval1 = string_a_int(eval1)  #eval1 ahora se encuentra en el modulo importado
lst_eval2 = string_a_int(eval2)  #eval2 ahora se encuentra en el modulo importado
lst_alumnos, promedio = calcuar_nota_final(lst_nombres, lst_eval1, lst_eval2)

print("""Los alumnos son:
 Nombres  eval1  eval2 sumas """)
for e in lst_alumnos:
    print(e)
print(f'''El promedio de todos los alumnos fue: {promedio}''')
print()
criterio = int(
    input(f'''Escriba el criterio por el cual desea obtener el reporte: 
          1 Para obtener el reporte por la primera evaluacion,
          2 Para obtener el reporte por la segunda evaluacion,
          3 Para obtener el reporte por la suma de las evaluaciones 
          \n'''))
#\n para saltear
valor_minimo = int(
    input((f'Escriba el valor minimo para buscar en el reporte ')))
valor_maximo = int(
    input(f'Escriba el valor maximo para buscar en el reporte '))

print()
print('Los alumnos que cumplen con el criterio son: ',
      reporteAlumnos(lst_alumnos, criterio, valor_minimo, valor_maximo))

print()

criterio_de_reordenado = int(
    input(f'''Escriba el criterio por el cual desea reordenar el reporte: 
          0 Para obtener el reporte por el nombre,
          1 Para obtener el reporte por la primera evaluacion,
          2 Para obtener el reporte por la segunda evaluacion,
          3 Para obtener el reporte por la suma de las evaluaciones 
          '''))

print(ordenar(lst_alumnos, criterio_de_reordenado))