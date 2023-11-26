import re
import openpyxl
from datetime import datetime
from guardado_de_observaciones import guardar_observaciones_nuevo_archivo, guadar_observaciones_nueva_hoja

tabla_edades_incorrectas = [["Codigo","Edad","Observacion"]]

def analizar_edad(data,nombre_archivo):
    for i in range(len(data)):
        edad_est = str(data[i][6])
        fecha_nacimiento = str(data[i][5])[0:10]
        if edad_est == "None":
            tabla_edades_incorrectas.append([int(data[i][1]), "", "Campo Vacio"])
            continue
        if not calcular_edad(fecha_nacimiento,2020) == int(edad_est):
            tabla_edades_incorrectas.append([int(data[i][1]), int(edad_est), "Edad Incorrecta"])
            continue
    guadar_observaciones_nueva_hoja(tabla_edades_incorrectas, "edades_incorrectas",nombre_archivo)

def calcular_edad(fecha_nacimiento, año_referencia):
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
    edad = año_referencia - fecha_nacimiento.year - (
                (año_referencia, fecha_nacimiento.month, fecha_nacimiento.day) < (
        año_referencia, datetime.now().month, datetime.now().day))
    return edad