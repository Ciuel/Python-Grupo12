import PySimpleGUI as sg
import csv
import os

layout_login = [
    [
        sg.Text("Sesion no iniciada",
                font=("Helvetica", 10),
                size=(49, 1),
                justification="right")
    ],
    [
        sg.Text("MemPy",
                font=("Helvetica", 40),
                size=(14, 2),
                justification="center")
    ], [sg.Text("Nick", size=(8, 1)),
        sg.InputText(key="-INPUT NICK-")],
    [sg.Text("Contraseña", size=(8, 1)),
     sg.InputText(key="-INPUT PASSWORD-")],
    [sg.Button('Iniciar Sesion', pad=(180, 10))],
    [
        sg.Text("No tiene sesion, Registrarse",
                size=(50, 1),
                enable_events="true",
                text_color="blue",
                key="Registrarse")
    ],
    [
        sg.Text("Ayuda",
                size=(49, 1),
                enable_events="true",
                key="Abrir_ayuda",
                text_color="blue",
                justification="right")
    ]
]
layout_registro = [[
    sg.Text("Registro",
            font=("Helvetica", 40),
            size=(14, 2),
            justification="center")
], [sg.Text("Nick", size=(8, 1)),
    sg.InputText(key="-REGIS NICK-")],
                   [
                       sg.Text("Contraseña", size=(8, 1)),
                       sg.InputText(key="-REGIS PASSWORD-")
                   ],
                   [
                       sg.Text("Confirmar contraseña", size=(8, 1)),
                       sg.InputText(key="-REGIS CONFIRM PASSWORD-",
                                    enable_events="true"),
                                    sg.Text("", size=(8, 1),key="-CONFIRMATION TEXT-")
                   ],
                   [
                       sg.Text("Edad", size=(8, 1)),
                       sg.InputText(key="-REGIS AGE-",
                                    size=(8, 1),
                                    enable_events="true")
                   ],
                   [
                       sg.Text("Genero", size=(8, 1)),
                       sg.Combo(['Hombre', 'Mujer', 'No binario', 'Otro'],
                                key="-REGIS GENDER-",
                                enable_events="true")
                   ],
                   [
                       sg.Button('Registrarse',
                                 pad=(180, 10),
                                 key="-REGIS SAVE-")
                   ]]

layout = [[
    sg.Column(layout_login, key='login'),
    sg.Column(layout_registro, visible=False, key='regis'),
]]
window = sg.Window("Login MemPy",
                   layout,
                   finalize="true",
                   size=(800, 600),
                   element_justification='center')
'''
try:
    info = open(f"..{os.sep}Archivos{os.sep}informacion_usuarios.csv", "x")
    writer.writerow(["Nick","Contrasenia","Edad","Genero"])
except:
    info = open(f"..{os.sep}Archivos{os.sep}informacion_usuarios.csv", "a")
    #!USAR ESTE CUANDO LO TERMINEMOS
'''
try:
    info = open(f"Archivos{os.sep}informacion_usuarios.csv", "x")
    writer = csv.writer(info)
    writer.writerow(["Nick","Contrasenia","Edad","Genero"])
except:
    info = open(f"Archivos{os.sep}informacion_usuarios.csv", "a")
    writer = csv.writer(info)

while True:
    #GENERAL
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
        break
    #VENTANA LOGIN
    if event == "Registrarse":
        window['login'].update(visible=False)
        window['regis'].update(visible=True)
    #VENATNA REGISTRO
    if event == "-REGIS AGE-":
        if values['-REGIS AGE-'] and values['-REGIS AGE-'][-1] not in ('0123456789'):
            window['-REGIS AGE-'].update(values['-REGIS AGE-'][:-1])

    if event == "-REGIS CONFIRM PASSWORD-":
        if values["-REGIS CONFIRM PASSWORD-"] != values["-REGIS PASSWORD-"]:
            window["-CONFIRMATION TEXT-"].update("Las contraseñas no coinciden")
        else:
            window["-CONFIRMATION TEXT-"].update("")

    if event == "-REGIS SAVE-":
        if values["-REGIS GENDER-"] in [
                'Hombre', 'Mujer', 'No binario', 'Otro'
        ] and (values["-REGIS NICK-"] != "") and values["-REGIS PASSWORD-"] != "" and values["-REGIS AGE-"] != "":  #Previene registros con campos vacios
            writer.writerow([values["-REGIS NICK-"], values["-REGIS PASSWORD-"],values["-REGIS AGE-"],values["-REGIS GENDER-"]])
            info.close()
            info = open(f"Archivos{os.sep}informacion_usuarios.csv", "r+")
            window['login'].update(visible=True)
            window['regis'].update(visible=False)

info.close()

window.close()