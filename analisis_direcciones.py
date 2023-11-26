import re

from guardado_de_observaciones import guadar_observaciones_nueva_hoja

patron_con_numeros = re.compile(r'[0-9]|s/n|S/N')
contiene = re.compile(r'PRIMAVERA')
empieza = r'^PRIMAVERA'
tabla_direcciones_incorrectas = [["Codigo","Direccion","Observacion"]]

def analizar_direccion(data,nombre_archivo):
    for i in range(len(data)):
        direccion = str(data[i][3])
        if direccion == "None":
            tabla_direcciones_incorrectas.append([int(data[i][1]),"","Campo Vacio"])
            continue
        if not patron_con_numeros.search(direccion):
            tabla_direcciones_incorrectas.append([int(data[i][1]),direccion,"Solo calles o sectores"])
            continue
        if contiene.search(direccion) and not (re.match(empieza,direccion.upper())):
            tabla_direcciones_incorrectas.append([int(data[i][1]),direccion,"Formato Confuso"])
            continue
    guadar_observaciones_nueva_hoja(tabla_direcciones_incorrectas,"direcciones_incorrectas",nombre_archivo)