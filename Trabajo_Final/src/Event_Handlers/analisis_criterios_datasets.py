#TODO cambiar nombre de archivo
import csv
import os
import time
import datetime
import string

def sort_app_data(info,day):
    csvreader = csv.reader(info)
    next(csvreader)
    app_list = list(csvreader)
    app_list = list(map(lambda x: (x[day], x[0] , x[len(app_list[0]) - 1]), app_list))
    if app_list[0][0].isdecimal():
        return sorted(app_list,key=lambda x: float(x[0]),reverse=True)
    else:
        return sorted(app_list, key=lambda x:  x[0])


def manipulate_app_data():
    day=datetime.datetime.today().weekday()
    maniana = range(0, 133)
    if datetime.datetime.now().hour in maniana:
        with open(os.path.join(os.getcwd(),f"src{os.sep}Data_files{os.sep}countries.csv"),"r",encoding="utf-8") as info:
            return sort_app_data(info,day)
    else:
        with open(os.path.join(os.getcwd(),f"src{os.sep}Data_files{os.sep}artists.csv"),"r",encoding="utf-8") as info:
            return sort_app_data(info,day)
