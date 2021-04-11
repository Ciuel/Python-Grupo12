import json
archivo = open("bandas.json", "w")
datos = [
{"nombre": "William Campbell", "ciudad": "La Plata", "ref": "www.instagram.com/williamcampbellok"},
{"nombre": "Buendia", "ciudad": "La Plata", "ref":"https://buendia.bandcamp.com/"},
{"nombre": "Lúmine", "ciudad": "La Plata", "ref": "https://www.instagram.com/luminelp/"}]
json.dump(datos, archivo,indent=2)
archivo.close()

archivo = open("bandas.json", "r")
datos = json.load(archivo)
datos_a_mostrar = json.dumps(datos, indent=4)
print(datos_a_mostrar)
archivo.close()
