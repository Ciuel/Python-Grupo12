from ..Windows.config import build
import PySimpleGUI as sg

def loop(config_window):
    while True:
        event,values= config_window.read()
        if event == sg.WIN_CLOSED:
            break


def start():
    config_window=build()
    loop(config_window)
    config_window.close()
    
    