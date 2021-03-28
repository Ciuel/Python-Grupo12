
template_minas = [
    '-*-*-',
    '--*--',
    '----*',
    '*----',
]




def bombCounter(template_in, linepos, stringpos):
    '''Se recorren las posiciones alrededor de una posicion
     formando una matriz de 3x3 en busca de las bombas y evitando las posiciones invalidas'''
    cont = 0
    for e in range(linepos - 1, linepos + 2):
        if (e < 0) or (e > len(template_in) - 1):
            continue
        for se in range(stringpos - 1, stringpos + 2):
            if ((se < 0) or (se > len(template_in[e]) - 1)):
                continue
            if template_in[e][se] == '*':
                cont += 1
    return cont


def bombRecognition(template_in):
    '''Se recorren las posiciones de la lista de strings,
     si es una bomba no se cambia y si no se buscan las bombas de alrededor con la funcion bombCounter 
     y se retorna una lista de strings con los numeros reemplazados'''
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

print()
for e in bombRecognition(template_minas):
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