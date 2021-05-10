from PIL import Image
import os


pathlist = [file for file in os.listdir(f"C:{os.sep}Users{os.sep}Tomy{os.sep}Google Drive{os.sep}Facu{os.sep}Seminario Python{os.sep}Práctica{os.sep}Python-Grupo13{os.sep}Trabajo_Final{os.sep}src{os.sep}Data_files{os.sep}Images") if file.endswith(('jpeg', 'png', 'jpg'))]
for filepath in pathlist:
    f = Image.open(os.path.join((f"C:{os.sep}Users{os.sep}Tomy{os.sep}Google Drive{os.sep}Facu{os.sep}Seminario Python{os.sep}Práctica{os.sep}Python-Grupo13{os.sep}Trabajo_Final{os.sep}src{os.sep}Data_files{os.sep}Images"),filepath))
    f=f.resize((400,400))
    f.save(os.path.join((
        f"C:{os.sep}Users{os.sep}Tomy{os.sep}Google Drive{os.sep}Facu{os.sep}Seminario Python{os.sep}Práctica{os.sep}Python-Grupo13{os.sep}Trabajo_Final{os.sep}src{os.sep}Data_files{os.sep}Images"
    ), filepath))

