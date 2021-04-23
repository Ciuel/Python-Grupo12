import os
import csv
import PySimpleGUI as sg
from ..Event_Handlers.score import *
from ..Windows.score import build
from ..Windows.Theme_browser import choose_theme


def loop(login_window):
    while True:
        event, values = login_window.read()
        if event == sg.WIN_CLOSED:
            break
        

def start():
    score_window = build(True,theme=choose_theme())
    loop(score_window)

    score_window.close()
