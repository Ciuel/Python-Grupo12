import PySimpleGUI as sg
from ..Constants.constants import WINDOW_FONT,WINDOW_FONT_SIZE

#TODO: Cambiar keys de login y regis

SIZE = (8, 1)


def build():
    """Construye la ventana de login y resgistro, en dos columnas que reprentan los layouts de cada uno y se van intercambiando,

    Returns:
        sg.Window: La ventana para ser utilizada por el resto del programa
    """
    # yapf: disable
    layout_login = [
        [sg.Text("MemPy",font=(WINDOW_FONT, WINDOW_FONT_SIZE *2), size=(14, 2),justification="center")],
        [sg.Text("Nick", size=SIZE),
         sg.InputText(key="-INPUT NICK-")],
        [sg.Text("Contraseña", size=SIZE),
         sg.InputText(key="-INPUT PASSWORD-",password_char="*")],
        [sg.Button('Iniciar Sesion',size=(15,2), pad=(180, 10),key="-LOG IN-")],
        [sg.Text("", size=(30,1), key="-W_LOGIN TEXT-",text_color="red")],
        [sg.Text("No tiene sesion, Registrarse",size=(50, 1),enable_events=True,text_color="blue", key="-REGIS-"),
         sg.Text("Ayuda",enable_events=True,key="-HELP-",text_color="blue", justification="right")]
    ]
    layout_registro = [
        [sg.Text("Registro",font=(WINDOW_FONT, WINDOW_FONT_SIZE *2),size=(14, 2),justification="center")],
        [sg.Text("Nick", size=SIZE),
         sg.InputText(key="-REGIS NICK-")],
        [sg.Text("Contraseña", size=SIZE),
         sg.InputText(key="-REGIS PASSWORD-",password_char="*")],
        [sg.Text("Confirmar contraseña", size=(8,2)),
         sg.InputText(key="-REGIS CONFIRM PASSWORD-",password_char="*")],
        [sg.Text("Edad", size=SIZE),
         sg.InputText(key="-REGIS AGE-", size=SIZE, enable_events=True)],
        [sg.Text("Genero", size=SIZE),
         sg.Combo(['Hombre', 'Mujer', 'No binario', 'Otro'],key="-REGIS GENDER-", enable_events=True,readonly=True)],
        [sg.Button('Registrarse',size=(15,2), pad=(180, 10), key="-REGIS SAVE-")],
        [sg.Text("", size=(30,1), key="-CONFIRMATION TEXT-",text_color="red")],
        [sg.Button('Atras', pad= ((360,0), 0), key="-REGIS BACK-")]
    ]
    # yapf: enable
    layout = [[
        sg.Column(layout_login, key='-LOGIN LAYOUT-'),
        sg.Column(layout_registro, visible=False, key='-REGISTER LAYOUT-'),
    ]]

    login_window = sg.Window("Login MemPy",
                             layout,
                             finalize=True,
                             size=(600,500),
                             margins=(None,40),
                             element_justification='center')



    return login_window
