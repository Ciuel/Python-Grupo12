import PySimpleGUI as sg
SIZE= (15,1)
SEPARACION=(25,25)

def build(initialConfig,theme="darkblue3"):
    layout= [
        [sg.Text("Configuracion",font=("Helvetica", 40), size=(14, 2),justification="center",pad=SEPARACION)],
        [sg.Text("Cant Coincidencias: ", size=SIZE,justification="left"), 
         sg.Combo(['2', '3', '4'],key="-CHOOSE COINCIDENCES-", enable_events="true",size=(5,1),readonly="true",default_value=f"{initialConfig['Coincidences']}"),
         sg.Text("Ayudas?",size=(7,1)),sg.Radio("Si",1,key='-CHOOSE HELP YES-',default="true"),
         sg.Radio("No",1,key='-CHOOSE HELP NO-')],
         [sg.Text("Tipo de casillas: ",size=(12,1),pad=SEPARACION),
         sg.Radio("Texto",2,key="-CHOOSE TYPE1-",default="true"),sg.Radio("Imagenes",2,key="-CHOOSE TYPE2-")],
         [sg.Text("Dificultad",size=(8,1)),
          sg.Combo(['Facil', 'Medio', 'Dificil','Muy Dificil'],key="-CHOOSE DIFFICULTY-", 
                   enable_events="true",pad=SEPARACION,readonly="true",default_value=f"{initialConfig['Difficulty']}"),
          sg.Button("Paleta de Colores",pad=SEPARACION,key="-CHOOSE COLOR-")],
         [sg.InputText(f"{initialConfig['VictoryText']}",key="-VICTORY TEXT-"), sg.Text("Ingrese el texto de victoria")],
         [sg.InputText(f"{initialConfig['LooseText']}",key="-LOOSE TEXT-"), sg.Text("Ingrese el texto de derrota")],
         [sg.Button("Guardar Cambios",key="-SAVE CHANGES-",pad=(5,25)),sg.Button("Volver",pad=(5,25),key="-BACK BUTTON-")],
         [sg.Text("",key="-INFO USER-",text_color="blue",size=(30,1))]
    ]
    sg.theme(theme)
    return sg.Window("Configuration MemPy",layout,finalize="true",size=(800, 600),element_justification='center')