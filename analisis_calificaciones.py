from guardado_de_observaciones import guardar_observaciones_nuevo_archivo, guadar_observaciones_nueva_hoja

tabla_calificaciones_erroneas = [["Codigo","Calificacion","Observacion"]]

def analizar_calificacion(data,nombre_archivo):
    for i in range(len(data)):
        dato = (data[i][7])
        if str(dato) == "None":
            tabla_calificaciones_erroneas.append([int(data[i][1]),"","Campo Vacio"])
            continue
        if not (dato >= 0 and dato <= 20):
            tabla_calificaciones_erroneas.append([int(data[i][1]),int(dato),"Calificacion fuera de los rangos permitidos"])
            continue
    guadar_observaciones_nueva_hoja(tabla_calificaciones_erroneas, "calificaciones_erronesas",nombre_archivo)