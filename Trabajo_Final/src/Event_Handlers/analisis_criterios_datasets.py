import csv
import os
import datetime

def sort_app_data(info,day):
    """Itera el dataset csv y nos devuelve una lista con el nombre, la imagen y el criterio de ordenacion

    Args:
        info (csv): El dataset a utilizar
        day (int): El dia de la semana que actua como indice de la columna del criterio

    Returns:
        [list]: La lista ordenada con el nombre, la imagen y el criterio de ordenacion
    """
    csvreader = csv.reader(info)
    next(csvreader)  #Saltea el encabezado
    app_list = list(csvreader)
    app_list = list(map(lambda x: (x[day], x[0] , x[len(app_list[0]) - 1]), app_list))
    return sorted(app_list,key=lambda x: float(x[0]),reverse=True) if app_list[0][0].isdecimal() else sorted(app_list, key=lambda x:  x[0])


def manipulate_app_data():
    """Dependiendo de si es mañana o tarde, abre un dataset distinto para usar en las fichas

    Returns:
        [list]: La lista ordenada con el nombre, la imagen y el criterio de ordenacion
    """
    day=datetime.datetime.today().weekday()
    if datetime.datetime.now().hour in range(0, 12):
        with open(os.path.join(os.getcwd(),f"src{os.sep}Data_files{os.sep}countries.csv"),"r",encoding="utf-8") as info:
            return sort_app_data(info,day)
    else:
        with open(os.path.join(os.getcwd(),f"src{os.sep}Data_files{os.sep}artists.csv"),"r",encoding="utf-8") as info:
            return sort_app_data(info,day)
