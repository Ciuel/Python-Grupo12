import PySimpleGUI as sg
from tkinter import font
from ..Constants.constants import WINDOW_FONT, WINDOW_FONT_SIZE, ELEMENT_SIZE, WINDOW_TITLE_FONT, WINDOW_DEFAULT_THEME



def build()->sg.Window:
    """Construye la ventana de login y resgistro, en dos columnas que reprentan los layouts de cada uno y se van intercambiando,

    Returns:
        sg.Window: La ventana para ser utilizada por el resto del programa
    """
    sg.theme(WINDOW_DEFAULT_THEME)
    # yapf: disable
    input_frame_layout=[[sg.Text("Nick", size=ELEMENT_SIZE),sg.InputText(key="-INPUT NICK-")],
    [sg.Text("Contraseña", size=ELEMENT_SIZE),sg.InputText(key="-INPUT PASSWORD-",password_char="*")]]
    layout_login = [#Fonts:Caladea
        [sg.Text("MemPy",font=(WINDOW_TITLE_FONT, WINDOW_FONT_SIZE *3),pad=((0,0),(15,30)),justification="center")],
        [sg.Frame(title="", layout=input_frame_layout,element_justification="center",relief="sunken",border_width=7)],
        [sg.Button('Iniciar Sesion',size=(15,2),key="-LOG IN-",bind_return_key=True,border_width=0)],
        [sg.Text("",pad=((0,180),(0,0)),size=(30,1), key="-W_LOGIN TEXT-",text_color="red")],
        [sg.Text("No tiene sesion, Registrarse",pad=((0,300),(0,0)),enable_events=True,text_color="blue", key="-REGIS-"),
         sg.Text("Ayuda",enable_events=True,key="-HELP-",text_color="blue", justification="right")]
    ]
    register_column_layout=[[sg.Text("Nick", size=ELEMENT_SIZE),
         sg.InputText(key="-REGIS NICK-")],
        [sg.Text("Contraseña", size=ELEMENT_SIZE),
         sg.InputText(key="-REGIS PASSWORD-",password_char="*")],
        [sg.Text("Confirmar contraseña", size=(8,2)),
         sg.InputText(key="-REGIS CONFIRM PASSWORD-",password_char="*")],
        [sg.Text("Edad", size=ELEMENT_SIZE),
         sg.InputText(key="-REGIS AGE-", size=ELEMENT_SIZE, enable_events=True)],
        [sg.Text("Genero", size=ELEMENT_SIZE),
         sg.Combo(['Hombre', 'Mujer', 'No binarie', 'Otro'],key="-REGIS GENDER-", enable_events=True,readonly=True)],
         [sg.Text("", size=(30,1), key="-CONFIRMATION TEXT-",text_color="red")]
         ]
    layout_registro = [
        [sg.Text("Registro",font=(WINDOW_TITLE_FONT, WINDOW_FONT_SIZE *2),pad=((0,0),(0,30)),justification="center")],
        [sg.Column(register_column_layout,element_justification="left")],
        [sg.Button('Registrarse',size=(15,2), key="-REGIS SAVE-")],
        [sg.Button('Atras', key="-REGIS BACK-")]
    ]
    # yapf: enable
    layout = [[
        sg.Column(layout_login, key='-LOGIN LAYOUT-',element_justification="center"),
        sg.Column(layout_registro, visible=False, key='-REGISTER LAYOUT-',element_justification="center"),
    ]]

    login_window = sg.Window("Login MemPy",
                             layout,
                             finalize=True,
                             size=(550,375),
                             element_justification='center')



    return login_window
