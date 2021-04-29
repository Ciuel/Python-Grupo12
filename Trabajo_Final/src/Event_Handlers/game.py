import os
import json
def check_config(nick):
    with open(os.path.join(os.getcwd(),f"src{os.sep}Data_files{os.sep}datos_usuarios.json"),"r+") as info:
        user_data = json.load(info)
        for user in user_data:
            if user["nick"]==nick:
                return (user["config"]["Coincidences"],
                        user["config"]["Level"])


words = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t"]


def obtener_datos(cant_coincidences,level):
    print(cant_coincidences, level)
