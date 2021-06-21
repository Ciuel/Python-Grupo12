import os
import datetime
import pandas as pd
from pandas.core.indexes.base import Index
from ..Constants.constants import COUNTRIES_CSV,ARTIST_CSV

def sort_app_data(info_path:str)->pd.DataFrame:
    """Dependiendo del dia de la semana, elige un criterio distinto para ordenar las fichas

    Args:
        info_path (str): El path del archivo a usar para la informacion

    Returns:
        pd.DataFrame: La informacion ordenada por el criterio del dia
    """
    day=datetime.datetime.today().weekday()
    datos = pd.read_csv(info_path)
    datos = datos[[ datos.columns[day], datos.columns[0], datos.columns[datos.columns.size-1]]]
    datos.columns=["order", "text", "image"]
    datos = datos.sort_values(datos.columns[0])
    return datos


def manipulate_app_data() -> pd.DataFrame:
    """Dependiendo de si es mañana o tarde, abre un dataset distinto para usar en las fichas

    Returns:
        pd.DataFrame: La informacion ordenada por sort_app_datas
    """
    if datetime.datetime.now().hour in range(0, 12):
        with open(os.path.join(os.getcwd(),COUNTRIES_CSV),"r",encoding="utf-8") as info:
            return sort_app_data(info)
    else:
        with open(os.path.join(os.getcwd(),ARTIST_CSV),"r",encoding="utf-8") as info:
            return sort_app_data(info)
