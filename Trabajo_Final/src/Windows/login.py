import PySimpleGUI as sg

SIZE = (8, 1)


def build():
    # yapf: disable
    layout_login = [
        [sg.Text("Sesion no iniciada", font=("Helvetica", 10),size=(49, 1),justification="right")],
        [sg.Text("MemPy",font=("Helvetica", 40), size=(14, 2),justification="center")],
        [sg.Text("Nick", size=SIZE),sg.InputText(key="-INPUT NICK-")],
        [sg.Text("Contraseña", size=SIZE), sg.InputText(key="-INPUT PASSWORD-")],
        [sg.Button('Iniciar Sesion', pad=(180, 10))],
        [sg.Text("No tiene sesion, Registrarse",size=(50, 1),enable_events="true",text_color="blue", key="Registrarse")],
        [sg.Text("Ayuda",size=(49, 1),enable_events="true",key="Abrir_ayuda",text_color="blue", justification="right")]
    ]
    layout_registro = [
        [sg.Text("Registro",font=("Helvetica", 40),size=(14, 2),justification="center")],
        [sg.Text("Nick", size=SIZE),sg.InputText(key="-REGIS NICK-")],
        [sg.Text("Contraseña", size=SIZE),sg.InputText(key="-REGIS PASSWORD-")],
        [sg.Text("Confirmar contraseña", size=(14,2)),sg.InputText(key="-REGIS CONFIRM PASSWORD-"),sg.Text("", size=SIZE, key="-CONFIRMATION TEXT-")],
        [sg.Text("Edad", size=SIZE),sg.InputText(key="-REGIS AGE-", size=SIZE, enable_events="true")],
        [sg.Text("Genero", size=SIZE),sg.Combo(['Hombre', 'Mujer', 'No binario', 'Otro'],key="-REGIS GENDER-", enable_events="true")],
        [sg.Button('Registrarse', pad=(180, 10), key="-REGIS SAVE-")]
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
                             element_justification='center')

    return login_window