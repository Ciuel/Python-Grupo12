import PySimpleGUI as sg
import csv
import os

WINDOW_FONT_SIZE = 20
WINDOW_FONT = "Helvetica"

def polishing_scores(scores):
    output= ""
    for user in scores:
        output += (" ".join(user)+ "\n")
    return output
#TODO Terminar el formateo de la tabla 

def scores_print(puntos, nick):
    csvreader = csv.reader(puntos)
    header= ""
    scores_table=""
    for cat in  next(csvreader):
        header += cat+" "
    csvreader = list(csvreader)
    csvreader.sort(key=lambda x: x[1])
    if len(csvreader) < 7:
        scores_table += polishing_scores(csvreader) + "\n"
    else:
        for index in range(len(csvreader)):
            if nick in csvreader[index]:
                if index < 3:
                    scores_table+=polishing_scores(csvreader[:index + 4])+"\n"
                else:
                    scores_table += polishing_scores(csvreader[index - 3:index + 4]) + "\n"
    print(header+"\n"+scores_table)


def build(gano,
          theme='DarkBlue3',
          texto_de_victoria="win",
          texto_de_derrota="lose",
          tiempo_jugado=-1,
          coincidencias=-1,
          fallos=-1,
          puntaje=-1):

    layout = [[
            sg.Text("Datos de partida",
                    font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE * 2),
                    justification="center")
    ],
                    [
                    sg.Text(
                            f"{texto_de_victoria if gano else texto_de_derrota}",
                            font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE),
                            justification="center")
                    ],
                    [
                    sg.Text(f"Tiempo jugado: {tiempo_jugado}",
                            font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE),
                            justification="left"),
                    sg.Text(f"Coincidencias: {coincidencias}",
                            font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE),
                            justification="center"),
                    sg.Text(f"Fallos: {fallos}",
                            font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE),
                            justification="right")
                    ],
                    [
                    sg.Text(f"Puntaje: {puntaje}",
                            font=(f"{WINDOW_FONT}",
                                    int(WINDOW_FONT_SIZE * 1.5)),
                            justification="center")
                    ],
                    [
                    sg.Output(font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE),
                                    size=(800, 100),echo_stdout_stderr="true")
                    ], [sg.Button('Menu', key="-MENU-")]]

    #Razon del finalize, probablemente no se necesite interactuar antes de window.read, pero ya está listo
    #If you need to interact with elements prior to calling window.read() you will need to "finalize"
    #your window first using the finalize parameter when you create your Window.
    #"Interacting" means calling that element's methods such as update, draw_line, etc.
    sg.theme(theme)
    return sg.Window("Puntuacion MemPy",
                    layout,
                    finalize="true",
                    element_justification='center',
                    size=(800, 600))
