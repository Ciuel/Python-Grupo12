def change_login_layout(login_window,event):
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

def age_field_check(login_window,event):
  """Previene que el usuario escriba caracteres no numericos en el campo de edad

  Args:
      login_window (window): La ventana donde ocurre el chequeo
      event (string): el evento que ocurre en la ventana
  """  
  if event == "-REGIS AGE-":
      if values['-REGIS AGE-'] and values['-REGIS AGE-'][-1] not in ('0123456789'):
          window['-REGIS AGE-'].update(values['-REGIS AGE-'][:-1])

'''def confirm_password(login_window,event):
    if event == "-REGIS CONFIRM PASSWORD-":
            if values["-REGIS CONFIRM PASSWORD-"] != values["-REGIS PASSWORD-"]:
                window["-CONFIRMATION TEXT-"].update("Las contraseñas no coinciden")
            else:
                window["-CONFIRMATION TEXT-"].update("")'''