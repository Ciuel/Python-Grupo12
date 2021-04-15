'''
10. Escriba un programa que solicite por teclado una palabra y calcule el valor de la misma dada
la siguiente tabla de valores del juego Scrabble:

Letra valor
A, E, I, O, U, L, N, R, S, T 1
D, G 2
B, C, M, P 3
F, H, V, W, Y 4
K 5
J, X 8
Q, Z 10

*Tenga en cuenta qué estructura elige para guardar estos valores en Python
Ejemplo 1
• Palabra: “solo”
• valor: 4
Ejemplo 2
• Palabra: “tomate”
• valor: 8
'''


palabra = input("Escriba una palabra: ").upper() #Se ingresa por teclado la palabra

dicci_Scrabble = {
    ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"): 1,   #Creo un diccionario con los puntajes determinados en la consigna, para luego procesar la palabra con este diccionario
    ("D", "G"): 2,
    ("B", "C", "M", "P"): 3,
    ("F", "H", "V", "W", "Y"): 4,
    ("K"): 5,
    ("J","X"): 8,
    ("Q","Z"): 10
}
valor_palabra=0 #Contador Total

for char in palabra:
    for tup in dicci_Scrabble:     #Itero la palabra consiguiendo cada letra y luego, busco la letra dentro del diccionario, para conocer su valor
        if char in tup:
            valor_palabra+=dicci_Scrabble[tup]  #Una vez encontrado el valor de esa letra, aumento el contrador total con el valo propuesto para esa letra
            
print(f"La palabra: {palabra.lower()} vale {valor_palabra} puntos")

