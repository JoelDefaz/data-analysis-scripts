import re
import openpyxl
from datetime import datetime

from guardado_de_observaciones import guardar_observaciones_nuevo_archivo, guadar_observaciones_nueva_hoja

tabla_fechas_incorrectas = [["Codigo","Fecha","Observacion"]]

def analizar_fecha_de_nacimiento(data, nombre_archivo):
    for i in range(len(data)):
        fecha_nacimiento = str(data[i][5])[0:10]
        try:
            fecha = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
            dia = fecha.day
            mes = fecha.month
            año = fecha.year
            if not es_fecha_valida(dia, mes, año):
                tabla_fechas_incorrectas.append([int(data[i][1]), fecha_nacimiento, "Fecha No Valida"])

        except ValueError:
            tabla_fechas_incorrectas.append([int(data[i][1]), "", "Campo Vacio"])
    guadar_observaciones_nueva_hoja(tabla_fechas_incorrectas, "fechas_incorrectas",nombre_archivo)
def es_fecha_valida(dia, mes, año):
    try:
        fecha = datetime(year=año, month=mes, day=dia)

        return fecha.day == dia and fecha.month == mes and fecha.year == año
    except ValueError:
        return False