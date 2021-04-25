import PySimpleGUI as sg
import csv
import os
from textwrap import wrap

WINDOW_FONT_SIZE = 15
WINDOW_FONT = "Helvetica"
X_SIZE=800
Y_SIZE=600


def polishing_scores(scores):
    output = ""
    for user in scores:
        for dato in user:
            output += (f"{dato:^12}")
        output += "\n"
    return output


#TODO Terminar el formateo de la tabla para que no queden numeros desalineados


def scores_print(puntos, nick):
    csvreader = csv.reader(puntos)
    header = ""
    for cat in next(csvreader):
        header += (f"{cat:^10}")
    csvreader = list(csvreader)
    csvreader.sort(key=lambda x: int(x[1]))
    if len(csvreader) < 7:
        scores_table = polishing_scores(csvreader) + "\n"
    else:
        for index in range(len(csvreader)):
            if nick in csvreader[index]:
                if index < 3:
                    scores_table = polishing_scores(
                        csvreader[:index + 4]) + "\n"
                else:
                    scores_table = polishing_scores(
                        csvreader[index - 3:index + 4]) + "\n"
    print(header + "\n" + scores_table)


def wrap_texto_fin(texto_fin):
    texto_fin_proce=""
    if len(texto_fin)>X_SIZE//10:
        wrap_list= wrap(texto_fin,X_SIZE//10)
        for string in wrap_list:
            texto_fin_proce+=string + "\n"
        return texto_fin_proce, len(wrap_list)
    else:
        return texto_fin, 1


def build(
        gano,
        theme='DarkBlue3',
        texto_de_victoria="Win",
        texto_de_derrota="Lose",
        tiempo_jugado="1:30:30",
        coincidencias=-1000,
        fallos=-1000,
        puntaje=10000):
    # yapf: disable

    texto_fin=texto_de_victoria if gano else texto_de_derrota
    texto_fin,line_amount=wrap_texto_fin(texto_fin)


    col= [
                    [sg.Text("Datos de partida",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE * 2))],
                    [sg.Text(texto_fin ,font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE),size=(None,line_amount))],
                    [sg.Text((f"Tiempo jugado: {tiempo_jugado}"),font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE)),
                    sg.Text((f"Coincidencias: {coincidencias}"),font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE)),
                    sg.Text((f"Fallos: {fallos}"),font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],
                    [sg.Text(f"Puntaje: {puntaje}",font=(f"{WINDOW_FONT}", int(WINDOW_FONT_SIZE * 1.5)))]
                    ]


    layout = [
                [col],
                [sg.Output(size=(int(X_SIZE/10),int(Y_SIZE/60)),font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE),echo_stdout_stderr="true")],
                [sg.Button('Menu', key="-MENU-")]]

    # yapf: enable

    #Razon del finalize, probablemente no se necesite interactuar antes de window.read, pero ya está listo
    #If you need to interact with elements prior to calling window.read() you will need to "finalize"
    #your window first using the finalize parameter when you create your Window.
    #"Interacting" means calling that element's methods such as update, draw_line, etc.
    sg.theme(theme)
    return sg.Window("Puntuacion MemPy",
                     layout,
                     finalize="true",
                     element_justification='center',
                     size=(X_SIZE, Y_SIZE),
                     margins=(10, 10))
