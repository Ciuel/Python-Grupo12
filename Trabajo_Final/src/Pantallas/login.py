import csv
import os


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

    change_login_layout()
    age_field_check()

    if event == "-REGIS SAVE-":
        if values["-REGIS GENDER-"] in [
                'Hombre', 'Mujer', 'No binario', 'Otro'
        ] and (values["-REGIS NICK-"] !=
               "") and values["-REGIS PASSWORD-"] != "" and values[
                   "-REGIS AGE-"] != "":  #Previene registros con campos vacios
            writer.writerow([
                values["-REGIS NICK-"], values["-REGIS PASSWORD-"],
                values["-REGIS AGE-"], values["-REGIS GENDER-"]
            ])
            info.close()
            info = open(f"Archivos{os.sep}informacion_usuarios.csv", "a")
            change_login_layout(window, event)

info.close()

window.close()