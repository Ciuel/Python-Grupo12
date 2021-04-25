import PySimpleGUI
from ..Components import config,game  #falta poner y stats

def jugar(window, event,nick):
    if event == "-PLAY-":
        window.hide()
        game.start(nick)
        window.close()


def configure(window, event, nick, theme):
    if event == "-CONFIG-":
        window.hide()
        config.start(nick, theme)
        window.close()


#def stats(window, event):