import PySimpleGUI as sg

SIZE = (8, 1)


def build(nick):
    # yapf: enable

    layout = [[sg.Text(f"Bienvenido {nick}",font=("Helvetica", 50),size=(49, 1),justification="center")]
    ]
    # yapf: disable

    game_window = sg.Window("MemPy",
                             layout,
                             finalize="true",
                             size=(800, 600),
                             element_justification='center',
                             margins=(10,10))
    return game_window
