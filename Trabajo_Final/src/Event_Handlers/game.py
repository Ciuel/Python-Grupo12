import os
import json
def check_config(nick):
    with open(os.path.join(os.getcwd(),f"src{os.sep}Data_files{os.sep}datos_usuarios.json"),"r+") as info:
        user_data = json.load(info)
        for user in user_data:
            if user["nick"]==nick:
                return (user["config"]["Coincidences"],
                        user["config"]["Level"])


def update_button(window, event, value_matrix):
    window[event].update(value_matrix[int(event[-1])][int(event[-2])])


def button_press(window,event,value_matrix):
    if event.startswith("cell"):
        update_button(window,event,value_matrix)
