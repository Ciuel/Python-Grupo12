import cairosvg
import csv
import os


with open(
        f"C:{os.sep}Users{os.sep}Tomy{os.sep}Google Drive{os.sep}Facu{os.sep}Seminario Python{os.sep}Práctica{os.sep}Python-Grupo13{os.sep}Trabajo_Final{os.sep}src{os.sep}Data_files{os.sep}Images{os.sep}countries.csv",
        "r+",newline="") as conv:
    csvreader = csv.reader(conv)
    next(csvreader)
    csvreader = list(csvreader)
    csvwriter = csv.writer(conv)
    for e in csvreader:
        e[len(e)-1] = (f"Flag_of_" + e[0] + ".png")
        csvwriter.writerow(e)
