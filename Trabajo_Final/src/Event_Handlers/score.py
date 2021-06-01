from ..Components import menu


def check_menu(event,window, theme,nick,vlc_dict):
    if event=="-MENU-":
        window.close()
        menu.start(nick, theme, vlc_dict)
