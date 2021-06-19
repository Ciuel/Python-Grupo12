import PySimpleGUI as sg
from numpy import pad
from ..Constants.constants import WINDOW_FONT, WINDOW_FONT_SIZE, WINDOW_TITLE_FONT

SIZE = (15, 1)
SEPARACION = (25, 25)
CONFIG_FONT_SIZE = WINDOW_FONT_SIZE-8


def build(initialConfig:dict)->sg.Window:
    #yapf: disable
    """Construye la ventana de configuracion con la informacion de la configuracion de usuario.

    Args:
        initialConfig (dict): Configuracion del usuario

    Returns:
        window (sg.Window): La ventana de configuarcion construida
    """
    sg.theme(initialConfig["Theme"])


    combo_text=[[sg.Text("Cantidad de coincidencias ",font=(WINDOW_FONT,CONFIG_FONT_SIZE))],
    [sg.Text("Nivel",font=(WINDOW_FONT,CONFIG_FONT_SIZE))]]

    radio_text=[[sg.Text("Ayudas",font=(WINDOW_FONT,CONFIG_FONT_SIZE))],[sg.Text("Tipo de casilla ",font=(WINDOW_FONT,CONFIG_FONT_SIZE))]]

    inputtext_text=[[sg.Text("Ingrese el texto de victoria",font=(WINDOW_FONT,CONFIG_FONT_SIZE))],[sg.Text("Ingrese el texto de derrota",font=(WINDOW_FONT,CONFIG_FONT_SIZE))]]

    combo_elements=[[sg.Combo([2, 3],key="-CHOOSE COINCIDENCES-",readonly=True,default_value=f"{initialConfig['Coincidences']}")],
    [sg.Combo([1, 2, 3],key="-CHOOSE LEVEL-",readonly=True,default_value=f"{initialConfig['Level']}")]]

    radio_elements=[[sg.Radio("Si",1,font=(WINDOW_FONT,CONFIG_FONT_SIZE),key='-CHOOSE HELP YES-',default=True if initialConfig["Help"]=="yes" else False),
         sg.Radio("No",1,font=(WINDOW_FONT,CONFIG_FONT_SIZE),key='-CHOOSE HELP NO-',default=True if initialConfig["Help"]=="no" else False)],

         [sg.Radio("Texto",2,font=(WINDOW_FONT,CONFIG_FONT_SIZE),key="-CHOOSE TYPE1-",default=True if initialConfig["Type of token"]=="Text" else False),
         sg.Radio("Imagenes",2,font=(WINDOW_FONT,CONFIG_FONT_SIZE),key="-CHOOSE TYPE2-",default=True if initialConfig["Type of token"]=="Images" else False)]]

    input_elements=[[sg.InputText(f"{initialConfig['VictoryText']}",key="-VICTORY TEXT-")],[sg.InputText(f"{initialConfig['LoseText']}",key="-Lose TEXT-")]]

    layout_radio=[[sg.Column(radio_text,element_justification="right"),sg.Column(radio_elements,element_justification="left")]]
    layout_combo=[[sg.Column(combo_text,element_justification="right"),sg.Column(combo_elements,element_justification="left")]]
    layout_inputtext=[[sg.Column(inputtext_text,element_justification="left"),sg.Column(input_elements,element_justification="left")]]



    layout= [
        [sg.Text("Configuracion",font=(WINDOW_TITLE_FONT, WINDOW_FONT_SIZE*2), size=(14, 2),justification="center",pad=(None,(20,0)))],

        [sg.Column(layout_combo,element_justification="right"),
        sg.Column(layout_radio,element_justification="right")],

        [sg.Button("Paleta de Colores",border_width=0,font=(WINDOW_FONT,CONFIG_FONT_SIZE),pad=(None,(5,5)),key="-CHOOSE COLOR-")],

        [sg.Column(layout_inputtext,element_justification="left")],

         [sg.Text("",font=(WINDOW_FONT,CONFIG_FONT_SIZE),key="-INFO USER-",text_color="blue",size=(37,1),pad=((25,0),0))],
         [sg.Button("Guardar Cambios",border_width=0,font=(WINDOW_FONT,CONFIG_FONT_SIZE),key="-SAVE CHANGES-",pad=((0,5),(25,5))),
         sg.Button("Volver",border_width=0,pad=(0,(25,5)),key="-BACK BUTTON-",font=(WINDOW_FONT,CONFIG_FONT_SIZE))]
    ]
    return sg.Window("Configuration MemPy",layout,finalize=True,margins=(10, 10),element_justification='center')
    #yapf: enable
