import csv
import os
import datetime
import pandas as pd

def sort_app_data(info_path):
    day=datetime.datetime.today().weekday()
    datos = pd.read_csv(info_path)
    datos = datos[[ datos.columns[day], datos.columns[0], datos.columns[datos.columns.size-1]]]
    datos=datos.sort_values(datos.columns[0])
    return datos


def manipulate_app_data():
    """Dependiendo de si es mañana o tarde, abre un dataset distinto para usar en las fichas

    Returns:
        [list]: La lista ordenada con el nombre, la imagen y el criterio de ordenacion
    """
    if datetime.datetime.now().hour in range(0, 12):
        with open(os.path.join(os.getcwd(),f"src{os.sep}Data_files{os.sep}countries.csv"),"r",encoding="utf-8") as info:
            return sort_app_data(info)
    else:
        with open(os.path.join(os.getcwd(),f"src{os.sep}Data_files{os.sep}artists.csv"),"r",encoding="utf-8") as info:
            return sort_app_data(info)
