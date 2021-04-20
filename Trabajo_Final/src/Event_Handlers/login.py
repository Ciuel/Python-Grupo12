import csv
import os

def change_login_layout(window,event):
  """Cambia de la ventana de login a la de registros
   si el usuario clickea el texto de registrarse
  Args:
      login_window (window): La ventana que cambia de layout
      event (string): el evento que ocurre en la ventana
  """  
  if event == "Registrarse":
    window['login'].update(visible=False)
    window['regis'].update(visible=True)
  elif event == "-REGIS SAVE-":
    window['login'].update(visible=True)
    window['regis'].update(visible=False)

def age_field_check(window,event,values):
  """Previene que el usuario escriba caracteres no numericos en el campo de edad"""

  if event == "-REGIS AGE-":
      if values['-REGIS AGE-'] and values['-REGIS AGE-'][-1] not in ('0123456789'):
          window['-REGIS AGE-'].update(values['-REGIS AGE-'][:-1])

def confirm_password(window,event,values):
    if event == "-REGIS CONFIRM PASSWORD-":
        if values["-REGIS CONFIRM PASSWORD-"] != values["-REGIS PASSWORD-"]:
            window["-CONFIRMATION TEXT-"].update("Las contraseñas no coinciden")
        else:
            window["-CONFIRMATION TEXT-"].update("")

def check_fields_and_register(window,event,values,info):  #Funciona mal, hay que repensar este
    if event == "-REGIS SAVE-":
        if values["-REGIS GENDER-"] in ['Hombre', 'Mujer', 'No binario', 'Otro'] and (values["-REGIS NICK-"] != "") and values["-REGIS PASSWORD-"] != "" and values["-REGIS AGE-"] != "":  #Previene registros con campos vacios
            writer=csv.writer(info)
            writer.writerow([values["-REGIS NICK-"], values["-REGIS PASSWORD-"],values["-REGIS AGE-"],values["-REGIS GENDER-"]])
            info.close()
            
            info = open(f"Trabajo_final{os.sep}src{os.sep}Data_files{os.sep}informacion_usuarios.csv", "a")
            change_login_layout(window,event)