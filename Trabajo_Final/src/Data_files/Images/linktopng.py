import csv
import os
from PIL import Image
with open(f"C:{os.sep}Users{os.sep}Tomy{os.sep}Google Drive{os.sep}Facu{os.sep}Seminario Python{os.sep}Práctica{os.sep}Python-Grupo13{os.sep}Trabajo_Final{os.sep}src{os.sep}Data_files{os.sep}Images{os.sep}artists.csv",
        "r+",newline="",encoding="utf-8") as conv:
    csvfile=csv.DictReader(conv)
    for e in csvfile:
        r = Image.open(e["painting"])
        r.save(e["painting"])

