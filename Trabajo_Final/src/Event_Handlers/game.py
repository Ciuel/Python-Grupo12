import os
import json
def check_config(nick):
    with open(os.path.join(os.getcwd(),f"src{os.sep}Data_files{os.sep}datos_usuarios.json"),"r+") as info:
        user_data = json.load(info)
        for user in user_data:
            if user["nick"]==nick:
                return (user["config"]["Coincidences"],
                        user["config"]["Level"],
                        user["config"]["Type of token"])


def update_button(window, event, value_matrix,type_of_token):
    if type_of_token=="Text":
        window[event].update(value_matrix[int(event[-1])][int(event[-2])])
    else:
            window[event].update(image_filename=
            os.path.join(os.getcwd(),f"src{os.sep}Data_files{os.sep}Images",value_matrix[int(event[-1])][int(event[-2])]), image_size=(118,120),image_subsample=3)


def button_press(window, event, value_matrix, type_of_token):
    if event.startswith("cell"):
        update_button(window, event, value_matrix, type_of_token)
