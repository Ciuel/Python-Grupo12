import os
import csv
import PySimpleGUI as sg
from ..Event_Handlers.score import *
from ..Windows.score import build


def loop(login_window):
    while True:
        event, values = login_window.read()
        if event == sg.WIN_CLOSED:
            break
        

def start():
    score_window = build(True)
    loop(score_window)

    score_window.close()
