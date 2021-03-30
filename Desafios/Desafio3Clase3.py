#Queremos implementar una función que dada una colección con datos de usuarios de un
#determinado juego. Tenemos: nombre, nivel y puntaje. Queremos retornar esta colección
#ordenada de acuerdo al nombre

def ordenar(usuario):
    """Funcion creada para darle criterio a la funcion sorted"""
    return usuario[0].lower()

def ordenando_por_nombre(ListIn):
    """ Retorna la lista ordenada por nombre"""
    return sorted(ListIn,key=ordenar)
    
  

usuarios = [
('JonY BoY', 'Nivel3', 15),
('1962', 'Nivel1', 12),
('caike', 'Nivel2', 1020),
('Straka^', 'Nivel2', 1020),
]

print(ordenando_por_nombre(usuarios))