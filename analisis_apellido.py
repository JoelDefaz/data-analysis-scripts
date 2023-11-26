import re

from guardado_de_observaciones import guadar_observaciones_nueva_hoja

patron_para_caracteres_especiales = re.compile(r'[^a-zA-Z0-9\s]')
tabla_apellidos_incorrectos = [["Codigo_Estudiante","Apellido","Observacion"]]
def analizar_apellido(data,nombre_archivo):
    for i in range(len(data)):
        apellidos = data[i][9]
        if str(apellidos) == 'None':
            tabla_apellidos_incorrectos.append([data[i][1],"", "Campo Vacio"])
            continue
        apellidos_aislados = str(apellidos).split()
        if not (len(apellidos_aislados) > 0 and len(apellidos_aislados) < 3):
            tabla_apellidos_incorrectos.append([data[i][1],str(apellidos), "Error de tipeo [Nombre+Apellido] o Apellidos Compuestos"])
            continue
        if patron_para_caracteres_especiales.search(apellidos):
            tabla_apellidos_incorrectos.append([data[i][1],str(apellidos), "Precaucion: Caracteres Especiales"])
            continue
    guadar_observaciones_nueva_hoja(tabla_apellidos_incorrectos, "apellidos_erroneas",nombre_archivo)
