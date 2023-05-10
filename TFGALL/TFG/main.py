import sys
sys.path.append('/Users/alvaro/Desktop/TFGALL/TFG')
from Usuarios import gestionUsuarios, User
import subprocess
#subprocess.call(['python', 'IU/LoginRegistro.py'])

#variables de la sesión
Nombre, Apellidos, Username = None, None, None

def init(username):
    user = gestionUsuarios.obtenerUsuario(username)
    global Nombre
    Nombre= user.nombre
    global Apellidos
    Apellidos = user.apellidos
    global Username
    Username = user.username

    ruta = "username.txt"
    file = open(ruta, "w")
    file.write(username)
    file.close()