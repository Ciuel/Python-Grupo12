import PySimpleGUI as sg
import csv
import os
import textwrap

WINDOW_FONT_SIZE = 15
WINDOW_FONT = "Helvetica"
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
        info_partida.sort(key=lambda x: int(x["Puntos"]))
        for user in info_partida:
            if user["Nick"] == nick:
                scores_table = info_partida[info_partida.index(user) -
                                            3 if info_partida.index(user) >= 3
                                            else 0:info_partida.index(user) +
                                            4]
        return polishing_scores(scores_table)






def build(
        gano,
        theme='DarkBlue3',
        texto_de_victoria='"But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?"',
        texto_de_derrota="Lose",
        tiempo_jugado="1:30:30",
        coincidencias=-1000,
        fallos=-1000,
        puntaje=10000):
    # yapf: disable

    texto_fin=texto_de_victoria if gano else texto_de_derrota



    col= [
                    [sg.Text("Datos de partida",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE * 2))],
                    [sg.Text(textwrap.fill(texto_fin, X_SIZE//10) ,font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],
                    [sg.Text((f"Tiempo jugado: {tiempo_jugado}"),font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE)),
                    sg.Text((f"Coincidencias: {coincidencias}"),font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE)),
                    sg.Text((f"Fallos: {fallos}"),font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],
                    [sg.Text(f"Puntaje: {puntaje}",font=(f"{WINDOW_FONT}", int(WINDOW_FONT_SIZE * 1.5)))]
                    ]


    layout = [
                [col],
                [sg.Listbox(values=scores_print("h"),size=(int(X_SIZE/10),int(Y_SIZE/60)),font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],
                [sg.Button('Menu', key="-MENU-")]]

    # yapf: enable

    #Razon del finalize, probablemente no se necesite interactuar antes de window.read, pero ya está listo
    #If you need to interact with elements prior to calling window.read() you will need to "finalize"
    #your window first using the finalize parameter when you create your Window.
    #"Interacting" means calling that element's methods such as update, draw_line, etc.
    sg.theme(theme)
    return sg.Window("Puntuacion MemPy",
                     layout,
                     finalize=True,
                     element_justification='center',
                     size=(X_SIZE, Y_SIZE),
                     margins=(10, 10))
