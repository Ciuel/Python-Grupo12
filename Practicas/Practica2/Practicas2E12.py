template_minas_facil = [
    '-*---',
    '-----',
    '----*',
    '*----',
]

template_minas_medio = [
    '-*-*-',
    '--*--',
    '----*',
    '*----',
]

template_minas_dificil = [
    '-*-*-',
    '--*--',
    '-*--*',
    '*--*-',
]

def bombRecognition(template_in):
    for i in range(len(template_in)):
        for j in range(len(template_in[i])):
            if template_in[i][j]=='-':
                




bombRecognition(template_minas_facil)





'''12. La idea es tratar de programar una de las partes principales del juego “Buscaminas”. La idea
es que dado una estructura que dice que celdas tienen minas y que celdas no las tienen, como
la siguiente:
[
'-*-*-',
'--*--',
'----*',
'*----',
]
Generar otra que indique en las celdas vacías la cantidad de bombas que la rodean, para el ejemplo
anterior, sería:
[
'1*3*1',
'12*32',
'1212*',
'*1011',
]
Nota: Defina al menos una función en el código (si hay mas mejor) y documente las mismas con
docstring que es lo que hacen.'''