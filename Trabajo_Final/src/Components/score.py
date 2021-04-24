import os
import csv
import PySimpleGUI as sg
from ..Event_Handlers.score import *
from ..Windows.score import build,scores_print


def loop(login_window):
    with open(f"src{os.sep}Data_files{os.sep}info_partida.csv", "r") as puntos:
        scores_print(puntos, "d")
    while True:
        event, values = login_window.read()
        if event == sg.WIN_CLOSED:
            break
        

def start():
    score_window = build(True)
    loop(score_window)

    score_window.close()
