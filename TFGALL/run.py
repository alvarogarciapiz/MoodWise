import subprocess, sys, os, zipfile

    
if len(sys.argv) > 1:
    # [LOG] => 'Se descarga al escritorio el log del usuario especificado.'  Ej.: 'python run.py log a'
    if sys.argv[1] == "log":
        ruta_origen = os.getcwd() + "/TFG/data/users/" + sys.argv[2] + "/log.txt"
        ruta_escritorio = os.path.join(os.path.expanduser("~"), "Desktop/")
        comando1 = "cp " + ruta_origen + " " + ruta_escritorio
        subprocess.call(comando1, shell=True)
        print("Se ha descargado el log del usuario " + sys.argv[2] + " en su escritorio")

    # [BACKUP] => 'Se descarga al escritorio una copia de seguridad de los datos de los usuarios'  Ej.: 'python run.py backup'
    if sys.argv[1] == "backup":
        #Primero se crea el zip
        directorio = os.getcwd() + "/TFG/data/users"
        with zipfile.ZipFile("backup.zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(directorio):
                for file in files:
                    ruta_archivo = os.path.join(root, file)
                    zipf.write(ruta_archivo, os.path.relpath(ruta_archivo, directorio))

        #Segundo se mueve al escritorio
        ruta_origen = os.getcwd() + "/backup.zip"
        ruta_escritorio = os.path.join(os.path.expanduser("~"), "Desktop/")
        comando2 = "mv " + ruta_origen + " " + ruta_escritorio
        subprocess.call(comando2, shell=True)
        print("Copia de seguridad guardada en su escritorio")

    else:
        print("Introduzca una opción correcta.")
        print("[LOG=> 'python run.py log username']")
else:
    comando = "python TFG/IU/LoginRegistro.py"
    output = subprocess.run(comando, shell=True, capture_output=True, text=True)