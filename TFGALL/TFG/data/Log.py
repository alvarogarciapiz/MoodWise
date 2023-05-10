import datetime
import os


#Recibe la acción de tipo [GESTOS, EMOCIONES, LOGIN, REGISTRO, DIRECTORIOS]
def makeLog(operacion, username):
    file = open("TFG/data/users/" + username + "/log.txt", "a")

    if operacion=="GESTOS":
        line = "El usuario " + username + " registró gestos el " + datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    elif operacion=="EMOCIONES":
        line = "El usuario " + username + " registró emociones el " + datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    elif operacion=="LOGIN":
        line = "El usuario " + username + " hizo login el " + datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    elif operacion=="REGISTRO":
        line = "El usuario " + username + " se registró el " + datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    elif operacion=="DIRECTORIOS":
        line = "Se crearon correctamente los directorios del usuario " + username + " el " + datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    elif operacion=="VISGESTOS":
        line = "El usuario " + username + " visualizó estadísticas de gestos el " + datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    elif operacion=="VISEMOCIONES":
        line = "El usuario " + username + " visualizó estadísticas de emociones el " + datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    elif operacion=="EXPGESTOS":
        line = "El usuario " + username + " exportó estadísticas de gestos el " + datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    elif operacion=="EXPEMOCIONES":
        line = "El usuario " + username + " exportó estadísticas de emociones el " + datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    file.write(line + os.linesep)
    file.close()