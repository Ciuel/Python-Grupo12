import PySimpleGUI as sg
def choose_theme(theme):
    """
        Es uno de los programas ejemplo de PySimpleGUI
        Le permite "navegar" a través de la configuración de apariencia. Haga clic en uno y verá una ventana emergente con el esquema de color que eligió. 
    """
    sg.theme(theme)
    color_list = sg.list_of_look_and_feel_values()
    color_list.sort()
    layout = [[sg.Text('Theme Browser')],
            [sg.Text('Click a look and feel color to see demo window')],
            [
                sg.Listbox(values=color_list,
                            size=(20, 12),
                            key='-LIST-',
                            enable_events=True)
            ], [sg.Button('Exit')]]

    window = sg.Window('Theme Browser', layout)

    while True:  # Event Loop
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        sg.theme(values['-LIST-'][0])
        sg.popup_get_text('This is {}'.format(values['-LIST-'][0]))
    try:
        save_theme = values['-LIST-'][0]
    except (IndexError,TypeError):
        save_theme=theme
    window.close()
    return save_theme


if __name__ == "__main__":
    print(choose_theme())