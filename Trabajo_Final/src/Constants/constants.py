import os
import sys

#Reusable Constants
LEVEL_DICTIONARY = {
    (1, 2): (4,4),
    (2, 2): (6,4),
    (3, 2): (6,7),
    (1, 3): (6,4),
    (2, 3): (6,5),
    (3, 3): (6,8)
}


def vlc_play_sound(vlc_dict, media):
    if vlc_dict["vlc"]:
        media_sound = os.path.join(os.getcwd(), media)
        button_press = vlc_dict["player_sounds"].get_instance().media_new(
            media_sound)
        vlc_dict["player_sounds"].set_media(button_press)
        vlc_dict["player_sounds"].play()


DEFAULT_CONFIG = {
    "Coincidences": 2,
    "Help": "yes",
    "Type of token": "Text",
    "Level": 1,
    "AppColor": "darkblue3",
    "VictoryText": "Ganaste!!!",
    "LoseText": ":( mas suerte la proxima"
}

HELP_COOLDOWN_TIME=5
WINDOW_FONT_SIZE = 20
WINDOW_FONT = "Helvetica"
MAX_VALUE = sys.maxsize

#Pathings

USER_JSON_PATH= f"src{os.sep}Data_files{os.sep}datos_usuarios.json"
GAME_INFO_PATH = f"src{os.sep}Data_files{os.sep}Datos_de_partida.csv"
IMAGES_PATH = f"src{os.sep}Data_files{os.sep}Images"
MENU_MUSIC_PATH = f"src{os.sep}Music_files{os.sep}Menu.mp3"
MENU_SOUND_PATH = f"src{os.sep}Music_files{os.sep}Menu_Button.mp3"
HELP_SOUND_PATH = f"src{os.sep}Music_files{os.sep}Help.mp3"
WIN_SOUND_PATH = f"src{os.sep}Music_files{os.sep}Win.mp3"
LOSE_SOUND_PATH = f"src{os.sep}Music_files{os.sep}Lose.mp3"
RIGHT_SOUND_PATH = f"src{os.sep}Music_files{os.sep}Right.mp3"
WRONG_SOUND_PATH = f"src{os.sep}Music_files{os.sep}Wrong.mp3"
BUTTON_SOUND_PATH = f"src{os.sep}Music_files{os.sep}Button.mp3"
