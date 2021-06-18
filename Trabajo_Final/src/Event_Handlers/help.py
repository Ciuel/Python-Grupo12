import PySimpleGUI as sg
def check_login(help_window:sg.Window,event:str):
    """Chequea si el usuario vuelve al login

    Args:
        help_window (sg.Window): La ventana de ayuda donde ocurre el chequeo
        event (str): El evento a chequear
    """    
    if event == "-BACK-":
        help_window.close()