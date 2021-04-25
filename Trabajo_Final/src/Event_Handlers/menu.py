import PySimpleGUI
from ..Components import config  #falta poner juego y stats

#def jugar(window, event):


def configure(window, event, nick, theme):
    if event == "-CONFIG-":
        window.hide()
        config.start(nick, theme)
        window.close()


#def stats(window, event):