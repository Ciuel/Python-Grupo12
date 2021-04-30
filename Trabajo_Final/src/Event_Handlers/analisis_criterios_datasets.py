#TODO cambiar nombre de archivo
import csv
import os
import time
import datetime as dt


def manipulate_app_data():
    with open(os.path.join(os.getcwd(),f"src{os.sep}Data_files{os.sep}appstore_games.csv"),"r",encoding="utf-8") as info:
        day=dt.datetime.today().weekday()
        maniana, tarde = range(0, 12), range(13, 23)
        if day==0:
            if dt.datetime.hour in maniana:
                print(f"Hoy es {day} y es la mañana")
            else:
                print(f"Hoy es {day} y es la tarde")
        elif day==1:
            if dt.datetime.hour in maniana:
                print(f"Hoy es {day} y es la mañana")
            else:
                print(f"Hoy es {day} y es la tarde")
        elif day==2:
            if dt.datetime.hour in maniana:
                print(f"Hoy es {day} y es la mañana")
            else:
                print(f"Hoy es {day} y es la tarde")
        elif day==3:
            if dt.datetime.hour in maniana:
                print(f"Hoy es {day} y es la mañana")
            else:
                print(f"Hoy es {day} y es la tarde")
        elif day==4:
            if dt.datetime.hour in maniana:
                print(f"Hoy es {day} y es la mañana")
            else:
                print(f"Hoy es {day} y es la tarde")
        elif day==5:
            if dt.datetime.hour in maniana:
                print(f"Hoy es {day} y es la mañana")
            else:
                print(f"Hoy es {day} y es la tarde")
        else:
            if dt.datetime.hour in maniana:
                print(f"Hoy es {day} y es la mañana")
            else:
                print(f"Hoy es {day} y es la tarde")



manipulate_app_data()
