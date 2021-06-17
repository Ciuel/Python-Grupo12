from ..Components import menu
from ..Constants.constants import BUTTON_SOUND_PATH, vlc_play_sound


def check_menu(event,window, theme,nick,vlc_dict):
    if event=="-MENU-":
        vlc_play_sound(vlc_dict, BUTTON_SOUND_PATH)
        window.close()
        menu.start(nick, theme, vlc_dict)
