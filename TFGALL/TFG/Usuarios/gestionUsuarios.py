import sys
sys.path.append('/Users/alvaro/Desktop/TFGALL/TFG')
import json
import Usuarios.User
from Usuarios import User
import os
import hashlib
from data import Log

# Método que devuelve True si el login es correcto, False si es incorrecto y None si no se encuentra el username
def comprobarLogin(username, password):
    if not comprobarUsername(username):
        return False
    else:
        password = passwordToHash(password)
        file = open('TFG/data/users.json')
        data = json.load(file)
        for i in data['users']:
            if (i['username'] == username):
                if (i['password'] == password):
                    Log.makeLog("LOGIN", username)
                    return True
                else:
                    return False
        file.close()


# Método que devuelve True si el username se encuentra en uso y None si no lo está
def comprobarUsername(username):
    file = open('TFG/data/users.json')
    data = json.load(file)
    for i in data['users']:
        if (i['username'] == username):
            return True

    file.close()


def crearEstructuraDirectorio(username):
    # Crear el directorio
    new_dir_name = username
    parent_dir_path = "TFG/data/users"
    new_dir_path = os.path.join(parent_dir_path, new_dir_name)
    os.mkdir(new_dir_path)

    # Creación de ficheros
    file = open("TFG/data/users/" + username + "/gestos.txt", "w")
    file.close()
    file = open("TFG/data/users/" + username + "/emociones.txt", "w")
    file.close()
    file = open("TFG/data/users/" + username + "/log.txt", "w")
    file.close()
    Log.makeLog("DIRECTORIOS", username)


def registrarUsuario(nombre, apellidos, username, password):
    if comprobarUsername(username):
        return False
    else:
        password = passwordToHash(password)
        rutaEmociones = "TFG/data/users/" + username + "/emociones.txt"
        rutaGestos = "TFG/data/users/" + username + "/gestos.txt"
        with open('TFG/data/users.json', 'r+') as file:
            file_data = json.load(file)
            sr = User.Usuario(nombre, apellidos, username, password, rutaGestos, rutaEmociones)
            file_data["users"].append(sr.__dict__)
            file.seek(0)
            json.dump(file_data, file, indent=4)
        file.close()
    crearEstructuraDirectorio(username)
    Log.makeLog("REGISTRO", username)
    return True

def passwordToHash(password):
    bytes = password.encode('utf-8')
    objetoHash = hashlib.sha256(bytes)
    passwordHash = objetoHash.hexdigest()
    return passwordHash


def obtenerUsuario(username):
    rutaEmociones = "TFG/data/users/" + username + "/emociones.txt"
    rutaGestos = "TFG/data/users/" + username + "/gestos.txt"
    file = open('TFG/data/users.json')
    data = json.load(file)
    for i in data['users']:
        if (i['username'] == username):
            user = User.Usuario(i['nombre'], i['apellidos'], i['username'], i['password'], rutaGestos, rutaEmociones)
    file.close()
    return user