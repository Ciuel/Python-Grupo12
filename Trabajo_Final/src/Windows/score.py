import PySimpleGUI as sg
import csv
import os
import textwrap
from ..Constants.constants import WINDOW_FONT,WINDOW_FONT_SIZE

X_SIZE = 800
Y_SIZE = 600


def polishing_scores(scores):
    return [" " *
            (X_SIZE // 16) + '{:^}  {:^30}  '.format('Nick', 'Puntos')] + list(
                map(
                    lambda x: " " * (X_SIZE // 16) + '{:^}  {:^40}  '.format(
                        str(x["Nick"]), str(x["Puntos"])), scores))


def scores_print(nick):
    with open(f"src{os.sep}Data_files{os.sep}info_partida.csv", "r") as puntos:
        info_partida = list(csv.DictReader(puntos))
        info_partida.sort(key=lambda x: int(x["Puntos"]),reverse=True)
        user = next(filter(lambda user: user["Nick"] == nick, info_partida))
        scores_table = info_partida[info_partida.index(user) -3 if info_partida.index(user) >= 3 else 0:info_partida.index(user) + 4]
        return polishing_scores(scores_table)


def build(
          theme,
          nick,
          texto_fin,
          tiempo_jugado,
          coincidencias,
          fallos,
          puntaje):
    # yapf: disable

    sg.theme(theme)




    col= [
                    [sg.Text("Datos de partida",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE * 2))],
                    [sg.Text(textwrap.fill(texto_fin, X_SIZE//10) ,font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],
                    [sg.Text((f"Tiempo jugado: {tiempo_jugado} segundos"),font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE)),
                    sg.Text((f"Coincidencias: {coincidencias}"),font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE)),
                    sg.Text((f"Fallos: {fallos}"),font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],
                    [sg.Text(f"Puntaje: {puntaje}",font=(f"{WINDOW_FONT}", int(WINDOW_FONT_SIZE * 1.5)))]
                    ]


    layout = [
                [col],
                [sg.Listbox(values=scores_print(nick),size=(int(X_SIZE/10),int(Y_SIZE/60)),font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],
                [sg.Button('Menu', key="-MENU-")]]

    # yapf: enable

    #Razon del finalize, probablemente no se necesite interactuar antes de window.read, pero ya está listo
    #If you need to interact with elements prior to calling window.read() you will need to "finalize"
    #your window first using the finalize parameter when you create your Window.
    #"Interacting" means calling that element's methods such as update, draw_line, etc.
    return sg.Window("Puntuacion MemPy",
                     layout,
                     finalize=True,
                     element_justification='center',
                     size=(X_SIZE, Y_SIZE),
                     margins=(10, 10))
