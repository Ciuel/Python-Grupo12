"Queremos escribir una función que imprima sus argumentos agregando de que tipo son."

def imprimir_muchos(*args):
    """Imprime los argumentos y sus tipos"""
    
    for arg in args:
        print(f'El parametro es {arg} y su tipo es {type(arg)}')


imprimir_muchos(15,"hola")
imprimir_muchos([1,2,3])