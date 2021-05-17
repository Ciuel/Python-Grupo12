import os

#Reusable Constants
LEVEL_DICTIONARY = {
    (1, 2): (4,4),
    (2, 2): (6,4),
    (3, 2): (6,7),
    (1, 3): (6,4),
    (2, 3): (6,5),
    (3, 3): (6,8)
}


DEFAULT_CONFIG = {
    "Coincidences": 2,
    "Help": "yes",
    "Type of token": "Text",
    "Level": 1,
    "AppColor": "darkblue3",
    "VictoryText": "Ganaste!!!",
    "LoseText": ":( mas suerte la proxima"
}

WINDOW_FONT_SIZE = 20
WINDOW_FONT = "Helvetica"


#Pathings

USER_JSON_PATH= f"src{os.sep}Data_files{os.sep}datos_usuarios.json"
GAME_INFO_PATH=f"src{os.sep}Data_files{os.sep}info_partida.csv"
IMAGES_PATH= f"src{os.sep}Data_files{os.sep}Images"