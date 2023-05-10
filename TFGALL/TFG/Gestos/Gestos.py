import datetime
import os
import time


#Recibe un diccionario del tipo {DATE: GESTO}
def guardarEstadisticas(dataGestos, username):
    gestos = limpiarRegistros(dataGestos)
    file = open("TFG/data/users/" + username + "/gestos.txt", "a")
    for clave, valor in gestos.items():
        line = clave + "|" + valor
        file.write(line + os.linesep)
    file.close()

#Durante la lectura de gestos hay segundos donde no se registra ningún gesto,
#este método limpia esos segundos vacíos dejando un diccionario con datos
def limpiarRegistros(gestos):
    gestosNew = {}
    for clave, valor in gestos.items():
        if valor!= '':
            gestosNew[clave] = valor
    return gestosNew

#Método para reducir el número de frecuencia de gestos aparecidos
def reducirGestos(gestos):
    return gestos