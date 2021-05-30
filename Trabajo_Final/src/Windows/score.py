import PySimpleGUI as sg
import csv
import os
import textwrap
from ..Constants.constants import WINDOW_FONT,WINDOW_FONT_SIZE

X_SIZE = 800
Y_SIZE = 600


def polishing_scores(scores):
    return ["Posicion    Nick       Puntos"]+[(f'''{tup[0]:<15} {tup[1]["Nick"]:<15} {tup[1]["Puntos"]:<15}''')  for tup in scores]


def scores_print():
    with open(f"src{os.sep}Data_files{os.sep}info_partida.csv", "r") as puntos:
        info_partida = list(csv.DictReader(puntos))
        game_number= info_partida[-1]["Numero de partida"]
        level= info_partida[-1]["Nivel"]

        info_partida= list(filter(lambda game: game["Nivel"] == level, info_partida))

        info_partida.sort(key=lambda x: int(x["Puntos"]),reverse=True)

        game_index=info_partida.index(next(filter(lambda n: n.get('Numero de partida') == game_number, info_partida)))

        info_partida = info_partida[game_index - 3:game_index + 4] if game_index > 3 else info_partida[:game_index + 4]

        scores_table = [(info_partida.index(elem),elem) for elem in info_partida]


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
                [sg.Listbox(values=scores_print(),size=(int(X_SIZE/10),int(Y_SIZE/60)),font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],
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
