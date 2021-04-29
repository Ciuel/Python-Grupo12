import PySimpleGUI as sg

SIZE = (15, 1)
SEPARACION = (25, 25)


def build(initialConfig, theme="darkblue3"):
    #yapf: disable
    #?Los radiobuttons no pueden tener default incluso forzados
    #(True if initialConfig["Type of token"]=="Text" else "false")
    layout= [
        [sg.Text("Configuracion",font=("Helvetica", 40), size=(14, 2),justification="center",pad=SEPARACION)],
        [sg.Text("Cant Coincidencias: ", size=SIZE,justification="left"),
         sg.Combo([2, 3],key="-CHOOSE COINCIDENCES-",size=(5,1),readonly=True,default_value=f"{initialConfig['Coincidences']}"),
         sg.Text("Ayudas?",size=(7,1)),sg.Radio("Si",1,key='-CHOOSE HELP YES-',default=True if initialConfig["Help"]=="yes" else False),
         sg.Radio("No",1,key='-CHOOSE HELP NO-',default=True if initialConfig["Help"]=="no" else False)],
         [sg.Text("Tipo de casillas: ",size=(12,1),pad=SEPARACION),
         sg.Radio("Texto",2,key="-CHOOSE TYPE1-",default=True if initialConfig["Type of token"]=="Text" else False),
         sg.Radio("Imagenes",2,key="-CHOOSE TYPE2-",default=True if initialConfig["Type of token"]=="Images" else False)],
         [sg.Text("Nivel",size=(8,1)),
          sg.Combo([1, 2, 3],key="-CHOOSE LEVEL-",
                   pad=SEPARACION,readonly=True,default_value=f"{initialConfig['Level']}"),
          sg.Button("Paleta de Colores",pad=SEPARACION,key="-CHOOSE COLOR-")],
         [sg.InputText(f"{initialConfig['VictoryText']}",key="-VICTORY TEXT-"), sg.Text("Ingrese el texto de victoria")],
         [sg.InputText(f"{initialConfig['LooseText']}",key="-LOOSE TEXT-"), sg.Text("Ingrese el texto de derrota")],
         [sg.Button("Guardar Cambios",key="-SAVE CHANGES-",pad=(5,25)),sg.Button("Volver",pad=(5,25),key="-BACK BUTTON-")],
         [sg.Text("",key="-INFO USER-",text_color="blue",size=(30,1))]
    ]
    sg.theme(theme)
    return sg.Window("Configuration MemPy",layout,finalize=True,size=(800, 600),element_justification='center')
    #yapf: enable
