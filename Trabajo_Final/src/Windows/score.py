import PySimpleGUI as sg

WINDOW_FONT_SIZE = 20
WINDOW_FONT = "Helvetica"


def build(gano,
          theme=sg.DEFAULT_TTK_THEME,
          texto_de_victoria="win",
          texto_de_derrota="lose",
          tiempo_jugado=-1,
          coincidencias=-1,
          fallos=-1,
          puntaje=-1):
    layout = [[
        sg.Text("Datos de partida",
                font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE * 2),
                justification="center")
    ],
              [
                  sg.Text(f"{texto_de_victoria if gano else texto_de_derrota}",
                          font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE),
                          justification="center")
              ],
              [
                  sg.Text(f"Tiempo jugado: {tiempo_jugado}",
                          font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE),
                          justification="left"),
                  sg.Text(f"Coincidencias: {coincidencias}",
                          font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE),
                          justification="center"),
                  sg.Text(f"Fallos: {fallos}",
                          font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE),
                          justification="right")
              ],
              [
                  sg.Text(f"Puntaje: {puntaje}",
                          font=(f"{WINDOW_FONT}", int(WINDOW_FONT_SIZE * 1.5)),
                          justification="center")
              ],
              [
                  sg.Listbox(font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE),
                             values=[("n0", 10), ("n1", 8), ("u", 5),
                                     ("n2", 1)],
                             size=(800, 100))
              ], [sg.Button('Menu', key="-MENU-")]]
    #Razon del finalize, probablemente no se necesite interactuar antes de window.read, pero ya está listo
    #If you need to interact with elements prior to calling window.read() you will need to "finalize"
    #your window first using the finalize parameter when you create your Window.
    #"Interacting" means calling that element's methods such as update, draw_line, etc.
    sg.theme(theme)
    return sg.Window("Puntuacion MemPy",
                     layout,
                     finalize="true",
                     element_justification='center',
                     size=(800, 600))
