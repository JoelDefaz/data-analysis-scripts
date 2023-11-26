import re

from guardado_de_observaciones import guadar_observaciones_nueva_hoja

patron_para_caracteres_especiales = re.compile(r'[^a-zA-Z0-9\s]')
tabla_nombres_incorrectos = [["Codigo","Nombre","Observacion"]]

def analizar_nombre(data,nombre_archivo):
    for i in range(len(data)):
        nombres = data[i][8]
        if str(nombres) == 'None':
            tabla_nombres_incorrectos.append([data[i][1],"", "Campo Vacio"])
            continue
        nombres_aislados = str(nombres).split()
        if not (len(nombres_aislados) > 0 and len(nombres_aislados) < 4):
            tabla_nombres_incorrectos.append([data[i][1],str(nombres), "Cantidad de nombres NO valido"])
            continue
        if patron_para_caracteres_especiales.search(nombres):
            tabla_nombres_incorrectos.append([data[i][1],str(nombres), "Precaucion: Caracteres Especiales"])
            continue
    guadar_observaciones_nueva_hoja(tabla_nombres_incorrectos,"nombres_no_vaidos",nombre_archivo)