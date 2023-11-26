import re
import openpyxl

from guardado_de_observaciones import guardar_observaciones_nuevo_archivo, guadar_observaciones_nueva_hoja

tabla_cedulas_erroneos = [["codigo", "Cedula", "Observacion"]]

def analizar_cedula(data,nombre_archivo):
    verificacion = "212121212"
    suma_total = 0
    for i in range(len(data)):
        dato = str(data[i][2])
        ########################################
        if dato == 'None':
            tabla_cedulas_erroneos.append([int(data[i][1]), "", "Campo Vacio"])
            continue
        ########################################
        if len(str(dato)) not in [9,10]:
            tabla_cedulas_erroneos.append([int(data[i][1]), int(dato), "Digitos Incompletos"])
            continue
        #######################################
        if len(str(dato)) == 9:
            if not dato or not re.match(r'^[1-9][0-5][0-9]{7}',dato):
                tabla_cedulas_erroneos.append([int(data[i][1]), int(dato), "Mal Inicio"])
                continue
        else:
            if not dato or not re.match(r'^(1[0-9]|2[0-4])[0-5][0-9]{7}', dato):
                tabla_cedulas_erroneos.append([int(data[i][1]), int(dato), "Mal Inicio"])
                continue
        ########################################
        if len(str(dato)) == 9:
            verificar_ultimo_digito(i,"0"+dato,data)
            continue
        else:
            verificar_ultimo_digito(i,dato,data)
            continue
    guadar_observaciones_nueva_hoja(tabla_cedulas_erroneos, "cedulas_erroneas",nombre_archivo)
            
def verificar_ultimo_digito(i, dato,data):
    coeficientes = "212121212"
    suma_total = 0
    for j in range(9):
        multiplicacion = int(dato[j]) * int(coeficientes[j])
        if (multiplicacion >= 10):
            multiplicacion = multiplicacion - 9
        suma_total = suma_total + multiplicacion
    decena_superior = ((suma_total//10)+1)*10
    verificar = decena_superior - suma_total
    if not (((verificar == 10) and (dato[9] == '0')) or (verificar == int(dato[9]))):
        tabla_cedulas_erroneos.append([int(data[i][1]), int(dato), "Ultimo Digito NO valido"])