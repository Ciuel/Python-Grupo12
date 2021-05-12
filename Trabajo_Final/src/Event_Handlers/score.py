from ..Components import menu


def check_menu(event,window, theme,nick):
    if event=="-MENU-":
        window.close()
        menu.start(nick, theme)
