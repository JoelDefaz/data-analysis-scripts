import openpyxl

from guardado_de_observaciones import guardar_observaciones_nuevo_archivo, guadar_observaciones_nueva_hoja

tabla_telefonos_erroneos = [["Codigo", "Telefono", "Observacion"]]

def analizar_telefono(data,nombre_archivo):
    for i in range(len(data)):
        dato = str(data[i][4])
        ########################################
        if dato == "None":
            tabla_telefonos_erroneos.append([int(data[i][1]),"", "Campo Vacio"])
            continue
        ########################################
        if not len(str(dato)) == 7:
            tabla_telefonos_erroneos.append([int(data[i][1]), int(dato), "Digitos Incompletos"])
            continue
    guadar_observaciones_nueva_hoja(tabla_telefonos_erroneos, "telefonos_erroneos",nombre_archivo)