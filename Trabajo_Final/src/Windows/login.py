import PySimpleGUI as sg

SIZE = (8, 1)


def build():
    # yapf: disable
    layout_login = [
        [sg.Text("Sesion no iniciada", font=("Helvetica", 10),size=(49, 1),justification="right")],
        [sg.Text("MemPy",font=("Helvetica", 40), size=(14, 2),justification="center")],
        [sg.Text("Nick", size=SIZE),sg.InputText(key="-INPUT NICK-")],
        [sg.Text("Contraseña", size=SIZE), sg.InputText(key="-INPUT PASSWORD-",password_char="*")],
        [sg.Button('Iniciar Sesion', pad=(180, 10),key="-LOG IN-")],
        [sg.Text("", size=(30,1), key="-W_LOGIN TEXT-",text_color="red")],
        [sg.Text("No tiene sesion, Registrarse",size=(50, 1),enable_events="true",text_color="blue", key="-REGIS-")],
        [sg.Text("Ayuda",size=(49, 1),enable_events="true",key="-HELP-",text_color="blue", justification="right")]
    ]
    layout_registro = [
        [sg.Text("Registro",font=("Helvetica", 40),size=(14, 2),justification="center")],
        [sg.Text("Nick", size=SIZE),sg.InputText(key="-REGIS NICK-")],
        [sg.Text("Contraseña", size=SIZE),sg.InputText(key="-REGIS PASSWORD-",password_char="*")],
        [sg.Text("Confirmar contraseña", size=(8,2)),sg.InputText(key="-REGIS CONFIRM PASSWORD-",password_char="*")],
        [sg.Text("Edad", size=SIZE),sg.InputText(key="-REGIS AGE-", size=SIZE, enable_events="true")],
        [sg.Text("Genero", size=SIZE),sg.Combo(['Hombre', 'Mujer', 'No binario', 'Otro'],key="-REGIS GENDER-", enable_events="true")],
        [sg.Button('Registrarse', pad=(180, 10), key="-REGIS SAVE-")],
        [sg.Text("", size=(30,1), key="-CONFIRMATION TEXT-",text_color="red")],
        [sg.Button('Atras', pad= ((360,0), 0), key="-REGIS BACK-")]

    ]
    # yapf: enable
    layout = [[
        sg.Column(layout_login, key='login'),
        sg.Column(layout_registro, visible=False, key='regis'),
    ]]

    login_window = sg.Window("Login MemPy",
                             layout,
                             finalize="true",
                             size=(800, 600),
                             element_justification='center',
                             margins=(10,10))


    return login_window
