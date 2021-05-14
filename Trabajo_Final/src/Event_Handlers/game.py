import os
import json
import time
def check_config(nick):
    """Devueve los valores necesarios para el juego de la configuracion del usuario

    Args:
        nick (str): El nick del jugador

    Returns:
        [tuple]: Los valores de configuracion necesarios para el juego
    """
    with open(os.path.join(os.getcwd(),f"src{os.sep}Data_files{os.sep}datos_usuarios.json"),"r+") as info:
        user_data = json.load(info)
        user_config=next(filter(lambda user:user["nick"]==nick,user_data))["config"]
        return (user_config["Coincidences"], user_config["Level"],user_config["Type of token"],user_config["AppColor"])


def update_button(window, event, value_matrix,type_of_token):
    """Cuando un boton es presionado muestra lo que está en el mismo lugar de la matriz de valores

        window (sg.Window): La ventana donde ocurren los chequeos
        event (str): El boton que produce el evento
        value_matrix (numpy.array): La matriz de los valores a mostrar para el tablero generado
        type_of_token (str): Si se eligio texto o imagenes
    """
    if type_of_token=="Text":
        window[event].update(value_matrix[int(event[-2])][int(event[-1])])
    else:
        window[event].update(image_filename=os.path.join(os.getcwd(),f"src{os.sep}Data_files{os.sep}Images",value_matrix[int(event[-2])][int(event[-1])]), image_size=(118,120),image_subsample=3)


def check_button(value_matrix, cant_coincidences, lista_chequeos, event,window,type_of_token):
    if event not in lista_chequeos:
        lista_chequeos.append(event)
    print(lista_chequeos)
    time.sleep(0.5)
    if all(value_matrix[int(lista_chequeos[0][-2])][int(lista_chequeos[0][-1])]== value_matrix[int(x[-2])][int(x[-1])] for x in lista_chequeos):
        if len(lista_chequeos) == cant_coincidences:
            for eve in lista_chequeos:
                window[eve].update(disabled=True)
            lista_chequeos = []
    else:
        for eve in lista_chequeos:
            window[eve].update("") if type_of_token=="Text" else window[eve].update(image_filename="", image_size=(118, 120))
        lista_chequeos = []

    print(lista_chequeos)
    return lista_chequeos


def button_press(window, event, value_matrix, type_of_token):
    """Chequea si el evento es una ficha

    Args:
        window ([sg.Window]): La ventana de juego armada
        event (str): El evento a chequear si empieza con 'cell'
        value_matrix (numpy.array): La matriz de los valores a mostrar para el tablero generado
        type_of_token (str): Si se eligio texto o imagenes
    """
    if event.startswith("cell"):
        update_button(window, event, value_matrix, type_of_token)
