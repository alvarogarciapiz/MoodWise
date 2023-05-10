import sys
sys.path.append('/Users/alvaro/Desktop/TFGALL/TFG')
import tkinter as tk
import customtkinter
from tkcalendar import DateEntry
import main
import Usuarios
from Gestos import EstadisticasGestos

#Se exportan los datos a un fichero PDF
def on_button_click():
    # Obtener las fechas seleccionadas
    fecha_inicio = cal_inicio.get()
    fecha_fin = cal_fin.get()
    user = Usuarios.gestionUsuarios.obtenerUsuario(main.Username)
    est = EstadisticasGestos.EstadisticasGestos(user)
    est.exportarEstadisticas(fecha_inicio, fecha_fin)

#Se exportan los datos a un fichero de excel
def on_button_click_excel():
    # Obtener las fechas seleccionadas
    fecha_inicio = cal_inicio.get()
    fecha_fin = cal_fin.get()
    user = Usuarios.gestionUsuarios.obtenerUsuario(main.Username)
    est = EstadisticasGestos.EstadisticasGestos(user)
    est.exportarEstadisticasExcel(fecha_inicio, fecha_fin)

# Crear la ventana
ventana = tk.Tk()
ventana.geometry("333x300")
ventana.title("Exportar Estadísticas de Gestos")
ventana.resizable(width=False, height=False)

# Crear los selectores de fechas
etiqueta_inicio = tk.Label(ventana, text="Fecha de inicio:")
etiqueta_inicio.pack(padx=10, pady=10)
cal_inicio = DateEntry(ventana, width=12, background='darkblue',
                       foreground='white', borderwidth=2, date_pattern='y-mm-dd')
cal_inicio.pack(padx=10, pady=10)

etiqueta_fin = tk.Label(ventana, text="Fecha de fin:")
etiqueta_fin.pack(padx=10, pady=10)
cal_fin = DateEntry(ventana, width=12, background='darkblue',
                    foreground='white', borderwidth=2, date_pattern='y-mm-dd')
cal_fin.pack(padx=10, pady=10)

# Crear el botón
boton = customtkinter.CTkButton(ventana, text="Descargar en PDF", command=on_button_click)
boton.pack(padx=10, pady=10)

# Crear el botón
boton = customtkinter.CTkButton(ventana, text="Descargar para Excel", command=on_button_click_excel)
boton.pack(padx=10, pady=10)

info = tk.Label(ventana, text="Los datos con las fechas seleccionadas \nserán exportados en su escritorio")
info.pack(padx=10, pady=10)

# Mostrar la ventana
ventana.mainloop()
