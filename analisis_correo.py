import re

from guardado_de_observaciones import guadar_observaciones_nueva_hoja

extension_de_correo = "@universidad.edu.ec"
patron_para_caracteres_especiales = re.compile(r'[^a-zA-Z0-9\s]')
tabla_correos_incoorrectos = [["Codigo","Correo","Observacion"]]

def analizar_correo(data,nombre_archivo):
    for i in range(len(data)):
        nombres = data[i][8]
        apellidos = data[i][9]
        correo = data[i][10]
        if str(nombres) == 'None' or str(apellidos) == 'None':
            tabla_correos_incoorrectos.append([data[i][1],"", "Campo Vacio"])
            continue
        nombres_aislados = str(nombres).split()
        apellidos_aislados = str(apellidos).split()
        if not (nombres_aislados[0].upper() + "." + apellidos_aislados[0].upper() + extension_de_correo) == correo:
            tabla_correos_incoorrectos.append([data[i][1],str(correo), "Los campos nombre o apellido no coinciden"])
            continue
        if patron_para_caracteres_especiales.search(nombres_aislados[0]) or patron_para_caracteres_especiales.search(apellidos_aislados[0]):
            tabla_correos_incoorrectos.append([data[i][1],str(correo), "Precaucion: Caracteres Especiales"])
            continue
    guadar_observaciones_nueva_hoja(tabla_correos_incoorrectos, "correos_erroneas",nombre_archivo)
