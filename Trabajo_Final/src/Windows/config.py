import PySimpleGUI as sg
from ..Constants.constants import WINDOW_FONT, WINDOW_FONT_SIZE, WINDOW_TITLE_FONT

SIZE = (15, 1)
SEPARACION = (25, 25)
CONFIG_WINDOW_FONT_SIZE = WINDOW_FONT_SIZE//2


def build(initialConfig:dict)->sg.Window:
    #yapf: disable
    """Construye la ventana de configuracion con la informacion de la configuracion de usuario.

    Args:
        initialConfig (dict): Configuracion del usuario

    Returns:
        window (sg.Window): La ventana de configuarcion construida
    """

    sg.theme(initialConfig["Theme"])
    layout= [
        [sg.Text("Configuracion",font=(WINDOW_TITLE_FONT, WINDOW_FONT_SIZE*2), size=(14, 2),justification="center",pad=(None,(20,0)))],
        [sg.Text("Cant Coincidencias: ",font=(WINDOW_FONT,CONFIG_WINDOW_FONT_SIZE), size=SIZE,justification="left"),
         sg.Combo([2, 3],key="-CHOOSE COINCIDENCES-",size=(5,1),readonly=True,default_value=f"{initialConfig['Coincidences']}"),
         sg.Text("Ayudas?",font=(WINDOW_FONT,CONFIG_WINDOW_FONT_SIZE),size=(7,1)),sg.Radio("Si",1,key='-CHOOSE HELP YES-',default=True if initialConfig["Help"]=="yes" else False),
         sg.Radio("No",1,key='-CHOOSE HELP NO-',default=True if initialConfig["Help"]=="no" else False)],
         [sg.Text("Tipo de casilla: ",font=(WINDOW_FONT,CONFIG_WINDOW_FONT_SIZE),size=(12,1),pad=SEPARACION),
         sg.Radio("Texto",2,key="-CHOOSE TYPE1-",default=True if initialConfig["Type of token"]=="Text" else False),
         sg.Radio("Imagenes",2,key="-CHOOSE TYPE2-",default=True if initialConfig["Type of token"]=="Images" else False)],
         [sg.Text("Nivel",font=(WINDOW_FONT,CONFIG_WINDOW_FONT_SIZE),size=(8,1)),
          sg.Combo([1, 2, 3],key="-CHOOSE LEVEL-",
                   pad=SEPARACION,readonly=True,default_value=f"{initialConfig['Level']}"),
          sg.Button("Paleta de Colores",font=(WINDOW_FONT,CONFIG_WINDOW_FONT_SIZE),pad=SEPARACION,key="-CHOOSE COLOR-")],
         [sg.InputText(f"{initialConfig['VictoryText']}",key="-VICTORY TEXT-"), sg.Text("Ingrese el texto de victoria")],
         [sg.InputText(f"{initialConfig['LoseText']}",key="-Lose TEXT-"), sg.Text("Ingrese el texto de derrota")],
         [sg.Button("Guardar Cambios",font=(WINDOW_FONT,CONFIG_WINDOW_FONT_SIZE),key="-SAVE CHANGES-",pad=((0,5),(25,5))),sg.Button("Volver",pad=(0,(25,5)),key="-BACK BUTTON-")],
         [sg.Text("",font=(WINDOW_FONT,CONFIG_WINDOW_FONT_SIZE),key="-INFO USER-",text_color="blue",size=(37,1),pad=((25,0),0))]
    ]
    return sg.Window("Configuration MemPy",layout,finalize=True,size=(600, 500),element_justification='center')
    #yapf: enable
