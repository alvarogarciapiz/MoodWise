import datetime
import os
import time


#Recibe un diccionario del tipo {DATE: EMOCION}
def guardarEstadisticas(dataEmociones, username):
    file = open("TFG/data/users/" + username + "/emociones.txt", "a")
    for clave, valor in dataEmociones.items():
        line = clave + "|" + valor
        file.write(line + os.linesep)
    file.close()


def simularEmociones():
    dataEmociones = {datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"): "triste"}
    for i in range(1,11):
        time.sleep(0.5)
        date = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        dataEmociones[date] = "cansado"
    guardarEstadisticas(dataEmociones, "a")

#simularEmociones()