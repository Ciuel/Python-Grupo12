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


def bombCounter(template_in, linepos, stringpos):
    cont = 0
    for e in range(linepos - 1, linepos + 1):
        print()
        if (not (e < 0) or (e > len(template_in))):
            for se in range(stringpos - 1, stringpos + 1):
                if (not (se < 0) or (se > len(template_in[e]))):
                    print("Estoy en la pos: ",gie," ",se)
                    if template_in[e][se] == '*':
                        cont += 1
    return cont


def bombRecognition(template_in):
    template_out = []
    for i in range(len(template_in)):
        lst_string = []
        for j in range(len(template_in[i])):
            if template_in[i][j] == '*':
                lst_string.append("*")
            else:
                lst_string.append(str(bombCounter(template_in, i, j)))
        template_out.append("".join(lst_string))
    return template_out


for e in bombRecognition(template_minas_medio):
    print(e)
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