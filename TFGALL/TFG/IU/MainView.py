import sys
sys.path.append('/Users/alvaro/Desktop/TFGALL/TFG')
import data
import tkinter as tk
import customtkinter
from PIL import Image
import subprocess
import sys
import main, os, time
from Gestos import registrarGestos
from Emociones import registrarEmociones

#Configuración general de la ventana
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

def limpiarDirectorio(directorio):
    for archivo in os.listdir(directorio):
        ruta_completa = os.path.join(directorio, archivo)
        if os.path.isfile(ruta_completa):
            os.remove(ruta_completa)
        else:
            os.rmdir(ruta_completa)

    # Elimina el directorio vacío
    os.rmdir(directorio)

#Las siguientes funciones lo que hacen es llevar al resto de interfaces cuando los botones son presionados
def iniciarGestos():
    data.Log.makeLog("GESTOS", main.Username)

    # ---------- FOTO ---------- 
    #ruta = registrarGestos.foto(main.Username)
    #comando = "python yolov7/detect.py --weights yolov7/runs/train/exp/weights/best.pt --conf 0.1 --source " + ruta
    #output = subprocess.run(comando, shell=True, capture_output=True, text=True)

    # ---------- VIDEO ---------- 
    ruta = registrarGestos.video(main.Username)
    print(ruta)
    comando = "python yolov7/detect.py --weights yolov7/runs/train/exp/weights/bestGEST.pt --conf 0.3 --source " + ruta
    output = subprocess.run(comando, shell=True, capture_output=True, text=True)
    registrarGestos.mostrarVideoProcesado("runs/detect/exp/video.mp4")
    time.sleep(1)
    limpiarDirectorio("runs/detect/exp")

def iniciarEmociones():
    data.Log.makeLog("EMOCIONES", main.Username)
    
    # ---------- FOTO ---------- 
    #ruta = registrarEmociones.foto(main.Username)
    #comando = "python yolov7/detect.py --weights yolov7/runs/train/exp/weights/best.pt --conf 0.1 --source " + ruta
    #output = subprocess.run(comando, shell=True, capture_output=True, text=True)

    # ---------- VIDEO ---------- 
    ruta = registrarEmociones.video(main.Username)
    comando = "python yolov7/detect.py --weights yolov7/runs/train/exp/weights/bestEMO.pt --conf 0.3 --source " + ruta
    output = subprocess.run(comando, shell=True, capture_output=True, text=True)
    registrarEmociones.mostrarVideoProcesado("runs/detect/exp/video.mp4")
    time.sleep(1)
    limpiarDirectorio("runs/detect/exp")

def viualizarGestos():
    data.Log.makeLog("VISGESTOS", main.Username)
    import viewEstadisticasGestos
    viewEstadisticasGestos(ventana)

def visualizarEmociones():
    data.Log.makeLog("VISEMOCIONES", main.Username)
    import viewEstadisticasEmociones
    viewEstadisticasEmociones(ventana)

def exportarGestos():
    data.Log.makeLog("EXPGESTOS", main.Username)
    import exportarEstadisticasGestos
    exportarEstadisticasGestos(ventana)

def exportarEmociones():
    data.Log.makeLog("EXPEMOCIONES", main.Username)
    import exportarEstadisticasEmociones
    exportarEstadisticasEmociones(ventana)


# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("MoodWise")
ventana.geometry("450x240")
ventana.resizable(width=False, height=False)

# Creamos dos marcos (uno para cada columna)
marco1 = tk.Frame(ventana)
marco1.pack(side=tk.LEFT, padx=10, pady=10)
marco2 = tk.Frame(ventana)
marco2.pack(side=tk.LEFT, padx=10, pady=10)

#Iconos
descarga = customtkinter.CTkImage(light_image=Image.open("TFG/assets/descargar.png"),
                                  dark_image=Image.open("TFG/assets/descargar.png"),
                                  size=(15, 15))

gestos = customtkinter.CTkImage(light_image=Image.open("TFG/assets/gestos.png"),
                                  dark_image=Image.open("TFG/assets/gestos.png"),
                                  size=(15, 15))

emociones = customtkinter.CTkImage(light_image=Image.open("TFG/assets/emociones.png"),
                                  dark_image=Image.open("TFG/assets/emociones.png"),
                                  size=(15, 15))

chart = customtkinter.CTkImage(light_image=Image.open("TFG/assets/chart.png"),
                                  dark_image=Image.open("TFG/assets/chart.png"),
                                  size=(15, 15))

# Elementos para GESTOS
texto1 = customtkinter.CTkLabel(marco1, text="Gestos", font=("Arial", 25), text_color="#3078c5")
texto1.pack(padx=10, pady=10)

boton1 = customtkinter.CTkButton(marco1, text="Iniciar reconocimiento", height=30, width=180, command=iniciarGestos, image=gestos)
boton1.pack(padx=10, pady=10)

boton2 = customtkinter.CTkButton(marco1, text="Estadísticas", height=30, width=180, command=viualizarGestos, image=chart)
boton2.pack(padx=10, pady=10)

boton3 = customtkinter.CTkButton(marco1, text="Exportar estadísticas", height=30, width=180, command=exportarGestos, image=descarga)
boton3.pack(padx=10, pady=10)

# Elementos para EMOCIONES
texto2 = customtkinter.CTkLabel(marco2, text="Emociones", font=("Arial", 25), text_color="#3078c5")
texto2.pack(padx=10, pady=10)

boton4 = customtkinter.CTkButton(marco2, text="Iniciar reconocimiento", height=30, width=180, command=iniciarEmociones, image=emociones)
boton4.pack(padx=10, pady=10)

boton5 = customtkinter.CTkButton(marco2, text="Estadísticas", height=30, width=180, command=visualizarEmociones, image=chart)
boton5.pack(padx=10, pady=10)

boton6 = customtkinter.CTkButton(marco2, text="Exportar estadísticas", height=30, width=180, command=exportarEmociones, image=descarga)
boton6.pack(padx=10, pady=10)


ventana.mainloop()