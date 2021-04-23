import PySimpleGUI as sg
SIZE= (15,1)
SEPARACION=(25,25)

def build():
    layout= [
        [sg.Text("Configuracion",font=("Helvetica", 40), size=(14, 2),justification="center",pad=SEPARACION)],
        [sg.Text("Cant Coincidencias: ", size=SIZE,justification="left"), 
         sg.Combo(['2', '3', '4'],key="-CHOOSE COINCIDENCES-", enable_events="true",size=(5,1)),
         sg.Text("Ayudas?",size=(7,1)),sg.Radio("Si",1,key='-CHOOSE HELP YES-'), sg.Radio("No",1,'-CHOOSE HELP NO-')],
         [sg.Text("Tipo de casillas: ",size=(12,1),pad=SEPARACION),
         sg.Radio("Texto ",2,key="-CHOOSE TYPE1-"),sg.Radio("Imagenes ",2,key="-CHOOSE TYPE2-")],
         [sg.Text("Dificultad",size=(8,1)),sg.Combo(['Facil', 'Medio', 'Dificil','Muy Dificil'],key="-CHOOSE DIFFICULTY-", enable_events="true",pad=SEPARACION),
          sg.Button("Paleta de Colores",pad=SEPARACION,key="-CHOOSE COLOR-")],
         [sg.InputText(key="-VICTORY TEXT-"), sg.Text("Ingrese el texto de victoria")],
         [sg.InputText(key="-LOOSE TEXT-"), sg.Text("Ingrese el texto de derrota")],
         [sg.Button("Guardar Cambios",key="-SAVE CHANGES-",pad=(5,25)),sg.Button("Volver",pad=(5,25))],
         [sg.Text("",key="-INFO USER-",text_color="blue",size=(30,1))]
    ]
    
    config_window= sg.Window("Configuration MemPy",layout,finalize="true",size=(800, 600),element_justification='center')
    
    return config_window